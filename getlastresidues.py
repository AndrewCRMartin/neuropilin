#!/usr/bin/python3

import argparse

# -------------------------------------------------------------------------
"""
print_last(sequence, nres)
--------------------------
Prints the last nres amino acids from the end of a sequence. If the
residues are ALL '-' characters, replaces them with alanine.
"""
def print_last(sequence, nres):
    # If we have the last nres residues missing they will all be '-'
    # characters in the alignment, so we construct a 'missing' string
    # to check. We will replace it with a set of alanines instead to
    # trick the phylogeny into thinking it's a valid sequence
    missing = '-' * nres
    fakeseq = 'A' * nres

    # Get the last residues from the sequence
    theseq  = sequence[-nres:]

    # if it's missing (i.e. all just '-' characters) replace it with the
    # fake sequence
    if(theseq == missing):
        theseq = fakeseq
        
    print(theseq)


# -------------------------------------------------------------------------
# Start of main program
# -------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='Extract last N residues from a FASTA alignment.')
parser.add_argument('filename', metavar='filename',
                    help='FASTA alignment file')
parser.add_argument('--nres', '-n', type=int, dest='nres', default=50,
                    action='store', help='number of residues to keep')
args = parser.parse_args()

# Get the data from the parser
filename = args.filename
nres     = args.nres

# Open the file for reading
fp = open(filename, "r")

# For storing a sequence
sequence = ''

# Now step through the lines in the file
for line in fp:
    # This just removes the newline character from the end of the line
    line = line.rstrip()

    # If it's a header line
    if(line[0:1] == '>'):
        # If we have some sequence information then print it (true for
        # everything but the first line)
        if(sequence != ''):
            # Print only the last nres characters
            print_last(sequence, nres)

        # Print the header line
        print(line)
        # Since this is a header it's the start of a new sequence
        # so we reset the sequence to a blank string
        sequence = ''
    else:
        # It's not a header so we append the current line to the
        # sequence
        sequence += line
        
# For the last entry in the file we need to print the sequence
# since normally we are only printing sequence information when
# we hit the next header line
if(sequence != ''):
    print_last(sequence, nres)
    
