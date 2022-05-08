#AMJITH PP 20219016
#fibonacci

#! /bin/bash

read -p "Enter the number of numbers in the series: " n

x=0
y=1
z=1

echo $x
if [ $n != 1 ]
then
	echo $y
fi
n=`expr $n - 2`

while [ $n -gt 0 ]
do
	echo $z
	x=$y
	y=$z
	z=`expr $x + $y`
        n=`expr $n - 1`	
done

