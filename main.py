#!/usr/bin/python

import sys, getopt, hashlib
from timeit import default_timer as timer

block_list = []
byte_list = []
byte = []
blacklisted_index = []
block_size = 4
block_count = 4
start = 0
end = 0
global_index = 0

def main(argv):
#VARIABLES
    help_message = "main.py -i <inputfile or hash> -o <outputfile if hash>"
    inputhash = "&"
    inputfile = "^"
    output = ""
    output_string = ""
    start = timer()
#END OF VARIABLES

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print help
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help_message
            sys.exit()
        elif opt in ("-i", "--ifile"):
            if "." in arg:
                inputfile = arg
            else:
                inputhash = arg
        elif opt in ("-o", "--ofile"):
            output = arg
    if inputfile is not "^":
        try:
            tohash = open(inputfile, "rb")
        except:
            print "Error! Probably file not found... I don't know enough python yet..."
            sys.exit(2)
       
        output_string = file_to_hash(tohash, inputfile)
        print output_string
    elif inputhash is not "&":
        hash_to_file(inputhash)
    else:
        print "Something bad happened."
        sys.exit(2)

    

def file_to_hash(tohash, filename):
    not_hash = ""
    string_of_file = tohash.read()
    md5hash = hashlib.md5(string_of_file).hexdigest().upper()
    #For now we are assuming defaults
    
    tmp = filename.encode('hex').upper()
    print tmp
    not_hash += tmp
    not_hash += '-'
    
    hex_of_file = string_of_file.encode('hex').upper()

def hash_to_file(inputhash):
    block = []
    maybe_file = ""
    #inputhash.split(h="-", num=string.count(h))
    total_del = inputhash.count('-')
    hash_list = inputhash.split('-')
    print hash_list
    filename = hash_list[0]
    filename = bytearray.fromhex(filename).decode()
    print filename
    pattern = hash_list[1]
    if "00" in pattern:
        print "No pattern, starting bruteforce from seed. Next few lines are the seed."
    elif "01" in pattern:
        print "Hash came from a zip file. This feature coming soon...ish."
    else:
        print "Something bad happened."
        
    for i in range(2, total_del):
        if i%2 == 0 and i != total_del:
            block_list.append(hash_list[i])
    print block_list
    
    for x in range(0, block_count):
        globals()['block%s' % x] = block_list[x]
    print block0
    
    for i in range(3, total_del):
        if i%2 == 1 and i != total_del:
            byte_list.append(hash_list[i])
    print byte_list

    
    for i in range(0, len(byte_list)):
        for x in range(i, block_count):
            for j in range(0, (int(byte_list[i]) / (2))):
                globals()['block%s' % x] = globals()['block%s' % x] + "**"
            break
   
    print block0
    print block1
    print block2
    print block3

    print "----"
    
    for y in range(0, block_count):
        block.append(globals()['block%s' % y])

    print block
    string_of_file = ''.join(block)
    
    print "----"

    for i in range(1, len(string_of_file) - 1):
        tmp = string_of_file[i] + string_of_file[i - 1]
        byte.append(tmp)

    for j in range(0, len(string_of_file) - 1):
        if (string_of_file[j] != '*'):
            blacklisted_index.append(j)

    print "Blacklisted index", blacklisted_index
    string_of_file = string_of_file.replace('*', '0')
    print string_of_file

    print "----MD5 Hashes Below----"
    
    print hashlib.md5(string_of_file).hexdigest().upper()
    print hash_list[total_del]
    
    global global_index
    
    while(hashlib.md5(string_of_file).hexdigest().upper() != hash_list[total_del]):
        #Increment and try again
        if global_index not in blacklisted_index:
            string_of_file = increment_by_one(string_of_file, global_index)
        else:
            global_index += 1
   
    print "Yay!"
    print "----"
    print string_of_file
    print "----"
    end = timer()

    print "It took me ", end-start, " seconds!"
    
    f = open(filename, 'w')
    f.write(string_of_file)
    f.close()

def increment_by_one(string_of_file, index):

    #The credit goes to Big-E for this function!
    
    hexval = string_of_file[index]              # Get the char that needs to be incremented    
    val = int ( hexval, 16 )                    # Convert the char to an int [0-16]
   
    val = (val + 1) % 0x10                      # Increment the int, this will be used to represent the next char
    hexval = "%X" % val                         # Convert the int back to a hex value
   
    list1 = list(string_of_file)                # Do stupid python stuff
    list1[index] = hexval                       # Save new value to array
    string_of_file = ''.join(list1)             # Do more stupid python stuff

    if hexval == '0' and (index + 1) < len(string_of_file): # Determine if next value to right needs to increment by one
        return increment_by_one(string_of_file, index + 1)  # Recursivelly call this function for value to right

    #print string_of_file
    return string_of_file;                      # Return from first instance of recursive functions


if __name__ == "__main__":
    main(sys.argv[1:])
