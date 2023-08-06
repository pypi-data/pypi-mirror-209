#!/bin/bash

###################################################################
# do_snapshot_volume
# Purpose: create a replay of a dellsc volume
#          The replaced dellsc volume is then deleted
# 
#    Args: -m -> source mountpoint 
#          -l -> Label for replay 
#          -r -> retention (days) 
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

This script creates a pure storage volume, providing size of volume to be create


OPTIONS:
  -h                        Show this message
  -n source volume          Name of the volume for which snapshot has to be taken.
  -s size                   Size of the volume to be created 
                              - Units: T,G,M eg: 1TB should be specified as 1T
  -k /path/to/secrets.json  Secret file containing URL and credential to access Pure Storage

E.g.
   $0 -n TEST123 -s 1T -k /path/to/secrets.json

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
while getopts "h:n:s:k:" opt
do
  case $opt in
    h)
      usage
      exit
      ;;
    n)
      name=$OPTARG
      ;;
    s)
      size=$OPTARG
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
if [ -z "$name" ] || [ -z "$size" ] || [ -z "$secrets" ]
then
   usage
   exit
fi

# Call ucampurestorage package
result=$($ucampurestorage --file $secrets volume create --name $name --size $size)

if [[ $result == *"[Command succeeded - Returns True]"* ]]
then
    echo "Command succeeded."
    exit 0
else
    echo "Command failed. Please check the ucampurestorage log file in /var/log/ucampurestorage/."
    exit 1
fi