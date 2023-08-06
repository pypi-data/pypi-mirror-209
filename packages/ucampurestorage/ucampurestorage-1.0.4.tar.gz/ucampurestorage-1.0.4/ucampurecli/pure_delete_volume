#!/bin/bash

###################################################################
# do_delete_purestorage_volume
# Purpose: Unmap and delete of PureStorage volume 
#
#    Args: $1 -> name of volume to delete
#
#  Output: Log of actions
# Returns: TRUE for success, FALSE for failure
###################################################################
# ucampurestorage="/usr/local/bin/ucampurestorage"
ucampurestorage="/root/test/pypi_test/venv/bin/ucampurestorage"

echo "Invoked with: $0 $@"
echo "My PID is $$"

###################################################################
# Purpose: usage information
###################################################################
function usage()
{
cat << EOF
usage: $0 options

This script unmaps and deletes a purestorage volume.

OPTIONS:
  -h 
  -n name                             Name of the volume.
  -k /path/to/secrets.json            Secret file containing URL and credential to access Pure Storage.

E.g.
  $0 -n 123455 -k /path/to/secrets.json

NB. 
1. /path/to/secrets.json must be in the following format:
{
  "client_id": "pure_api_client_id",
  "key_id": "pure_api_key_id",
  "client_name": "pure_api_client_name",
  "storage": "purestorage.cam.ac.uk",
  "user": "pureuser",
  "password": "purepassword",
  "keyfile": "private.pem"
}

2. ucampurestorage must be installed and located under /usr/local/bin/
EOF
}

###################################################################
# Parse the args 
###################################################################

while getopts "hn:k:" opt
do
  case $opt in
    h)
      usage
      exit
      ;;
    n)
      name=$OPTARG
     ;;
    k)
      secrets=$OPTARG
     ;;
    ?)
      usage
      exit
      ;;
  esac
done

# check required arguments
if [ -z "$name" ] || [ -z "$secrets" ]
then
   usage
   exit
fi

# Call ucampurestorage package
result=$($ucampurestorage --file $secrets volume delete --name $name -nop)
if [[ $result == *"[Command succeeded - Returns True]"* ]]
then
    echo "Command succeeded."
    exit 0
else
  echo "Command failed. Please check the ucampurestorage log file in /var/log/ucampurestorage/."
  exit 1
fi