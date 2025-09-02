# GitHub Activity Bot - Complete Git Automation Suite

A comprehensive automation solution for Git operations including push, merge, branch management, and workflow automation.

## 🚀 Features

### Git Push Bot (`git_push_bot.py`)
- **Automated Branch Management**: Creates branches if they don't exist
- **Smart Pull Updates**: Pulls latest changes before pushing to avoid conflicts
- **Intelligent File Exclusion**: Always excludes `github_activity_bot/` folder from commits
- **Flexible Configuration**: JSON-based configuration for different projects
- **Comprehensive Logging**: Detailed logs for debugging and monitoring
- **Error Handling**: Robust error handling with meaningful messages
- **Multiple Usage Patterns**: Command-line, programmatic, and interactive modes

### Git Merge Bot (`git_merge_bot.py`) - NEW!
- **Automated Branch Merging**: Merge feature branches into main/target branches
- **Safe Merge Workflow**: Pulls latest changes before merging to prevent conflicts
- **Branch Cleanup**: Optionally delete feature branches after successful merge
- **Merge Confirmation**: Interactive confirmation to prevent accidental merges
- **Custom Merge Messages**: Support for custom merge commit messages
- **Multiple Target Branches**: Merge into any target branch (main, develop, staging, etc.)

## 📁 Project Structure

```
github_activity_bot/
├── git_push_bot.py      # Main push automation script
├── git_merge_bot.py     # NEW! Branch merge automation script
├── config.json          # Configuration file template
├── example_usage.py     # Usage examples and demonstrations
├── run_git_bot.sh      # Convenient shell script for push operations
├── run_git_merge.sh    # NEW! Convenient shell script for merge operations
├── README.md           # This documentation
├── git_push_bot.log    # Push bot log file (created when script runs)
└── git_merge_bot.log   # Merge bot log file (created when script runs)
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.6 or higher
- Git installed and configured
- Git repository initialized in your project

### Quick Setup

1. **Clone or copy the files** to your project directory
2. **Configure Git** (if not already done):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
3. **Make the script executable** (optional):
   ```bash
   chmod +x git_push_bot.py
   ```

## 📖 Usage

### Git Push Bot Usage

#### Command Line Usage
```bash
# Basic push to feature branch
python git_push_bot.py "feature/new-feature" "Added new functionality"

# Advanced usage with options
python git_push_bot.py "hotfix/bug-fix" "Fixed critical bug" --remote origin --config config.json --verbose

# Using the convenient shell script
./run_git_bot.sh "feature/my-feature" "My commit message"
```

#### Push Bot Parameters
- `branch`: Target branch name (required)
- `message`: Commit message (required)
- `--remote`: Remote repository name (default: origin)
- `--config`: Path to configuration file
- `--files`: Specific files to stage (default: all files except github_activity_bot/)
- `--repo-path`: Repository path (default: current directory)
- `--verbose`: Enable verbose logging

### Git Merge Bot Usage - NEW!

#### Command Line Usage
```bash
# Basic merge: feature branch → main
python git_merge_bot.py "feature/new-feature"

# Merge with cleanup (deletes feature branch after merge)
python git_merge_bot.py "feature/completed-feature" --cleanup

# Merge to different target branch
python git_merge_bot.py "feature/my-feature" --target development

# Custom merge message
python git_merge_bot.py "hotfix/critical-fix" --message "Emergency hotfix for production issue"

# Force merge without confirmation
python git_merge_bot.py "feature/auto-deploy" --force --cleanup

# Using the convenient shell script
./run_git_merge.sh "feature/my-feature"
./run_git_merge.sh "feature/my-feature" --target development --cleanup
```

#### Merge Bot Parameters
- `feature_branch`: Feature branch to merge (required)
- `--target`: Target branch to merge into (default: main)
- `--remote`: Remote repository name (default: origin)
- `--message`: Custom merge message
- `--cleanup`: Delete feature branch after successful merge
- `--config`: Path to configuration file
- `--repo-path`: Repository path (default: current directory)
- `--verbose`: Enable verbose logging
- `--force`: Skip confirmation prompt

### Programmatic Usage

#### Push Bot Example
```python
from git_push_bot import GitPushBot

# Initialize the push bot
push_bot = GitPushBot(config_path="config.json")

# Execute push workflow
success = push_bot.execute_git_workflow(
    target_branch="feature/my-feature",
    commit_message="Added new feature",
    remote="origin"
)

if success:
    print("✅ Push successful!")
else:
    print("❌ Push failed!")
```

#### Merge Bot Example - NEW!
```python
from git_merge_bot import GitMergeBot

# Initialize the merge bot
merge_bot = GitMergeBot(config_path="config.json")

# Execute merge workflow
success = merge_bot.execute_merge_workflow(
    feature_branch="feature/my-feature",
    target_branch="main",
    merge_message="Merged feature/my-feature into main",
    cleanup_branch=True  # Delete feature branch after merge
)

if success:
    print("✅ Merge successful!")
else:
    print("❌ Merge failed!")
