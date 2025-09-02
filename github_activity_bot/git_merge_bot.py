#!/usr/bin/env python3
"""
GitHub Merge Bot - Automated Branch Merging Script
Handles merging feature branches into main branch with proper Git workflow.

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
        logging.FileHandler('git_merge_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class GitMergeBot:
    """
    Automated Git merge operations bot that handles:
    - Switching to target branch (usually main)
    - Pulling latest changes
    - Merging feature branches
    - Pushing merged changes
    - Optionally cleaning up merged branches
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the Git Merge Bot
        
        Args:
            config_path: Path to configuration file (optional)
        """
        self.config = self._load_config(config_path)
        self.repo_path = self.config.get('repo_path', os.getcwd())
        self._setup_git_user()
        logger.info(f"Initialized GitMergeBot for repository: {self.repo_path}")
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from file or use defaults"""
        default_config = {
            "repo_path": os.getcwd(),
            "default_target_branch": "main",
            "default_remote": "origin",
            "auto_cleanup_branches": False,
            "require_confirmation": True
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
    
    def branch_exists_local(self, branch_name: str) -> bool:
        """Check if branch exists locally"""
        try:
            result = self._run_command(['git', 'branch', '--list', branch_name], check_return_code=False)
            return branch_name in result.stdout
        except subprocess.CalledProcessError:
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
            
            self._run_command(['git', 'pull', remote, branch])
            logger.info(f"Successfully pulled latest changes from {remote}/{branch}")
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to pull from {remote}/{branch}: {e}")
            return False
    
    def merge_branch(self, source_branch: str, merge_message: Optional[str] = None) -> bool:
        """
        Merge source branch into current branch
        
        Args:
            source_branch: Branch to merge into current branch
            merge_message: Custom merge message (optional)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if merge_message:
                self._run_command(['git', 'merge', source_branch, '-m', merge_message])
            else:
                self._run_command(['git', 'merge', source_branch])
            
            logger.info(f"Successfully merged {source_branch} into current branch")
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to merge {source_branch}: {e}")
            logger.error("You may need to resolve merge conflicts manually")
            return False
    
    def push_changes(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """
        Push changes to remote repository
        
        Args:
            remote: Remote repository name
            branch: Branch name (if None, uses current branch)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if branch is None:
                branch = self.get_current_branch()
            
            self._run_command(['git', 'push', remote, branch])
            logger.info(f"Pushed changes to {remote}/{branch}")
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to push to {remote}/{branch}: {e}")
            return False
    
    def delete_branch(self, branch_name: str, remote: str = "origin", force: bool = False) -> bool:
        """
        Delete branch locally and remotely
        
        Args:
            branch_name: Name of branch to delete
            remote: Remote repository name
            force: Force delete even if not fully merged
            
        Returns:
            True if successful, False otherwise
        """
        success = True
        
        try:
            # Delete local branch
            delete_flag = '-D' if force else '-d'
            self._run_command(['git', 'branch', delete_flag, branch_name])
            logger.info(f"Deleted local branch: {branch_name}")
        except subprocess.CalledProcessError as e:
            logger.warning(f"Failed to delete local branch {branch_name}: {e}")
            success = False
        
        try:
            # Delete remote branch
            self._run_command(['git', 'push', remote, '--delete', branch_name])
            logger.info(f"Deleted remote branch: {remote}/{branch_name}")
        except subprocess.CalledProcessError as e:
            logger.warning(f"Failed to delete remote branch {remote}/{branch_name}: {e}")
            success = False
        
        return success
    
    def execute_merge_workflow(self,
                             feature_branch: str,
                             target_branch: str = "main",
                             remote: str = "origin",
                             merge_message: Optional[str] = None,
                             cleanup_branch: bool = False) -> bool:
        """
        Execute the complete merge workflow:
        1. Switch to target branch (usually main)
        2. Pull latest changes from target branch
        3. Merge feature branch into target branch
        4. Push merged changes
        5. Optionally delete feature branch
        
        Args:
            feature_branch: Feature branch to merge
            target_branch: Target branch to merge into (default: main)
            remote: Remote repository name
            merge_message: Custom merge message
            cleanup_branch: Whether to delete feature branch after merge
            
        Returns:
            True if successful, False otherwise
        """
        logger.info(f"Starting merge workflow: {feature_branch} → {target_branch}")
        
        # Verify we're in a Git repository
        if not self.check_git_repo():
            return False
        
        # Store current branch for potential rollback
        original_branch = self.get_current_branch()
        
        try:
            # Verify feature branch exists
            if not self.branch_exists_local(feature_branch):
                logger.error(f"Feature branch {feature_branch} does not exist locally")
                return False
            
            # Switch to target branch
            if not self.switch_branch(target_branch):
                return False
            
            # Pull latest changes from target branch
            if not self.pull_latest(remote, target_branch):
                logger.error("Failed to pull latest changes from target branch")
                return False
            
            # Merge feature branch
            if not merge_message:
                merge_message = f"Merge branch '{feature_branch}' into {target_branch}"
            
            if not self.merge_branch(feature_branch, merge_message):
                logger.error("Merge failed - you may need to resolve conflicts manually")
                return False
            
            # Push merged changes
            if not self.push_changes(remote, target_branch):
                logger.error("Failed to push merged changes")
                return False
            
            # Cleanup feature branch if requested
            if cleanup_branch:
                logger.info(f"Cleaning up feature branch: {feature_branch}")
                self.delete_branch(feature_branch, remote)
            
            logger.info(f"Successfully completed merge workflow: {feature_branch} → {target_branch}")
            return True
            
        except Exception as e:
            logger.error(f"Merge workflow failed: {e}")
            logger.info(f"Attempting to return to original branch: {original_branch}")
            try:
                self.switch_branch(original_branch)
            except:
                logger.warning("Failed to return to original branch")
            return False


def main():
    """Main function to handle command line arguments and execute merge workflow"""
    parser = argparse.ArgumentParser(description="Automated Git Merge Bot")
    parser.add_argument('feature_branch', help='Feature branch to merge')
    parser.add_argument('--target', default='main', help='Target branch to merge into (default: main)')
    parser.add_argument('--remote', default='origin', help='Remote repository name (default: origin)')
    parser.add_argument('--message', help='Custom merge message')
    parser.add_argument('--cleanup', action='store_true', help='Delete feature branch after merge')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--repo-path', help='Repository path (default: current directory)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--force', action='store_true', help='Force merge without confirmation')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize Git Merge Bot
    bot = GitMergeBot(config_path=args.config)
    
    # Override repo path if provided
    if args.repo_path:
        bot.repo_path = args.repo_path
    
    # Confirmation prompt unless forced
    if not args.force:
        print(f"About to merge '{args.feature_branch}' into '{args.target}'")
        if args.cleanup:
            print(f"⚠️  This will also DELETE the '{args.feature_branch}' branch!")
        
        confirm = input("Continue? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Merge cancelled.")
            sys.exit(0)
    
    # Execute merge workflow
    success = bot.execute_merge_workflow(
        feature_branch=args.feature_branch,
        target_branch=args.target,
        remote=args.remote,
        merge_message=args.message,
        cleanup_branch=args.cleanup
    )
    
    if success:
        logger.info("Merge workflow completed successfully!")
        print(f"✅ Successfully merged '{args.feature_branch}' into '{args.target}'")
        if args.cleanup:
            print(f"🗑️  Cleaned up '{args.feature_branch}' branch")
        sys.exit(0)
    else:
        logger.error("Merge workflow failed!")
        print(f"❌ Failed to merge '{args.feature_branch}' into '{args.target}'")
        sys.exit(1)


if __name__ == "__main__":
    main()
