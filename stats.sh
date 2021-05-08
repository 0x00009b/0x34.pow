#!/bin/bash
export PROCESSES=$(ps -e | wc -l)
export UPTIME=$(uptime | awk -F'( |,|:)+' '{d=h=m=0; if ($7=="min") m=$6; else {if ($7~/^day/) {d=$6;h=$8;m=$9} else {h=$6;m=$7}}} {print d+0,"day(s),",h+0,"hour(s),",m+0,"minute(s)."}')
export LOAD=$(uptime | awk -F'[a-z]:' '{ print $2}') 

printf "
Uptime: $UPTIME$
Load Average: $LOAD
Running Processes: $PROCESSES \n
"