```

### Configuration File

Create a `config.json` file to customize behavior:

```json
{
    "repo_path": "/path/to/your/repo",
    "default_branch": "main",
    "default_remote": "origin",
    "auto_stage_all": true,
    "create_branch_if_missing": true,
    "pull_before_push": true,
    "excluded_files": [
        "*.log",
        "__pycache__/*",
        "*.pyc",
        ".env"
    ]
}
```

## 🔧 Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `repo_path` | string | current directory | Path to Git repository |
| `default_branch` | string | "main" | Default branch name |
| `default_remote` | string | "origin" | Default remote repository |
| `auto_stage_all` | boolean | true | Stage all files automatically |
| `create_branch_if_missing` | boolean | true | Create branch if it doesn't exist |
| `pull_before_push` | boolean | true | Pull latest changes before pushing |
| `excluded_files` | array | [] | Files to exclude from staging |

## 🔄 Workflow Processes

### Push Bot Workflow

The push bot follows this automated workflow:

1. **Repository Validation**: Verify current directory is a Git repository
2. **Branch Handling**: 
   - Check if target branch exists locally
   - Create branch if missing (when enabled)
   - Switch to target branch
3. **Update Local Branch**: Pull latest changes from remote (when enabled and branch exists)
4. **Stage Changes**: Add files to staging area (excluding github_activity_bot/ folder)
5. **Commit Changes**: Create commit with provided message
6. **Push Changes**: Push to remote repository with upstream setting for new branches

### Merge Bot Workflow - NEW!

The merge bot follows this automated workflow:

1. **Repository Validation**: Verify current directory is a Git repository
2. **Branch Validation**: Verify feature branch exists locally
3. **Switch to Target**: Switch to target branch (usually main)
4. **Update Target Branch**: Pull latest changes from remote target branch
5. **Merge Process**: Merge feature branch into target branch
6. **Push Merged Changes**: Push merged changes to remote repository
7. **Branch Cleanup** (optional): Delete feature branch locally and remotely

## 📝 Examples

### Push Bot Examples

#### Example 1: Basic Push to Feature Branch
```bash
python git_push_bot.py "feature/user-authentication" "Implemented user login system"
```

#### Example 2: Hotfix with Specific Files
```bash
python git_push_bot.py "hotfix/security-patch" "Fixed security vulnerability" --files "auth.py" "utils.py"
```

#### Example 3: Push to Different Remote
```bash
python git_push_bot.py "development" "Weekly development update" --remote upstream
```

#### Example 4: Using Configuration File
```bash
python git_push_bot.py "feature/new-ui" "Updated user interface" --config my-project-config.json
```

### Merge Bot Examples - NEW!

#### Example 5: Basic Feature Merge
```bash
python git_merge_bot.py "feature/user-authentication"
```

#### Example 6: Merge with Branch Cleanup
```bash
python git_merge_bot.py "feature/completed-feature" --cleanup
```

#### Example 7: Emergency Hotfix Merge
```bash
python git_merge_bot.py "hotfix/critical-security-fix" --force --message "Emergency security patch"
```

#### Example 8: Merge to Development Branch
```bash
python git_merge_bot.py "feature/new-api" --target development --cleanup
```

### Complete Development Workflow Example

```bash
# 1. Create and work on a feature branch
python git_push_bot.py "feature/new-dashboard" "Added user dashboard functionality"

# 2. Continue development with more commits
python git_push_bot.py "feature/new-dashboard" "Fixed dashboard styling issues"
python git_push_bot.py "feature/new-dashboard" "Added dashboard tests"

# 3. Merge the completed feature to main and cleanup
python git_merge_bot.py "feature/new-dashboard" --cleanup

# Result: Feature is now in main branch, feature branch is deleted
```

## 🚨 Error Handling

The script includes comprehensive error handling for common scenarios:

- **Invalid Git Repository**: Checks if current directory is a Git repo
- **Network Issues**: Handles network connectivity problems
- **Merge Conflicts**: Provides clear error messages for conflict resolution
- **Permission Issues**: Reports authentication and permission errors
- **Branch Conflicts**: Handles existing branch and naming conflicts

## 📊 Logging

Logs are automatically generated in `git_push_bot.log` with different levels:

- **INFO**: General workflow information
- **DEBUG**: Detailed command execution (with --verbose)
- **WARNING**: Non-critical issues
- **ERROR**: Critical errors that prevent completion

## 🔐 Security Considerations

- **Credentials**: Never store passwords or tokens in configuration files
- **SSH Keys**: Use SSH keys for authentication instead of passwords
- **File Exclusions**: Configure excluded_files to prevent sensitive data commits
- **Repository Access**: Ensure proper repository permissions are set

## 🛠️ Troubleshooting

### Common Issues

**1. "Not a git repository" Error**
```bash
# Initialize Git repository
git init
git remote add origin https://github.com/username/repo.git
```

**2. "Permission denied" Error**
```bash
# Check SSH key configuration
ssh -T git@github.com

# Or use HTTPS with token
git remote set-url origin https://token@github.com/username/repo.git
```

**3. "Branch already exists" Error**
- The script automatically handles this by switching to existing branches
- Check logs for detailed information

**4. "Nothing to commit" Message**
- No changes detected in repository
- Add or modify files before running the script

### Debug Mode

Enable verbose logging for detailed troubleshooting:
```bash
python git_push_bot.py "branch-name" "commit message" --verbose
```

## 🔄 Integration Examples

### GitHub Actions Integration
```yaml
name: Auto Push
on: [push]
jobs:
  auto-push:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run Git Push Bot
      run: python git_push_bot.py "automated-updates" "Automated commit from CI"
```

### Cron Job Integration
```bash
# Add to crontab for daily backups
0 2 * * * cd /path/to/repo && python git_push_bot.py "daily-backup" "Daily automated backup"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to modify and distribute according to your needs.

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review log files for detailed error messages
3. Ensure Git and Python are properly configured
4. Verify repository permissions and network connectivity

---

**Created by GitHub Activity Bot** - Automating Git workflows for better productivity!
