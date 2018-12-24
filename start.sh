#!/bin/bash

if [ $# -gt 0 ]
then
  rm ./*.csv
  ./packstat $1
  python main.py
else
  echo 'Ooops! You forgot to specify a filename'
fi
