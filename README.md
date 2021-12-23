## Level 2: Clean Up

### Introduction:
Welcome to level 2! There are a lot of useless files and commits on this branch, so lets clean things up. Below are some relevant linux/terminal commands you will need and git commands you may find useful for this task. Enjoy!  

### Useful Commands
   - cd 
   - ls
   - touch 
   - vim/nano

### Instructions:

1. There are 3 important words stored in 3 important files. Your goal is to find those files.
   - You must not leave the command line to do this, your main tool for exploration is `git checkout [branch_name]`. The file could be in any of three branches: `level2` (this one), `branch1` or `branch2`. It could also be in any commit within those branches. To switch to a specific commit you must also use `git checkout [commit_id]`. 
2. To actually clean things up, our job is now to get these 3 important files into our main `level2` branch. The first thing we must do is to make the HEADS of each branch point to the commit that added that important to that branch's history. Then, to get things into the `level2` branch, we must perform a merge. 
   - For instance, lets say you have a file named `important.txt` that stores one of the important words. Lets say this file is stored on `branch1`. `branch1` has 5 total commits and `important.txt` was added on the second commit. Our goal now is to make the HEAD of the `branch1` branch to point to that second commit, essentially ignoring the 3 after it. After we do this, we have to merge this branch into `level2` so that the file in `branch1` shows up in `level2`. 
   - Follow the instructions below to do this for all 3 files. At the end of these steps `level2` should have all 3 important files (and nothing else, so go ahead and delete all the other useless files as well). 

#### Reverting to a previous commit: 
1. Lets revert our project's state to those commits, in other words, lets move the HEAD to point to the commit that introduced that files you found in step 1 to the repo.
   - Now there are ways three ways to revert to previous commits:
     1. Temporary Switch
        - This involves using `git checkout [commit id]` to temporarily observe a previous state but not necessarily make changes. This is what you did above to explore and look around files. 
     2. Undo Recent Commits
        - If you create some changes and decide you don't want them anymore you can do `git revert [commit id]`
        - view [revert docs](https://git-scm.com/docs/git-revert) for more details
     3. Delete Commits Completely
        - if you do not care about your changes that have followed from the commit you want to go to, you can delete them completely by performing a `git reset --hard [commit id]`
        - this is not reversible so please use this with caution.
   - Which of the 3 do you think are most relevant for our purposes? Once you decide, perform that command.  
     - It may seem like number 3 is the way to go, but that is dangerous, in case you make a mistake, there is no going back. So what we will do instead is number 1 but with a slight modification. There are two steps to this process, one is to get to the commit you want to go, which happens when you do `git checkout [commit id]` and step two is to actually get the repo to this spot (to remove detached HEAD state) so instead of deleting everything with the `reset` command we will instead move this state onto a new branch with the current branch staying intact. So to do this we will run two commands: 1. `git checkout -b [name of new branch]` 2. `git push [your_name_gitworkshop] [name of new branch from previous command]`  
      - Now we have our original branch in case we need to go back but on our new branch can start any new updates we want to make with a state that starts with the commit we wanted to go back to. You may name the branches whatever you like.

#### Merging Branches 
1. Now, we have our branches each with the latest commit (the HEAD) pointing at the commits that introduced those important files to that branch. We must now unite these branches with our main one. To do so we must move to the branch we want to merge into, for us, this is `level2`. 
2. Now, type `git merge [branch_name]`, for us this will be either `branch1` or `branch2`. If you need to merge both, merge them independently, so run this command twice for each branch. 
3. Check `git log`, you should see commits from all branches on one page. 

### Evaluation
1. Now to make sure those changes took effect, push your changes to github (to your remote repo).
2. Now, delete all other useless files. Your `src` folder should only have 3 important files. In the real world, you would likely also delete the useless branches: `branch1`, `branch2`, `new_branch1`
3. Add, Commit, Push these changes. 
4. Now do `git log` from the `level2` branch, and you should be seeing something like this in your terminal:
5. Congrats! You just cleaned up a really messy repo and learned how to work within a branch and across branches. 
