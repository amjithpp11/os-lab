#AMJITH PP 20219016
#palindrome

#! /bin/bash

echo "Enter the string:" 
read string

length=${#string}
reverse=""

for (( i=$length-1; i>=0; i-- ))
do
	reverse="$reverse${string:$i:1}"
done

if [ $string == $reverse ]
then
	echo "$string is palindrome"
else
	echo "$string is not palindrome"
fi


