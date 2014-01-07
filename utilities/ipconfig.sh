#!/bin/bash
interfaces=($(ifconfig | sed 's/:/\ /' | cut -d ' ' -f 1 -s | grep '^[a-z]' | grep -v lo))
num=0
if [ ${#interfaces[@]} -eq 1 ]
then
    printf "Selecting interface %s\n" ${interfaces[0]}
else
    for i in "${interfaces[@]}"
    do
        printf "Interface %d: %s\n" $num $i
        num=$[num+1]
    done
    echo "Select interface: "
    read num
fi

echo "Enter team number, or 0 for DHCP: "
read teamnum
if [ $teamnum -eq 0 ]
then
    sudo ifconfig ${interfaces[$num]} 0.0.0.0 0.0.0.0 && dhclient
else
    sudo killall dhclient
    sudo ifconfig ${interfaces[$num]} 10.$[teamnum/100].$[teamnum%100].$[$RANDOM%240+10] netmask 255.0.0.0 up
    if grep -q 208.67.222.222 /etc/resolve.conf
    then
        echo -e "nameserver 208.67.222.222\nnameserver 208.67.220.220" | sudo tee -a /etc/resolve.conf
    fi
fi

