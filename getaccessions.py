#!/usr/bin/python3

import sys

# Get the filename from the command line
filename = sys.argv[1]

# Open the file for reading
fp = open(filename, "r")

# The hits and their accessions are in a block that starts with the word "Description"
# There are about 8 lines before that.
# That block ends with a blank line and the next block starts with the word "Alignments"
# i.e.
# -----------------------------------------------------------------------------------------------------------------
# Description                                                       Score  Score cover Value  Ident  Accession        
# neuropilin-1 isoform a precursor [Homo sapiens]                   1927   1927  100%  0.0    100.00 NP_003864.5      
# neuropilin-1 isoform X1 [Gorilla gorilla gorilla]                 1922   1922  100%  0.0    99.67  XP_004049296.1   
# ...
# PREDICTED: cubilin [Eurypyga helias]                              112    214   27%   1e-21  29.73  XP_010155518.1   
# embryonic protein UVS.2 [Xenopus tropicalis]                      112    185   26%   1e-21  28.88  XP_004913424.2   
# 
# Alignments:
# >neuropilin-1 isoform a precursor [Homo sapiens]
# -----------------------------------------------------------------------------------------------------------------
#
# We start off setting a flag to say that we are not in the list of hits
inList = False

# Now step through the lines in the file
for line in fp:
    # This just removes the newline character from the end of the line
    line = line.rstrip()

    if(line[0:11] == "Description"):
        # If the line starts with the word "Description" then we are entering the block
        inList = True
    elif(line == ""):
        # If the line is blank then we are leaving the block
        inList = False
    elif(inList):
        # Otherwise, if we are in the block, print the line from column 99 onwards (i.e. the accession)
        print(line[99:])


