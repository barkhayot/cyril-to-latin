#!/bin/bash

for i in {1..20}
do
  scp /path/to/file1 user@fs$i:/path/to/destination1 && \
  scp /path/to/file2 user@fs$i:/path/to/destination2 && \
  ssh user@fs$i "systemctl restart myservice"
done
