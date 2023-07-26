---
title: Git and Github useful commands
date: 2017-05-28 11:15:20
categories: [Git, Github, DevOps, Odoo]
tags: [Git, Github, DevOps, Odoo]
---
Git is a distributed version control system (DVCS) that is used to track changes in computer files. It is often used for coordinating work among programmers collaboratively developing source code during software development.

## Git cheat sheet

|Git Command | Usage |
| ------------ | ------------- | 
|`git init` | initialize an existing directory as a Git repository |
|`git clone ` | retrieve an entire repository from a hosted location via URL |
|`git status` | show modified files in working directory, staged for your next commit |
|`git add [. or file]` | add a file as it looks now to your next commit (stage) |
|`git diff` | diff of what is changed but not staged |
|`git commit -m` | commit your staged content as a new commit snapshot |
|`git branch` | list your branches. a * will appear next to the currently active branch |
|`git branch [branch-name]` | create a new branch at the current commit |
|`git checkout` | switch to another branch and check it out into your working directory |
|`git merge [branch]` | switch to another branch and check it out into your working directory |
|`git log` | show all commits in the current branch’s history
|`git log branchB..branchA` | show the commits on branchA that are not on branchB |
|`git push ` | Transmit local branch commits to the remote repository branch
|`git pull ` | fetch and merge any commits from the tracking remote branch |
|`git fetch  ` | fetch down all the branches from that Git remote
|`git reset --hard [commit]` | clear staging area, rewrite working tree from specified commit |
|`git stash` | Save modified and staged changes |

## Git clone branch
```sh
git clone --depth 1 --branch 16.0 git@github.com:odoo/odoo.git
```
## Git configuration
Git Config
```sh
git config --global user.name "Mohamed Elbagoury" 
git config --global user.email "info@bagoury.com"
git remote add origin git@gitlab.com:Elbagoury/odoo.git
git push --set-upstream google staging
```
Generate SSH key
```sh
ssh-keygen -t rsa -C "info@bagoury.com"
cat  ~/.ssh/id_rsa.pub
```
Generate gpg key for github
```sh
gpg --full-generate-key
gpg --armor --output mypublic.key --export 'info@bagoury.com' # then copy to github
git config --global --unset gpg.format
git config --global user.signingkey # take after sec 3AA5C34371567BD2
export GPG_TTY=$(tty)
echo "test" | gpg --clearsign
git config --global commit.gpgsign true
```
Remember git passphrase in WSL
```sh
cp -r /mnt/c/Users/<username>/.ssh ~/.ssh
sudo apt install keychain
# inside ~/.bashrc add 
eval `keychain --quiet --eval --agents ssh id_rsa`
```