#!/usr/bin/python3

import sys

"""
Function to process and output the data. Takes a FASTA header and the 
sequence; strips out any insertion characters and prints the header and
sequence
"""
def Process(header, sbjct):
    print(header)
    sbjct = sbjct.replace("-", "")
    print(sbjct)


"""
Main program
"""

# Get the filename from the command line
filename = sys.argv[1]

# Default Range start and stop
start = 125
stop  = 500

# Get start and stop if specified
if(len(sys.argv) > 2):
    start = int(sys.argv[2])
if(len(sys.argv) > 3):
    stop  = int(sys.argv[3])

# Open the file for reading
fp = open(filename, "r")

gotSequence  = False # Flag to indicate we have a sequence to print
inAlignments = False # Flag to indicate we are in the alignments block
sbjct        = ''    # The BLAST hit's sequence
theHeader    = ''    # FASTA header as read from the file
header       = ''    # The FASTA header with Range info added
rangeOK      = False # Is the range correct?

for line in fp:
    line = line.rstrip()

    if(line[0:10] == "Alignments"):
        inAlignments = True

    elif(line[0:5] == "Range"):
        if(gotSequence and rangeOK):
            Process(header, sbjct)
            gotSequence  = False
        fields = line.split()
        if((int(fields[2]) <= start) and (int(fields[4]) >= stop)):
            rangeOK = True
        else:
            rangeOK = False
        header = theHeader + ' (' + line + ')'
        sbjct  = ''

    elif(inAlignments and (line[0:1] == ">")):
        if(gotSequence and rangeOK):
            Process(header, sbjct)
            gotSequence = False
        theHeader = line
        sbjct     = ''
        
    elif(inAlignments and (line[0:5] == "Sbjct")):
        fields       = line.split()
        sbjct       += fields[2]
        gotSequence  = True

if(gotSequence and rangeOK):
    Process(header, sbjct)
