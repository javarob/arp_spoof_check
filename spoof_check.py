
import os
import time
from datetime import datetime

# Access arp table and extract entries



def arp_table_extraction():
    # Read arp talbe and save in list
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    #print(arp_table)
    addresses = {} #dict for addresses & mac addresses

    #filter unnecessary data & store
    for line in arp_table_lines:
        if "ff-ff-ff-ff-ff-ff" in line or "ff:ff:ff:ff:ff:ff" in line:
            break
        if arp_table_lines.index(line) > 2:
            ip, mac, _type = line.split()
            addresses[ip] = mac
            #print(addresses)

    identify_duplicates(addresses)

# Examine IP & MAC and check for MAC duplication
def identify_duplicates(addresses):
    temp_mac_list = []
    print("Scanning...")
    time.sleep(3)
    for mac in addresses.values():
        # ends if MAC dup found
        if mac in temp_mac_list:
            print("Finished scanning")
            create_log("Arp Spoofed!\nThe address is:" + mac)
            break
        temp_mac_list.append(mac)

# Creates a file and appends it into a log of the arp spoofing event
def create_log(message):
    print("Generating logs...")
    time.sleep(3)
    date = datetime.now()
    with open("log.txt","a") as log:
        log.write(message + "\nDate: {}\n\n".format(date))
    print("The event is logged in log.txt")

# Verify direct execution
if __name__ == "__main__":
    arp_table_extraction()