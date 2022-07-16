from scapy.all import ARP, Ether, srp
import time


target =input(str("Type in the address you would like to target Ex: 192.168.0.0/24: "))

while True:
    #Text file for our addresses
    file = open("addresses.txt", "a")

     # The list of addresses
    address = []

    # create the broadcast packet
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # creating a ARP packet
    arp_packet = ARP(pdst=target)

    # making our target packet
    t_packet = broadcast/arp_packet

    #srp allows us to send and recieve packets
    result = srp(t_packet, timeout=3, verbose=0)[0]

    for sent, received in result:
    # Appending the ip and mac address we recieved to a list
        address.append({'ip': received.psrc, 'mac': received.hwsrc})

    #writing to our text file
    file.write("\n%s" % time.ctime())
    file.write("\nDevices in your network:\n")
    file.write("------------------\nIP Address\tMAC Address\n------------------\n")
    #formating our text
    for i in address:
        file.write("\n{}\t{}".format(i["ip"], i["mac"],"\n"))
    
    #text break
    file.write("\n_________________________________\n")
    file.close()
    #putting a delay on our loop
    time.sleep(10)
    

     