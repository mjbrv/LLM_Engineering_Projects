# GitHub Activity Bot - Automated Git Push Tool

A comprehensive Python script for automating Git operations including branch creation, pulling updates, and pushing code changes to specified repositories and branches.

## 🚀 Features

- **Automated Branch Management**: Creates branches if they don't exist
- **Smart Pull Updates**: Pulls latest changes before pushing to avoid conflicts
- **Flexible Configuration**: JSON-based configuration for different projects
- **Comprehensive Logging**: Detailed logs for debugging and monitoring
- **Error Handling**: Robust error handling with meaningful messages
- **Multiple Usage Patterns**: Command-line, programmatic, and interactive modes

## 📁 Project Structure

```
github_activity_bot/
├── git_push_bot.py      # Main automation script
├── config.json          # Configuration file template
├── example_usage.py     # Usage examples and demonstrations
├── README.md           # This documentation
└── git_push_bot.log    # Log file (created when script runs)
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

### Command Line Usage

#### Basic Usage
```bash
python git_push_bot.py "feature/new-feature" "Added new functionality"
```

#### Advanced Usage
```bash
python git_push_bot.py "hotfix/bug-fix" "Fixed critical bug" --remote origin --config config.json --verbose
```

#### Parameters
- `branch`: Target branch name (required)
- `message`: Commit message (required)
- `--remote`: Remote repository name (default: origin)
- `--config`: Path to configuration file
- `--files`: Specific files to stage (default: all files)
- `--repo-path`: Repository path (default: current directory)
- `--verbose`: Enable verbose logging

### Programmatic Usage

```python
from git_push_bot import GitPushBot

# Initialize the bot
bot = GitPushBot(config_path="config.json")

# Execute Git workflow
success = bot.execute_git_workflow(
    target_branch="feature/my-feature",
    commit_message="Added new feature",
    remote="origin"
)

if success:
    print("✅ Push successful!")
else:
    print("❌ Push failed!")
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

## 🔄 Workflow Process

The script follows this automated workflow:

1. **Repository Validation**: Verify current directory is a Git repository
2. **Branch Handling**: 
   - Check if target branch exists locally
   - Create branch if missing (when enabled)
   - Switch to target branch
3. **Update Local Branch**: Pull latest changes from remote (when enabled)
4. **Stage Changes**: Add files to staging area
5. **Commit Changes**: Create commit with provided message
6. **Push Changes**: Push to remote repository with upstream setting for new branches

## 📝 Examples

### Example 1: Basic Push to Feature Branch
```bash
python git_push_bot.py "feature/user-authentication" "Implemented user login system"
```

### Example 2: Hotfix with Specific Files
```bash
python git_push_bot.py "hotfix/security-patch" "Fixed security vulnerability" --files "auth.py" "utils.py"
```

### Example 3: Push to Different Remote
```bash
python git_push_bot.py "development" "Weekly development update" --remote upstream
```

### Example 4: Using Configuration File
```bash
python git_push_bot.py "feature/new-ui" "Updated user interface" --config my-project-config.json
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
