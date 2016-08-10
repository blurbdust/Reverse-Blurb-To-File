#!/usr/bin/python

import sys, getopt, hashlib

block_list = []
byte_list = []
block_size = 4
block_count = 4

def main(argv):
#VARIABLES
    help_message = "main.py -i <inputfile or hash> -o <outputfile if hash>"
    inputhash = "&"
    inputfile = "^"
    output = ""

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
       
        file_to_hash(tohash)
    elif inputhash is not "&":
        hash_to_file(inputhash, block_count)
    else:
        print "Something bad happened."
        sys.exit(2)

    

def file_to_hash(tohash):
    tohash.close()
    print "Coming soon if I can actually get the motivation to work on this."


def hash_to_file(inputhash, block_count):
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
                globals()['block%s' % x] = globals()['block%s' % x] + "00"
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
    print string_of_file
    
    print "----"
    
    print hashlib.md5(string_of_file).hexdigest().upper()
    print hash_list[total_del]
    
    while(hashlib.md5(string_of_file).hexdigest().upper() != hash_list[total_del]):
        #Increment and try again
        string_of_file = increment_by_one(string_of_file, block_list, block_size, block_count, byte_list)
        
    print "Yay!"

def increment_by_one(string_of_file, block_list, block_size, block_count, byte_list):
    #THIS IS BROKEN BUT I'M TIRED
    index = 0;
    last_index = 0;
    hexval = ''
    for i in range(0, len(string_of_file) - 1):
        if (0 <= i <= ((block_size * 2) - 1)):
            index += 1
            print "Skip this"
        elif (((block_size * 2) - 1) <= i <= ((block_size * 2) - 1) + int(byte_list[index]) - 1):
            print "Skip this too"
            index += 1
        else:
            hexval = string_of_file[i] + string_of_file[i - 1]
            val = int(hexval, 16)
            val =+ 1
            hexval = hex(val)

    return string_of_file;

if __name__ == "__main__":
    main(sys.argv[1:])
