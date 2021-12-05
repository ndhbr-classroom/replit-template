#!/bin/bash
script_path=`dirname $(realpath $0)`
orga_url=git@github.com:ndhbr-classroom/

# check for parameter
if [ -z "$1" ]
then
    printf "Usage: get <REPOSITORY-NAME>\n"
else
    printf "Selected exercise: $1\n"

    # clone
    cd $script_path
    git clone $orga_url$1.git
    
    # git clone went wrong, probably enough error message by github
    if [ ! -d "$script_path/$1" ]; then
        exit 1
    fi

    printf "\nYour exercise template was cloned into the folder $1. "
    printf "If you want to reset your task, just delete the folder $1 and run the command again.\n"
fi
