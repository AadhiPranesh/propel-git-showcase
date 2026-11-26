A. Setup & Repository Connection
git config --global user.name / user.email — Set your author identity once on your machine.

git init — Initialize a brand-new local repository from scratch.

git clone <ssh-url> — Download an existing remote repository from GitHub onto your laptop.

git remote -v — Inspect connected remote repository URLs (fetch and push).

git remote add origin <ssh-url> — Link a local repository to an empty remote repository on GitHub.

git remote set-url origin <ssh-url> — Switch an existing remote repository connection from HTTPS to SSH.

B. Daily Staging, Inspection & Micro-Commits
git status — Check modified, staged, and untracked files in your working directory.

git diff — View line-by-line unstaged changes before adding them.

git diff --staged — View line-by-line staged changes ready to be committed.

git add <file> — Stage a specific file for the next commit.

git add -p <file> — Interactively stage individual code chunks ("hunks") to split unrelated edits into separate micro-commits.

git commit -m "title" -m "body" — Create an atomic commit with a Conventional Commits title and a detailed description.

git log --oneline --graph --all — View a compact visual commit tree and branch history.

C. Branching & Merging
git branch — List all local branches and see which branch is currently active (*).

git checkout -b <branch-name> — Create a new branch and switch to it immediately.

git switch <branch-name> — Switch between existing branches cleanly.

git merge <branch-name> — Combine changes from a feature branch into your active branch (and resolve conflicts when overlapping lines change).

git branch -d <branch-name> — Delete a local branch after it has been merged.

D. Syncing with GitHub (Remote)
git fetch origin — Download remote updates safely into your local cache without modifying your working files.

git pull origin <branch> — Download remote updates and merge them immediately into your active branch (fetch + merge).

git push -u origin <branch> — Push local commits to GitHub and set upstream tracking for future pushes.

git push — Push new commits to the linked remote branch over SSH.

E. Undoing Mistakes & Temporary Storage
git commit --amend -m "new message" — Fix the last commit message or include forgotten staged files before pushing.

git restore <file> — Discard uncommitted local edits in a file and revert it to the last commit.

git restore --staged <file> — Unstage a file without losing your local code changes.

git stash / git stash pop — Temporarily shelve uncommitted work so you can switch branches cleanly, then restore it later.

git revert <commit-hash> — Create a new commit that safely undoes a previously pushed commit without rewriting shared history.

git reset --soft HEAD~1 / --hard HEAD~1 — Undo unpushed local commits (either keeping edits staged with --soft or discarding them with --hard).
