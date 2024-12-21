# Development Team Process
Repeat the follwoing steps for each change made to this repository:
1. Checkout `main` branch with command `git checkout main`.
2. Fetch latest changes with command `git pull origin main`.
3. Create a new branch with command `git checkout -b <branch-name>` // this command checks out automatically to new branch/
4. Make any changes/development/improvements locally.
5. Test functionality locally.
6. Add your changes to Staging area for commit with command `git add <file-name[s]>` to add specific file or `git add .` to add all files at once.
7. Create a commit with command `git commit -m <message>`. 
8. Set up upstream once only for each new branch with command `git push --set-upstream origin <branch-name>`.
9. Now go to github.com and create a PR/MR (Pull Request / Merge Request) and add other team members as reviewers.
10. Once reviewed by at least two team members then merge the branch into main branch.


# Commit Messages:
It should be like `type: single line sentence for changes made`
Here are some examples of types:
* `fix` example: "fix: resolved xyz issue"
* `add` example: "add: xyz feature added"
* `chore` example: "chore: add xyz type of files in .gitignore"
* `refactor` example: "refactor: xyz function or xyz class or xyz file or xyz methodology etc."
