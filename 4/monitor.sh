#!/bin/bash
make clean
make

# cleans the log files
rm -f comm.log forks.log

# gains the pids of the child processes
strace -o dump.txt -ff ./run
pids=($(ls | grep "dump.txt" | cut -d'.' -f3))


fpid=${pids[0]}

# Loop through all elements in the array
for i in ${pids[@]}; do
    if [ $i -lt $fpid ]; then
        fpid=$i
    fi
done

# LOGGING FORKS
f_dump="dump.txt.$fpid"
s_pids=($(cat $f_dump | grep clone | awk -F ' = ' '{print $2}'))
if [ ${#s_pids[@]} -ne 0 ]; then
    echo "Number of sons processes: "${#s_pids[@]} > forks.log
    for i in ${s_pids[@]}; do
        echo "Son pid "$i >> forks.log
    done
else
    echo "No forks." >> forks.log
fi

# LOGGING WRITES (communication through pipes)
writes=$(cat $f_dump | grep write | awk -F "[()]" '{print $2}'| cut -d ',' -f 1)
touch comm.log
for i in ${writes[@]}; do
    if [ $i -gt 2 ]; then
        echo "$(date): process wrote to child on fd $i." >> comm.log
    fi
done


# cleans the folder from dumps
rm -f dump.txt.*




