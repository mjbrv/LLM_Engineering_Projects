#!/bin/bash

# GitHub Merge Bot - Convenient Shell Script
# Handles merging feature branches into main branch

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to display help
show_help() {
    echo -e "${BLUE}GitHub Merge Bot - Feature Branch Merger${NC}"
    echo ""
    echo "Usage: $0 [OPTIONS] <feature_branch>"
    echo ""
    echo "Options:"
    echo "  -t, --target BRANCH     Target branch to merge into (default: main)"
    echo "  -m, --message MESSAGE   Custom merge message"
    echo "  -c, --cleanup           Delete feature branch after successful merge"
    echo "  -f, --force             Skip confirmation prompt"
    echo "  -v, --verbose           Enable verbose logging"
    echo "  -h, --help              Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 feature/new-functionality"
    echo "  $0 feature/bug-fix --target development --cleanup"
    echo "  $0 hotfix/critical-fix --force --message 'Emergency hotfix'"
    echo ""
    echo "Interactive mode:"
    echo "  $0 --interactive"
}

# Function for interactive mode
interactive_mode() {
    echo -e "${BLUE}=== Interactive Merge Mode ===${NC}"
    echo ""
    
    # Get feature branch
    read -p "Enter feature branch name: " feature_branch
    if [[ -z "$feature_branch" ]]; then
        echo -e "${RED}Error: Feature branch name is required${NC}"
        exit 1
    fi
    
    # Get target branch
    read -p "Enter target branch (default: main): " target_branch
    target_branch=${target_branch:-main}
    
    # Get merge message
    read -p "Enter custom merge message (optional): " merge_message
    
    # Ask about cleanup
    read -p "Delete feature branch after merge? (y/N): " cleanup_choice
    cleanup_flag=""
    if [[ "$cleanup_choice" =~ ^[Yy]$ ]]; then
        cleanup_flag="--cleanup"
    fi
    
    # Build command
    cmd_args="$feature_branch --target $target_branch"
    if [[ -n "$merge_message" ]]; then
        cmd_args="$cmd_args --message \"$merge_message\""
    fi
    if [[ -n "$cleanup_flag" ]]; then
        cmd_args="$cmd_args $cleanup_flag"
    fi
    
    echo ""
    echo -e "${YELLOW}Executing: python git_merge_bot.py $cmd_args${NC}"
    echo ""
    
    # Execute the command
    cd "$REPO_ROOT"
    eval "python github_activity_bot/git_merge_bot.py $cmd_args"
}

# Default values
TARGET_BRANCH="main"
MERGE_MESSAGE=""
CLEANUP_FLAG=""
FORCE_FLAG=""
VERBOSE_FLAG=""
INTERACTIVE_MODE=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--target)
            TARGET_BRANCH="$2"
            shift 2
            ;;
        -m|--message)
            MERGE_MESSAGE="$2"
            shift 2
            ;;
        -c|--cleanup)
            CLEANUP_FLAG="--cleanup"
            shift
            ;;
        -f|--force)
            FORCE_FLAG="--force"
            shift
            ;;
        -v|--verbose)
            VERBOSE_FLAG="--verbose"
            shift
            ;;
        -i|--interactive)
            INTERACTIVE_MODE=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}Unknown option: $1${NC}"
            show_help
            exit 1
            ;;
        *)
            if [[ -z "$FEATURE_BRANCH" ]]; then
                FEATURE_BRANCH="$1"
            else
                echo -e "${RED}Multiple feature branches specified. Use only one.${NC}"
                exit 1
            fi
            shift
            ;;
    esac
done

# Handle interactive mode
if [[ "$INTERACTIVE_MODE" == true ]]; then
    interactive_mode
    exit $?
fi

# Check if feature branch is provided
if [[ -z "$FEATURE_BRANCH" ]]; then
    echo -e "${RED}Error: Feature branch name is required${NC}"
    echo ""
    show_help
    exit 1
fi

# Build command arguments
CMD_ARGS="$FEATURE_BRANCH --target $TARGET_BRANCH"

if [[ -n "$MERGE_MESSAGE" ]]; then
    CMD_ARGS="$CMD_ARGS --message \"$MERGE_MESSAGE\""
fi

if [[ -n "$CLEANUP_FLAG" ]]; then
    CMD_ARGS="$CMD_ARGS $CLEANUP_FLAG"
fi

if [[ -n "$FORCE_FLAG" ]]; then
    CMD_ARGS="$CMD_ARGS $FORCE_FLAG"
fi

if [[ -n "$VERBOSE_FLAG" ]]; then
    CMD_ARGS="$CMD_ARGS $VERBOSE_FLAG"
fi

# Display what we're about to do
echo -e "${BLUE}=== GitHub Merge Bot ===${NC}"
echo -e "Feature Branch: ${GREEN}$FEATURE_BRANCH${NC}"
echo -e "Target Branch:  ${GREEN}$TARGET_BRANCH${NC}"
if [[ -n "$MERGE_MESSAGE" ]]; then
    echo -e "Merge Message:  ${GREEN}$MERGE_MESSAGE${NC}"
fi
if [[ -n "$CLEANUP_FLAG" ]]; then
    echo -e "Cleanup:        ${YELLOW}Yes - will delete feature branch${NC}"
fi
echo ""

# Change to repository root and execute
echo -e "${BLUE}Changing to repository root: $REPO_ROOT${NC}"
cd "$REPO_ROOT"

echo -e "${BLUE}Executing merge bot...${NC}"
eval "python github_activity_bot/git_merge_bot.py $CMD_ARGS"

# Capture exit code
EXIT_CODE=$?

if [[ $EXIT_CODE -eq 0 ]]; then
    echo ""
    echo -e "${GREEN}✅ Merge completed successfully!${NC}"
else
    echo ""
    echo -e "${RED}❌ Merge failed. Check the logs for details.${NC}"
fi

exit $EXIT_CODE
