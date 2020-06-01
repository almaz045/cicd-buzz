#!/bin/sh

setup_git() {
  git config --global user.email "internet69s@mail.ru"
  git config --global user.name "almaz045"
}

commit_website_files() {
  git checkout -b master
  git add . *.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin https://${GH_TOKEN}@github.com/almaz045/cicd-buzz.git > /dev/null 2>&1
  git push --quiet --set-upstream origin master 
}

setup_git
commit_website_files
upload_files
