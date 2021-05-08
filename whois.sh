#!/bin/bash
function whois_init() {  
echo $arg2; sleep 1;  
} 
function whois_strt() {
whois_init | busybox telnet whois.iana.org 43 | tee /dev/tty ; 
}
if [[ $arg1 = 'whois' ]]
then 
whois_strt
fi