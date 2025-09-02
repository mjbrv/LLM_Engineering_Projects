#!/bin/bash
# GitHub Activity Bot - Quick Run Script
# This script provides easy access to the Git Push Bot functionality

# Activate virtual environment (as per workspace rules)
source C:/Users/molak/.virtualenvs/mj_bots_env/Scripts/activate

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}GitHub Activity Bot - Quick Run Script${NC}"
echo "========================================"

# Function to show usage
show_usage() {
    echo -e "${YELLOW}Usage:${NC}"
    echo "  $0 <branch_name> <commit_message> [options]"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo "  $0 \"feature/new-bot\" \"Added new bot functionality\""
    echo "  $0 \"hotfix/bug-fix\" \"Fixed critical bug\" --verbose"
    echo "  $0 \"development\" \"Weekly update\" --config config.json"
    echo ""
    echo -e "${YELLOW}Options:${NC}"
    echo "  --remote <name>     Remote repository name (default: origin)"
    echo "  --config <path>     Configuration file path"
    echo "  --files <files>     Specific files to stage (space-separated)"
    echo "  --verbose           Enable verbose logging"
    echo "  --help             Show this help message"
}

# Function to check if git is available
check_git() {
    if ! command -v git &> /dev/null; then
        echo -e "${RED}Error: Git is not installed or not in PATH${NC}"
        exit 1
    fi
}

# Function to check if we're in a git repository
check_git_repo() {
    if ! git rev-parse --git-dir &> /dev/null; then
        echo -e "${RED}Error: Current directory is not a Git repository${NC}"
        echo -e "${YELLOW}Tip: Run 'git init' to initialize a repository${NC}"
        exit 1
    fi
}

# Function to run the Git Push Bot
run_git_bot() {
    local branch_name="$1"
    local commit_message="$2"
    shift 2
    local additional_args="$@"
    
    echo -e "${BLUE}Running Git Push Bot...${NC}"
    echo -e "${YELLOW}Branch:${NC} $branch_name"
    echo -e "${YELLOW}Message:${NC} $commit_message"
    echo ""
    
    # Change to repository root (not script directory) to run the bot
    REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
    echo -e "${BLUE}Repository root: $REPO_ROOT${NC}"
    cd "$REPO_ROOT"
    python github_activity_bot/git_push_bot.py "$branch_name" "$commit_message" $additional_args
    
    local exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✅ Git Push Bot completed successfully!${NC}"
    else
        echo ""
        echo -e "${RED}❌ Git Push Bot failed with exit code: $exit_code${NC}"
        echo -e "${YELLOW}💡 Check git_push_bot.log for detailed error information${NC}"
    fi
    
    return $exit_code
}

# Function to show interactive mode
interactive_mode() {
    echo -e "${BLUE}Interactive Mode${NC}"
    echo "==============="
    
    # Get branch name
    read -p "Enter target branch name: " branch_name
    if [ -z "$branch_name" ]; then
        echo -e "${RED}Branch name cannot be empty${NC}"
        exit 1
    fi
    
    # Get commit message
    read -p "Enter commit message: " commit_message
    if [ -z "$commit_message" ]; then
        echo -e "${RED}Commit message cannot be empty${NC}"
        exit 1
    fi
    
    # Get optional remote
    read -p "Enter remote name (default: origin): " remote_name
    if [ -z "$remote_name" ]; then
        remote_name="origin"
    fi
    
    # Ask for verbose mode
    read -p "Enable verbose logging? (y/N): " verbose_choice
    verbose_args=""
    if [[ $verbose_choice =~ ^[Yy]$ ]]; then
        verbose_args="--verbose"
    fi
    
    echo ""
    echo -e "${YELLOW}Configuration Summary:${NC}"
    echo "Branch: $branch_name"
    echo "Message: $commit_message"
    echo "Remote: $remote_name"
    echo "Verbose: $([ -n "$verbose_args" ] && echo "Yes" || echo "No")"
    echo ""
    
    read -p "Proceed with these settings? (Y/n): " confirm
    if [[ $confirm =~ ^[Nn]$ ]]; then
        echo -e "${YELLOW}Operation cancelled${NC}"
        exit 0
    fi
    
    run_git_bot "$branch_name" "$commit_message" --remote "$remote_name" $verbose_args
}

# Function to show examples
show_examples() {
    echo -e "${BLUE}Common Usage Examples${NC}"
    echo "====================="
    echo ""
    echo -e "${YELLOW}1. Basic feature branch push:${NC}"
    echo "   $0 \"feature/user-auth\" \"Implemented user authentication\""
    echo ""
    echo -e "${YELLOW}2. Hotfix with verbose logging:${NC}"
    echo "   $0 \"hotfix/security-fix\" \"Fixed security vulnerability\" --verbose"
    echo ""
    echo -e "${YELLOW}3. Push specific files only:${NC}"
    echo "   $0 \"development\" \"Updated core modules\" --files \"*.py\" \"requirements.txt\""
    echo ""
    echo -e "${YELLOW}4. Using custom configuration:${NC}"
    echo "   $0 \"release/v1.0\" \"Release version 1.0\" --config production-config.json"
    echo ""
    echo -e "${YELLOW}5. Push to different remote:${NC}"
    echo "   $0 \"main\" \"Sync with upstream\" --remote upstream"
}

# Main script logic
main() {
    # Check prerequisites
    check_git
    check_git_repo
    
    # Handle command line arguments
    case "${1:-}" in
        --help|-h)
            show_usage
            exit 0
            ;;
        --examples|-e)
            show_examples
            exit 0
            ;;
        --interactive|-i)
            interactive_mode
            exit $?
            ;;
        "")
            echo -e "${RED}Error: Missing required arguments${NC}"
            echo ""
            show_usage
            exit 1
            ;;
        *)
            if [ $# -lt 2 ]; then
                echo -e "${RED}Error: Both branch name and commit message are required${NC}"
                echo ""
                show_usage
                exit 1
            fi
            
            run_git_bot "$@"
            exit $?
            ;;
    esac
}

# Run main function with all arguments
main "$@"
