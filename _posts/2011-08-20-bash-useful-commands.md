---
title: Bash useful commands
date: 2011-08-20 12:15:20
categories: [Linux, DevOps, Odoo]
tags: [Linux, DevOps, Odoo]
---

Bash, or the Bourne-Again Shell, is a command-line interpreter and shell scripting language. It is the default shell for most Linux distributions and macOS. Bash is a powerful tool that can be used to automate tasks, manage files and directories, and interact with the operating system.

# Bash Basic

| Command               | Usage        |
|:------------          |:-------------|
|`sudo su - <any user>` | Change user |
|`ls / ls  -l ` | Show all files & directories |
|`pwd` | Show current  directory |
|`cd` | Change directory: `cd /opt`  to go up `cd..` |
|`mv` | Move files and directories `mv *.zip ../zip` |
|`mkdir` | Create directory |
|`find` | to find anything `find . -name "*.py"` |

Zip my modules all at once

```sh
for i in *
 do
    zip "$i.zip" -r "$i"
 done
 # unzip module.zip
```
Search in all the code and get modules then move it

```sh
find odoo -type f -name "__manifest__.py" -exec dirname {} \; |  xargs -I % mv % code-lib
```
Remove all pyc
```sh
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```
Move all the directories in the list
```sh
 while IFS= read -r dir; do mv -vt newdir/ "$dir"; done < dirlist.txt
```
Find a word inside all files and replace it
```sh
find ./ -type f -exec sed -i 's/mod/web/g' {} \;
```
find a word inside file name and replace it
```sh
find . -type f -name '*mod*' -exec  bash -c ' mv $0 ${0/\mod/web}' {} \;
find . -name 'odoo*' -exec bash -c 'mv "$1" "${1/odoo/modeem}"' -- {} \;
```
Count code lines
```sh
( find ./ -name '*.py' -print0 | xargs -0 cat ) | wc -l
```