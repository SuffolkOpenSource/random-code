#!/usr/bin/python

##########################################
# Python code to experiment with file
# Read & Write
##########################################

intf = '/Users/miket/Code/Python/MessageInABottle/textfile.txt'
infile = open(intf)
data = infile.read()
print data
infile.close()

outf = '/Users/miket/Code/Python/MessageInABottle/newfile.txt'
outfile = open(outf, 'w+')
outfile.write(data)
outfile.close()