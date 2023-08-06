
function about_test()
{
cat << EOF
TESTING ::
1. Creation of the Volume.
2. Mapping the Volume.
3. Clone the Volume.
4. Replace the Clone Volume.
5. Unmap the new replaced volume.
6. Take the snapshot of the volume.
7. Create clone volume from the snapshot. 
8. Map the clone volume of the snapshot volume.
9. Unmap the clone volume.
10. Unmap the clone volume of the snapshot volume and source volume.
11. Delete the clone volume of the snapshot volume and source volume.
13. Delete the clone volume of the snapshot volume and source volume.
14. Eradicate the clone volumes and source volume.
EOF
}

function show_result()
{
if [ $1 -eq $3 ]
then
  echo "Test $2 passed."
  sleep 10
else
  echo "Test $2 failed."
  exit 1
fi
}

SECRETS="/usr/local/etc/pure_secrets.json"
TEST_SOURCE_VOL="Test0007"
TEST_SOURCE_MP=/t0007
TEST_CLONE_VOL="Test0007_CLONE"
TEST_CLONE_MP="/t0007_clone"
TEST_SNAP_LABEL="snap"

about_test
# pure_create_volume -n $TEST_SOURCE_VOL -s 1T -k $SECRETS
# show_result $? 1 0

# pure_map_volume -n $TEST_SOURCE_VOL -p $TEST_SOURCE_MP -x 1 -k $SECRETS
# show_result $? 2 0

# pure_clone_volume -n $TEST_CLONE_VOL -s $TEST_SOURCE_VOL -p $TEST_CLONE_MP -k $SECRETS
# show_result $? 3 0

# pure_replace_volume -g $TEST_SOURCE_MP -t $TEST_CLONE_MP -k $SECRETS
# show_result $? 4 0

# pure_unmap_volume -g $TEST_SOURCE_MP -t $TEST_CLONE_MP -k $SECRETS
# show_result $? 5 0

# pure_create_snapshot -s $TEST_SOURCE_VOL -l $TEST_SNAP_LABEL  -k $SECRETS
# show_result $? 6 0
