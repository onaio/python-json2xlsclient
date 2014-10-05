#!/bin/bash

set -eu

function usage {
  echo "json2xlsclient convenience test script"
  echo "Usage: $0 [OPTION]..."
  echo ""
  echo "  -x, --stop               Stop running tests after the first error or failure."
  echo "  -f, --flake8             Run flake8 only"
  echo "  -h, --help               Print this help text...assuming you didn't know that already :)"
  echo ""
  echo "If called with no args, the script will just run the tests (nosetests),"
  exit
}

function process_option {
  case "$1" in
    -h|--help) usage;;
    -p|--flake8) just_flake8=1
  esac
}

just_flake8=0

for arg in "$@"; do
  process_option $arg
done

if [ $just_flake8 -eq 1 ]; then
    echo "Running flake8 ..."
    flake8 json2xlsclient 
    exit
fi

# Cleanup *.pyc
find . -type f -name "*.pyc" -delete

#run nosetests + doctests
nosetests -w tests/ --with-doctest
