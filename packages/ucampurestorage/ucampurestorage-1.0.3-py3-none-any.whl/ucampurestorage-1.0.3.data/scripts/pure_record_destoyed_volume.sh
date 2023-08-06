#!/bin/bash 

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

This script saves the list of destroyed volumes in files

OPTIONS:
   -h                                  Show this message
   -o /path/to/dir/                    Path of where the destroyed volumes information will be saved
   -k /path/to/secrets.json            Secret file containing URL and credential to access Pure Storage

E.g.
   $0 -o /path/to/dir/ -k /path/to/secrets.json

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

while getopts "ho:k:" opt
do
  case $opt in
    h)
      usage
      exit
      ;;
    o)
      output_dir=$OPTARG
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
if [ -z "$output_dir" ] || [ -z "$secrets" ]
then
   usage
   exit
fi

mkdir -p "$output_dir"
datestamp=$(date '+%Y%m%d')
output_file="${output_dir}/${datestamp}"

destroyedVols=$($ucampurestorage --file $secrets list --object destroyed_volumes)

if [[ $destroyedVols == *"[Command succeeded - Returns True]"* ]]
then
    echo "$destroyedVols"  > "${output_file}.pure_destoyed"
    echo "Command succeeded."
    exit 0
else
    echo "Command failed. Please check the ucampurestorage log file in /var/log/ucampurestorage/."
    exit 1
fi
