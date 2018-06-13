#Subnetting calculator
#Use Python 2.7 version.(will not work on python 3 version)

# Asking for IP address and checking validation
import random
try:

    while True:
        ip_address = raw_input("Please enter IP address: ")
        ip_address_list = ip_address.split(".")
        if (len(ip_address_list) == 4) and (1 <= int(ip_address_list[0]) <= 223) and (int(ip_address_list[0]) != 127) and ( int(ip_address_list[0]) != 169 or int(ip_address_list[1]) != 254) and (0 <= int(ip_address_list[1]) <= 255) and (0 <= int(ip_address_list[2] <= 255)) and (1 <= int(ip_address_list[3]) <= 254):
            break
        else:
            print "Please provide valid IP address."
            continue
    #print ip_address_list
    # Asking for Subnet mask and checking validation
    while True:
        sub_mask_fix = ["255", "252", "248", "240", "224", "192", "128", "0"]
        sub_mask = raw_input("Please provide subnet mask: ")
        sub_mask_list = sub_mask.split(".")
        if (len(sub_mask_list) == 4) and (sub_mask_list[0] == '255') and (sub_mask_list[1] in sub_mask_fix) and (sub_mask_list[2] in sub_mask_fix) and (sub_mask_list[3] in sub_mask_fix) and (sub_mask_list[1] >= sub_mask_list[2] >= sub_mask_list[3]):
            break
        else:
            print "Please provide valid subnet mask"
    #print sub_mask_list

    # Calculating wild mask
    wild_mask = []
    for element in sub_mask_list:
        new_element = abs(255 - int(element))
        wild_mask.append(str(new_element))
    #print wild_mask
    wild_mask_strg = wild_mask[0]+"." + wild_mask[1]+"." + wild_mask[2]+"." + wild_mask[3]
    #print wild_mask_strg

    # Converting IP and subnet mask into binary formate
    #IP address to binary
    net_bin_list = []
    for net_num in ip_address_list:
        net_bin = bin (int(net_num))
        net_bin_split = net_bin.split("b")[1]
        #print net_bin_split
        if len(net_bin_split) == 8:
            net_bin_list.append(net_bin_split)
        elif len(net_bin_split) < 8:
            net_bin_8 = net_bin_split.zfill(8)
            net_bin_list.append(net_bin_8)
    #print net_bin_list

    net_bin_strg = net_bin_list[0] + net_bin_list[1] + net_bin_list[2] + net_bin_list[3]
    #print net_bin_strg

    #Subnet mask to binary
    mask_bin_list = []
    for mask_num in sub_mask_list:
        mask_bin = bin (int(mask_num))
        #print mask_bin
        mask_bin_split = mask_bin.split("b")[1]
        #print mask_bin_split
        if len(mask_bin_split) == 8:
            mask_bin_list.append(mask_bin_split)
        elif len(mask_bin_split) < 8:
            mask_bin_8 = mask_bin_split.zfill(8)
            mask_bin_list.append(mask_bin_8)
    #print mask_bin_list

    mask_bin_strng = mask_bin_list[0] + mask_bin_list[1] + mask_bin_list[2] + mask_bin_list[3]

    #print mask_bin_strng


    # Calculating no. of host and no. subnets

    no_of_zeros = mask_bin_strng.count("0")
    #print no_of_zeros

    no_of_host = (2 ** no_of_zeros) - 2
    no_of_ones = 32 -no_of_zeros
    #print no_of_host

    #### Finding N/W address and Broadcast address
    #N/w address
    net_ones = net_bin_strg[:no_of_ones]
    #print net_ones
    net_strg = net_ones + ("0" * no_of_zeros)
    net_strg_list = []
    for element_net in range(0,32,8):
        net_strg_element = int(net_strg[element_net:element_net+8],2)
        net_strg_list.append(net_strg_element)

    #print net_strg_list
    net_add = str(net_strg_list[0]) + "." + str(net_strg_list[1]) + "." + str(net_strg_list[2]) + "." + str(net_strg_list[3])
    #print net_add

    #Broadcast address
    brd_strg = net_ones + ("1" * no_of_zeros)
    #print brd_strg
    brd_list = []
    for element_net in range(0,32,8):
        brd_strg_element = int(brd_strg[element_net:element_net+8],2)
        brd_list.append(brd_strg_element)
    #print brd_list
    brd_add = str(brd_list[0]) + "." + str(brd_list[1]) + "." + str(brd_list[2]) + "." + str(brd_list[3])
    #print brd_add

    print "\n\nIP address you have entered:", ip_address
    print "For subnet mask:", sub_mask
    print "Wild card mask:" ,wild_mask_strg
    print "No. of host per subnet:", no_of_host
    print "Network address:", net_add
    print "Broadcast address:", brd_add

    while True:
        random_ask = raw_input("Do you want to generate random IP address(y/n):")
        if random_ask == "y" or random_ask == "Y":
            random_list = []
            for indexb,oct_brd in enumerate(brd_list):
                for indexn, oct_net in enumerate(net_strg_list):
                    if indexb == indexn:
                        if oct_net == oct_brd:
                            random_list.append(oct_brd)
                        else:
                            random_no = random.randint(int(oct_net),int(oct_brd))
                            random_list.append(random_no)
            #print random_list
            print str(random_list[0]) + "." + str(random_list[1]) + "." + str(random_list[2]) + "." + str(random_list[3])
        else:
            print "Thank you!!!"
            break
except:
    print ""


#####Credits######
#Name: Mayur Baviskar
#Github: www.github.com/mayur01201
#Email: mayur01201@gmail.com
