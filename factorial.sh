#AMJITH PP 20219016
#factorial

#! /bin/bash

read -p "Enter the value of n:" n
factorial=1

while [ $n != 0 ]
do
	
	factorial=$((factorial * N))
	n=`expr $n - 1`
done

echo "Factorial: $factorial" 

