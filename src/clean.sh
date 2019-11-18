#/usr/bin/env bash

if [ -e *.pyc ]
then
    rm *.pyc
fi

if [ -d __pycache__ ]
then
    rm -r __pycache__
fi

if [ -e config.txt ]
then
    rm config.txt
fi
