#!/usr/bin/env python3
"""
GitHub Activity Bot - Automated Git Push Script
Handles pushing code to specified repository and branch with automatic branch creation and pull updates.

Author: GitHub Activity Bot
Created: 2024
"""

import os
import sys
import subprocess
import argparse
import json
from typing import Optional, Dict, Any
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('git_push_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class GitPushBot:
    """
    Automated Git operations bot that handles:
    - Pulling latest changes from remote branch
    - Creating branches if they don't exist
    - Adding, committing, and pushing changes
    - Error handling and logging
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the Git Push Bot
        
        Args:
            config_path: Path to configuration file (optional)
        """
        self.config = self._load_config(config_path)
        self.repo_path = self.config.get('repo_path', os.getcwd())
        self._setup_git_user()
        logger.info(f"Initialized GitPushBot for repository: {self.repo_path}")
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from file or use defaults"""
        default_config = {
            "repo_path": os.getcwd(),
            "default_branch": "main",
            "default_remote": "origin",
            "auto_stage_all": True,
            "create_branch_if_missing": True,
            "pull_before_push": True
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                default_config.update(user_config)
                logger.info(f"Loaded configuration from: {config_path}")
            except Exception as e:
                logger.warning(f"Failed to load config from {config_path}: {e}")
                logger.info("Using default configuration")
        
        return default_config
    
    def _setup_git_user(self):
        """Setup git user configuration from config file"""
        git_user = self.config.get('git_user', {})
        name = git_user.get('name')
        email = git_user.get('email')
        
        if name and email:
            try:
                # Set git user for this repository
                self._run_command(['git', 'config', 'user.name', name], check_return_code=False)
                self._run_command(['git', 'config', 'user.email', email], check_return_code=False)
                logger.info(f"Git user configured: {name} <{email}>")
            except subprocess.CalledProcessError:
                logger.warning("Failed to configure git user - using system defaults")
        else:
            logger.debug("No git user configuration found in config file")
    
    def _run_command(self, command: list, check_return_code: bool = True) -> subprocess.CompletedProcess:
        """
        Execute a shell command and handle errors
        
        Args:
            command: Command to execute as list
            check_return_code: Whether to raise exception on non-zero return code
            
        Returns:
            subprocess.CompletedProcess object
        """
        try:
            logger.debug(f"Executing command: {' '.join(command)}")
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=check_return_code
            )
            
            if result.stdout.strip():
                logger.debug(f"Command output: {result.stdout.strip()}")
            
            return result
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {' '.join(command)}")
            logger.error(f"Error output: {e.stderr}")
            raise
    
    def check_git_repo(self) -> bool:
        """Check if current directory is a Git repository"""
        try:
            self._run_command(['git', 'rev-parse', '--git-dir'])
            return True
        except subprocess.CalledProcessError:
            logger.error(f"Directory {self.repo_path} is not a Git repository")
            return False
    
    def get_current_branch(self) -> str:
        """Get the current Git branch name"""
        try:
            result = self._run_command(['git', 'branch', '--show-current'])
            current_branch = result.stdout.strip()
            logger.info(f"Current branch: {current_branch}")
            return current_branch
        except subprocess.CalledProcessError:
            logger.error("Failed to get current branch")
            raise
    
    def branch_exists_remote(self, branch_name: str, remote: str = "origin") -> bool:
        """Check if branch exists on remote repository"""
        try:
            self._run_command(['git', 'ls-remote', '--heads', remote, branch_name])
            return True
        except subprocess.CalledProcessError:
            return False
    
    def branch_exists_local(self, branch_name: str) -> bool:
        """Check if branch exists locally"""
        try:
            result = self._run_command(['git', 'branch', '--list', branch_name], check_return_code=False)
            return branch_name in result.stdout
        except subprocess.CalledProcessError:
            return False
    
    def create_branch(self, branch_name: str, switch_to_branch: bool = True) -> bool:
        """
        Create a new Git branch
        
        Args:
            branch_name: Name of the branch to create
            switch_to_branch: Whether to switch to the new branch
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if switch_to_branch:
                self._run_command(['git', 'checkout', '-b', branch_name])
                logger.info(f"Created and switched to new branch: {branch_name}")
            else:
                self._run_command(['git', 'branch', branch_name])
                logger.info(f"Created new branch: {branch_name}")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to create branch {branch_name}: {e}")
            return False
    
    def switch_branch(self, branch_name: str) -> bool:
        """Switch to specified branch"""
        try:
            self._run_command(['git', 'checkout', branch_name])
            logger.info(f"Switched to branch: {branch_name}")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to switch to branch {branch_name}: {e}")
            return False
    
    def pull_latest(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """
        Pull latest changes from remote repository
        
        Args:
            remote: Remote repository name
            branch: Branch name (if None, uses current branch)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if branch is None:
                branch = self.get_current_branch()
            
            # Check if remote branch exists
            if not self.branch_exists_remote(branch, remote):
                logger.warning(f"Remote branch {remote}/{branch} does not exist, skipping pull")
                return True
            
            self._run_command(['git', 'pull', remote, branch])
            logger.info(f"Successfully pulled latest changes from {remote}/{branch}")
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to pull from {remote}/{branch}: {e}")
            return False
    
    def stage_changes(self, files: Optional[list] = None) -> bool:
        """
        Stage changes for commit
        
        Args:
            files: List of files to stage (if None, stages all changes except excluded)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if files is None:
                # Get excluded patterns from config
                excluded_patterns = self.config.get('excluded_files', []).copy()
                
                # Always exclude the github_activity_bot folder regardless of current directory
                bot_exclusions = [
                    'github_activity_bot/',
                    'github_activity_bot/*',
                    'github_activity_bot/**',
                    './github_activity_bot/',
                    './github_activity_bot/*'
                ]
                excluded_patterns.extend(bot_exclusions)
                
                # Safety check: warn if running from bot directory
                current_dir = os.path.basename(os.getcwd())
                if current_dir == 'github_activity_bot':
                    logger.warning("⚠️  RUNNING FROM BOT DIRECTORY!")
                    logger.warning("⚠️  For best results, run from repository root directory")
                    logger.warning("⚠️  This may cause the bot folder to be included in commits")
                
                # Stage all changes first
                self._run_command(['git', 'add', '.'])
                logger.debug("Added all files to staging")
                
                # Remove excluded patterns from staging
                excluded_count = 0
                for pattern in excluded_patterns:
                    try:
                        result = self._run_command(['git', 'reset', 'HEAD', pattern], check_return_code=False)
                        if result.returncode == 0:
                            excluded_count += 1
                            logger.debug(f"Unstaged pattern: {pattern}")
                    except subprocess.CalledProcessError:
                        pass  # Pattern might not exist
                
                if excluded_count > 0:
                    logger.info(f"Staged all changes (excluded {excluded_count} patterns including github_activity_bot)")
                else:
                    logger.info("Staged all changes (no exclusion patterns matched)")
                    
            else:
                # Stage specific files (make sure none are from bot directory)
                safe_files = []
                for file in files:
                    if not file.startswith('github_activity_bot/') and 'github_activity_bot' not in file:
                        safe_files.append(file)
                        self._run_command(['git', 'add', file])
                    else:
                        logger.warning(f"Skipped bot directory file: {file}")
                
                if safe_files:
                    logger.info(f"Staged files: {', '.join(safe_files)}")
                else:
                    logger.warning("No safe files to stage (all were bot directory files)")
                    
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to stage changes: {e}")
            return False
    
    def commit_changes(self, message: str) -> bool:
        """
        Commit staged changes
        
        Args:
            message: Commit message
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Check if there are any changes to commit
            result = self._run_command(['git', 'status', '--porcelain'], check_return_code=False)
            if not result.stdout.strip():
                logger.info("No changes to commit")
                return True
            
            self._run_command(['git', 'commit', '-m', message])
            logger.info(f"Committed changes with message: {message}")
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to commit changes: {e}")
            return False
    
    def push_changes(self, remote: str = "origin", branch: Optional[str] = None, set_upstream: bool = False) -> bool:
        """
        Push changes to remote repository
        
        Args:
            remote: Remote repository name
            branch: Branch name (if None, uses current branch)
            set_upstream: Whether to set upstream for new branches
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if branch is None:
                branch = self.get_current_branch()
            
            if set_upstream:
                self._run_command(['git', 'push', '-u', remote, branch])
                logger.info(f"Pushed changes to {remote}/{branch} and set upstream")
            else:
                self._run_command(['git', 'push', remote, branch])
                logger.info(f"Pushed changes to {remote}/{branch}")
            
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to push to {remote}/{branch}: {e}")
            return False
    
    def execute_git_workflow(self, 
                           target_branch: str,
                           commit_message: str,
                           remote: str = "origin",
                           files_to_stage: Optional[list] = None) -> bool:
        """
        Execute the complete Git workflow:
        1. Check if target branch exists, create if needed
        2. Switch to target branch
        3. Pull latest changes
        4. Stage changes
        5. Commit changes
        6. Push changes
        
        Args:
            target_branch: Target branch name
            commit_message: Commit message
            remote: Remote repository name
            files_to_stage: Specific files to stage (None for all)
            
        Returns:
            True if successful, False otherwise
        """
        logger.info(f"Starting Git workflow for branch: {target_branch}")
        
        # Verify we're in a Git repository
        if not self.check_git_repo():
            return False
        
        try:
            # Store current branch for potential rollback
            original_branch = self.get_current_branch()
            
            # Handle target branch
            if not self.branch_exists_local(target_branch):
                if self.config.get('create_branch_if_missing', True):
                    if not self.create_branch(target_branch, switch_to_branch=True):
                        return False
                else:
                    logger.error(f"Branch {target_branch} does not exist and auto-creation is disabled")
                    return False
            else:
                # Switch to existing branch
                if not self.switch_branch(target_branch):
                    return False
            
            # Pull latest changes if enabled
            if self.config.get('pull_before_push', True):
                if not self.pull_latest(remote, target_branch):
                    logger.warning("Pull failed, continuing with push...")
            
            # Stage changes
            if not self.stage_changes(files_to_stage):
                return False
            
            # Commit changes
            if not self.commit_changes(commit_message):
                return False
            
            # Push changes (set upstream for new branches)
            set_upstream = not self.branch_exists_remote(target_branch, remote)
            if not self.push_changes(remote, target_branch, set_upstream):
                return False
            
            logger.info(f"Successfully completed Git workflow for branch: {target_branch}")
            return True
            
        except Exception as e:
            logger.error(f"Git workflow failed: {e}")
            return False


def main():
    """Main function to handle command line arguments and execute Git workflow"""
    parser = argparse.ArgumentParser(description="Automated Git Push Bot")
    parser.add_argument('branch', help='Target branch name')
    parser.add_argument('message', help='Commit message')
    parser.add_argument('--remote', default='origin', help='Remote repository name (default: origin)')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--files', nargs='+', help='Specific files to stage (default: all files)')
    parser.add_argument('--repo-path', help='Repository path (default: current directory)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize Git Push Bot
    bot = GitPushBot(config_path=args.config)
    
    # Override repo path if provided
    if args.repo_path:
        bot.repo_path = args.repo_path
    
    # Execute Git workflow
    success = bot.execute_git_workflow(
        target_branch=args.branch,
        commit_message=args.message,
        remote=args.remote,
        files_to_stage=args.files
    )
    
    if success:
        logger.info("Git workflow completed successfully!")
        sys.exit(0)
    else:
        logger.error("Git workflow failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
