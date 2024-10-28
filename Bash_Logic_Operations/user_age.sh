#!/bin/bash 
 echo "How old are you?"
 read age
 if [[ "$age" -lt 18 ]]
 then 
    echo "You are a minor."
elif [ "$age" -ge 18 ] && [ "$age" -lt 64 ]; 
then
    echo "You are an adult."
else [["$age" -ge 65]]    
fi