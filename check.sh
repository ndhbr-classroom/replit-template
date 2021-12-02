#!/bin/bash
script_path=`dirname $(realpath $0)`

# check for parameter
if [ -z "$1" ]
then
    printf "Usage: check <REPOSITORY-NAME>\n"
else
    # check wether folder exists
    if [ ! -d "$script_path/$1" ]; then
        printf "Exercise does not exist in your space\n"
        exit 1
    fi

    cd $script_path/$1
    lang=`cat .language`

    case $lang in
     javascript) ## JS
          npm test
          ;;
     python) ## Python
          pytest
          ;;
     *)
          echo "Did not find valid .language file, did you remove or modify it?"
          ;;
    esac

    cd ..
fi