#1/bin/bash 

args=("$@")
n=$#

if [[ n -eq 0 ]]
then 
	echo " "
	exit 0
fi

i=$((n-1))

while [ $i -ge 0 ]
do 
	echo -n "${args[$i]}"
	if [[ i -gt 0 ]]
	then 
		echo -n " "
	fi
	i=$((i-1))
done
echo

