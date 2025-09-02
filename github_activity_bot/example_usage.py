#!/usr/bin/env python3
"""
Example usage scripts for GitHub Activity Bot
Demonstrates different ways to use the Git Push Bot for automation.

Author: GitHub Activity Bot
Created: 2024
"""

import os
import sys
from pathlib import Path

# Add the current directory to the path to import git_push_bot
sys.path.append(str(Path(__file__).parent))

from git_push_bot import GitPushBot


def example_basic_usage():
    """Basic example: Push to a specific branch with auto-creation"""
    print("=== Basic Usage Example ===")
    
    # Initialize the bot
    bot = GitPushBot()
    
    # Execute workflow
    success = bot.execute_git_workflow(
        target_branch="feature/new-bot-updates",
        commit_message="Added new bot functionality and improvements",
        remote="origin"
    )
    
    if success:
        print("✅ Successfully pushed to feature/new-bot-updates")
    else:
        print("❌ Failed to push changes")


def example_with_config():
    """Example using a configuration file"""
    print("=== Configuration File Example ===")
    
    # Initialize with config file
    config_path = "config.json"
    bot = GitPushBot(config_path=config_path)
    
    # Push to development branch
    success = bot.execute_git_workflow(
        target_branch="development",
        commit_message="Automated update from bot development",
        remote="origin"
    )
    
    if success:
        print("✅ Successfully pushed to development branch")
    else:
        print("❌ Failed to push changes")


def example_specific_files():
    """Example: Stage and push only specific files"""
    print("=== Specific Files Example ===")
    
    bot = GitPushBot()
    
    # Only push specific Python files
    files_to_push = [
        "ig_bots/instagram_deleter.py",
        "braive_bot/braive_bot.py",
        "requirements.txt"
    ]
    
    success = bot.execute_git_workflow(
        target_branch="bot-updates",
        commit_message="Updated bot scripts and dependencies",
        files_to_stage=files_to_push
    )
    
    if success:
        print("✅ Successfully pushed specific files")
    else:
        print("❌ Failed to push specific files")


def example_hotfix_workflow():
    """Example: Hotfix workflow - create branch, push, and notify"""
    print("=== Hotfix Workflow Example ===")
    
    bot = GitPushBot()
    
    # Create a hotfix branch and push critical fixes
    hotfix_branch = "hotfix/critical-bug-fix"
    
    success = bot.execute_git_workflow(
        target_branch=hotfix_branch,
        commit_message="HOTFIX: Fixed critical bug in Instagram bot authentication",
        remote="origin"
    )
    
    if success:
        print(f"✅ Hotfix successfully pushed to {hotfix_branch}")
        print("🔔 Consider creating a pull request for code review")
    else:
        print("❌ Hotfix push failed")


def example_multiple_repos():
    """Example: Push to multiple repositories"""
    print("=== Multiple Repositories Example ===")
    
    # List of repositories to update
    repos = [
        {"path": ".", "branch": "main", "message": "Updated main project"},
        {"path": "../backup-repo", "branch": "backup", "message": "Backup sync"}
    ]
    
    for repo_config in repos:
        if os.path.exists(repo_config["path"]):
            print(f"Processing repository: {repo_config['path']}")
            
            bot = GitPushBot()
            bot.repo_path = repo_config["path"]
            
            success = bot.execute_git_workflow(
                target_branch=repo_config["branch"],
                commit_message=repo_config["message"]
            )
            
            if success:
                print(f"✅ Successfully updated {repo_config['path']}")
            else:
                print(f"❌ Failed to update {repo_config['path']}")
        else:
            print(f"⚠️  Repository path not found: {repo_config['path']}")


def example_scheduled_backup():
    """Example: Automated backup workflow"""
    print("=== Scheduled Backup Example ===")
    
    from datetime import datetime
    
    bot = GitPushBot()
    
    # Create timestamp for backup branch
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_branch = f"backup/auto_{timestamp}"
    
    success = bot.execute_git_workflow(
        target_branch=backup_branch,
        commit_message=f"Automated backup - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        remote="origin"
    )
    
    if success:
        print(f"✅ Backup created successfully: {backup_branch}")
    else:
        print("❌ Backup creation failed")


def example_error_handling():
    """Example: Comprehensive error handling"""
    print("=== Error Handling Example ===")
    
    bot = GitPushBot()
    
    try:
        # Attempt to push to a branch with potential conflicts
        success = bot.execute_git_workflow(
            target_branch="experimental/test-branch",
            commit_message="Testing error handling and recovery"
        )
        
        if success:
            print("✅ Push completed successfully")
        else:
            print("❌ Push failed - check logs for details")
            
            # Additional error recovery steps could go here
            print("🔧 Consider manual intervention or alternative strategies")
            
    except Exception as e:
        print(f"💥 Unexpected error occurred: {e}")
        print("📋 Check git_push_bot.log for detailed error information")


def interactive_example():
    """Interactive example: Get user input for branch and message"""
    print("=== Interactive Example ===")
    
    try:
        # Get user input
        branch_name = input("Enter target branch name: ").strip()
        if not branch_name:
            branch_name = "feature/interactive-update"
        
        commit_message = input("Enter commit message: ").strip()
        if not commit_message:
            commit_message = "Interactive commit via Git Push Bot"
        
        # Initialize bot and execute
        bot = GitPushBot()
        
        print(f"\n🚀 Pushing to branch: {branch_name}")
        print(f"📝 Commit message: {commit_message}")
        
        success = bot.execute_git_workflow(
            target_branch=branch_name,
            commit_message=commit_message
        )
        
        if success:
            print("✅ Interactive push completed successfully!")
        else:
            print("❌ Interactive push failed!")
            
    except KeyboardInterrupt:
        print("\n🛑 Operation cancelled by user")
    except Exception as e:
        print(f"💥 Error in interactive mode: {e}")


def main():
    """Run example demonstrations"""
    print("GitHub Activity Bot - Example Usage Demonstrations")
    print("=" * 50)
    
    examples = [
        ("1", "Basic Usage", example_basic_usage),
        ("2", "With Configuration", example_with_config),
        ("3", "Specific Files Only", example_specific_files),
        ("4", "Hotfix Workflow", example_hotfix_workflow),
        ("5", "Multiple Repositories", example_multiple_repos),
        ("6", "Scheduled Backup", example_scheduled_backup),
        ("7", "Error Handling", example_error_handling),
        ("8", "Interactive Mode", interactive_example),
    ]
    
    print("\nAvailable examples:")
    for num, title, _ in examples:
        print(f"  {num}. {title}")
    
    print("\nTo run a specific example, modify this script or call the function directly.")
    print("For production use, consider running examples one at a time.\n")
    
    # Uncomment the line below to run a specific example
    # example_basic_usage()


if __name__ == "__main__":
    main()
