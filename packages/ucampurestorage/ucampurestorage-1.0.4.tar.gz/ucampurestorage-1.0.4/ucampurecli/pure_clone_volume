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

This script creates a clone from a volume. 
The clone will be mapped to the local server and mounted on the desired mountpoint.

Restrictions for use:
  * The server must be connected to the same Pure Storage
  * The volume must exist.

OPTIONS:
   -h                                  Show this message.
   -n clone_name                       Name of the clone volume.
   -s souce_name                       Name of the source volume from which to create the clone.
   -p /path/to/mountpoint              Mountpoint of the clone volume.
   -k /path/to/secrets.json            Secret file containing URL and credential to access Pure Storage.

E.g.
   $0 -n clone_name -s source_name -p /t10 -k /path/to/secrets.json

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

while getopts "h:n:s:p:k:" opt
do
  case $opt in
    h)
      usage
      exit
      ;;
    n)
      clone_name=$OPTARG
      ;;
    s)
      volume_name=$OPTARG
     ;;
    p)
      t_mount_point=$OPTARG
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
if [ -z "$t_mount_point" ] || [ -z "$clone_name" ] || [ -z "$volume_name" ] || [ -z "$secrets" ]
then
   usage
   exit
fi

# Call ucampurestorage package
result=$($ucampurestorage --record_config True --file $secrets volume clone --name $clone_name --srcvol $volume_name --target_mp $t_mount_point)
if [[ $result == *"[Command succeeded - Returns True]"* ]]
then
    echo "Command succeeded."
    exit 0
else
    echo "Command failed. Please check the ucampurestorage log file in /var/log/ucampurestorage/."
    exit 1
fi