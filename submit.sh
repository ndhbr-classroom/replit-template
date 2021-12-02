#!/bin/bash

# check for parameter
if [ -z "$1" ]
then
    printf "Usage: submit <REPOSITORY-NAME>\n"
else
    # check wether folder exists
    if [ ! -d "$1" ]; then
        printf "Exercise does not exist in your space\n"
        exit 1
    fi

    cd $1
    # if changed something
    if [[ `git status --porcelain` ]]; then
        git add .
        git commit -m "Automated commmit"
        git push -u origin master
    fi
    cd ..
fi
