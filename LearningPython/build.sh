#! /bin/bash

echo 'Running tests ...'

python count_vowels.py

if (( $? > 0 ))
then
  echo 'TC1 failed with exit code $rc'
  exit 1
fi

python open-chrome-browser.py

if (( $? > 0 ))
then
  echo 'TC2 failed with exit code $rc'
  exit 1
fi

echo 'Tests successful'
exit 0
