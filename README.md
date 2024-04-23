; always update
git fetch --all
git pull

; if you have changes sa "master" branch
stash your changes
git checkout -b branchname
pop stash

; push
git add . 
git commit -m "date time"
git push
