# 📁 Directory Guide - IMPORTANT!

## ⚠️ **CRITICAL: Where to Run the Scripts**

### ✅ **CORRECT - Run from Repository Root:**

```bash
# You should be here (repository root):
/c/Users/molak/MJ_Repos/LLM_Engineering_Projects

# Run scripts like this:
python github_activity_bot/git_push_bot.py "branch-name" "commit message"
python github_activity_bot/git_merge_bot.py "feature-branch"

# Or use shell scripts (they automatically go to repository root):
./github_activity_bot/run_git_bot.sh "branch-name" "commit message"
./github_activity_bot/run_git_merge.sh "feature-branch"
```

### ❌ **WRONG - Don't Run from Bot Directory:**

```bash
# DON'T be here (bot subdirectory):
/c/Users/molak/MJ_Repos/LLM_Engineering_Projects/github_activity_bot

# DON'T run like this:
python git_push_bot.py "branch-name" "commit message"  # ❌ WRONG!
```

## 🚨 **Why This Matters:**

### **When you run from the wrong directory:**
- ❌ The `github_activity_bot/` folder gets included in commits
- ❌ Git commands only see files in the current subdirectory  
- ❌ Exclusion logic can't work properly
- ❌ You may miss important files from other parts of your project

### **When you run from the correct directory:**
- ✅ The `github_activity_bot/` folder is automatically excluded
- ✅ Git commands can see all project files
- ✅ Exclusion logic works perfectly
- ✅ All project files are properly managed

## 🛡️ **Safety Features Added:**

### **1. Directory Warning**
The bot now warns you if you're running from the wrong directory:
```
⚠️  RUNNING FROM BOT DIRECTORY!
⚠️  For best results, run from repository root directory
⚠️  This may cause the bot folder to be included in commits
```

### **2. Improved Exclusion Logic**
- Multiple exclusion patterns for the bot directory
- Enhanced file filtering for specific file operations
- Better logging of what gets excluded

### **3. Shell Script Auto-Navigation**
The shell scripts now automatically:
- Navigate to the repository root
- Show you which directory they're using
- Run the Python scripts with the correct path

## 📖 **Quick Reference:**

### **Check Your Current Directory:**
```bash
pwd
# Should show: /c/Users/molak/MJ_Repos/LLM_Engineering_Projects
```

### **Navigate to Repository Root:**
```bash
cd /c/Users/molak/MJ_Repos/LLM_Engineering_Projects
```

### **Correct Usage Examples:**
```bash
# Push bot
python github_activity_bot/git_push_bot.py "feature/new-feature" "Added new functionality"

# Merge bot  
python github_activity_bot/git_merge_bot.py "feature/new-feature"

# Using shell scripts (recommended)
./github_activity_bot/run_git_bot.sh "feature/new-feature" "Added new functionality"
./github_activity_bot/run_git_merge.sh "feature/new-feature"
```

## 🔧 **Troubleshooting:**

### **Problem: Bot folder still getting committed**
**Solution:** Make sure you're running from repository root, not from `github_activity_bot/` folder

### **Problem: "Not a git repository" error**
**Solution:** Make sure you're in the correct repository directory with `.git` folder

### **Problem: Can't find the scripts**
**Solution:** Use the full path: `python github_activity_bot/git_push_bot.py` from repository root

---

**Remember:** Always run from the repository root (`LLM_Engineering_Projects`), never from the `github_activity_bot` subdirectory!
