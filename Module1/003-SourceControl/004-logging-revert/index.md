# Tutorial
Go through the following commands

git log
git log <branch>
git log --oneline
git log --branches=*
git log --all --decorate --oneline --graph

Talk about reverting compared to reset

git revert <commit id> - new commit to revert back to this commit
git revert HEAD        - new commit reverts back to previous commit
git reset -- hard <commit id> - reverts back to this commit and discards history after this point

# Exercise
Create a new commit on dev with a new file (wrongFile.txt), revert back to the commit before this commit before pushing to gitlab