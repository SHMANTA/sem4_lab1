#!/bin/bash

args=("$@")
n=$#

if [[ n -eq 0 ]]
then
	echo " "
	exit 0
fi

for ((i=n-1; i>=0; i--))
do
	echo -n "${args[$i]}"
	if [[ i -gt 0 ]] 
	then 
		echo -n " "
	fi	
done
echo
