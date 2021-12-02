#!/bin/bash
script_path=`dirname $(realpath $0)`

# check for parameter
if [ -z "$1" ]
then
    printf "Usage: submit <REPOSITORY-NAME>\n"
else
    # check wether folder exists
    if [ ! -d "$script_path/$1" ]; then
        printf "Exercise does not exist in your space\n"
        exit 1
    fi

    cd $script_path/$1
    # if changed something
    if [[ `git status --porcelain` ]]; then
        git add .
        git commit -m "Automated commmit"
        git push -u origin master
    fi
    cd ..
fi
