#Reverse Blurb Readme

#As of 11/7/2016 @ 9:00am I decided on the name "blurb" for what this program makes and reverses. 

TODO: Implement 	                   

As of 9/6/2016 @ 2:52pm multi-core processing appears to work. I can in fact hit 100% CPU usage.
http://imgur.com/a/NS6O4

~~#IMPORTANT: Comment out lines 114-116 && 120-138 for this to run as of 8/10/16 @ 1:28am~~

Specs of blurb:
An example blurb for a file with the arguments of “-i ./test.txt”
* File name and extension’s hex value followed by hyphen
   * 746573742E747874
* Add a delimiter stating new section
* If a pattern is in the file
   * 00 = no pattern
   * 01 = zip file (Parts in square brackets change)
      * Starts with 50 4B 03 04 14 [00 00 00 08 00]
      * Ends with  50 4B 01 02 14 [00 14 00 00 00] [08 00 0C 9F F0 48 03 FD C4 06 D5 46 00 00 CA 51 00 00 09 00 00 00 00 00 00 00 00 00 20 00 00 00 00 00 00 00] **FILENAME** 50 4B 05 06 00 00 00 00 01 00 01 00 [37 00 00 00 FC 46 00 00 00 00] 
   * 02 = tbd and so on
* Add a delimiter stating new section 
   * we could have a different section specifying block and split amounts
* Beginning block in proper size (using the default of 4 since no -b was specified)
   * 49662079
* Add a delimiter stating new section
* Length until start of new section (in this case in bytes)
   * 20
* Add a delimiter stating new section
* Middle Start block in proper size
   * 6D65616E
* Add a delimiter stating new section
* Length until start of new section (in this case in bytes)
   * 20
* Add a delimiter stating new section
* Middle End block in proper size
   * 2120416C
* Add a delimiter stating new section
* Length until start of new section (in this case in bytes)
   * 20
* Add a delimiter stating new section
* Ending block in proper size
   * 20224A6F
* Add a delimiter stating new section
* Length until start of new section (in this case in bytes)
   * 12
* Add a delimiter stating new section

* Checksum of file 
   * 9180801A5E24A242EB91953E41394EFB


So the whole blurb is:
`746573742E747874-00-49662079-20-6D65616E-20-2120416C-20-20224A6F-12-9180801A5E24A242EB91953E41394EFB`


Another thought I had could be each split of the file has it’s own checksum for larger files


Specs of Program:
   * Utilize any available hardware 
   * GPU (NVIDIA and AMD)
   * iGPU as well (Intel)
   * CPU with multi-core/threads
   * Command line arguments: *=required useage
   *  -i for input (blurb or path to file)*
   * -o for output (blurb or path to file)*
   * If input is a file and -o is blank print blurb to screen
   * -t to specify amount of cores/threads
   * -b to specify block size (default: 4)
   * -s to specify split amounts (default: 4)
   * -c for checksum type (default: md5)
   * -h for help


Goals:
   * Generation of blurb from file needs to be almost instant
   * Compare to 300KB/s assuming constant speed
   * Example times: 
   * 1MB file in 3.4 second
   * 128MB file in 437 seconds or 7 minutes
   * 512MB in 1748 seconds or 29 minutes
   * 1GB file in in 2495 seconds or 58 minutes
   * I’m prepared to lose against this speed for small files but then why would you compress an already small file?
