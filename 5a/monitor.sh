#!/bin/bash

# file generation
rm -f irr_access.log
touch ltrace_log.txt # temp log
touch irr_access.log

# execution and syscall tracing
ltrace -b -o ltrace_log.txt ./run 
fopens=$(more ltrace_log.txt | grep fopen)

# the loop gets the path where the user tries to access
for e in "${fopens[@]}"
do
    full_path=$(echo $e | awk -F'"' '{print $2}')
    folder=$(echo $full_path | rev | cut -d'/' -f2- | rev)
    
    # if the user is not the owner of the directory he's accessing,
    # a new line to the log file is added
    if [[ $(stat -c %U $folder) == $(whoami) ]]; then
        echo "Regular access to: "$folder" $(date)" >> irr_access.log
    else
        echo "Irregular access to: "$folder" $(date)" >> irr_access.log
    fi
done

# the temp log is removed
rm -f ltrace_log.txt
