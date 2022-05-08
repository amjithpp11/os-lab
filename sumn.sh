#AMJITH PP 20219016
#sumn

#! /bin/bash

read -p "Enter the value of n: " N

SUM=0

while [ $N != 0 ]
do
	echo "Enter number: " 
	read VAL
	SUM=`expr $SUM + $VAL`
	N=`expr $N - 1`
done

echo "SUM: $SUM"
