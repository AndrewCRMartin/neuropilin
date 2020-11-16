#!/usr/bin/perl
use strict;
my $start  = 1;  # Flag to indicate we are in a sequence
my $inAlignments = 0; # FLag to indicate we are in the alignments block
my $query  = ''; # The query sequence
my $sbjct  = ''; # The subject sequence
my $qStart = 0;  # The query start
my $qEnd   = 0;  # The query end
my $sStart = 0;  # The subject start
my $sEnd   = 0;  # The subject end
my $header = ''; # The FASTA header

@::querySeq = (); # The assembled query sequence
@::sbjctSeq = (); # An assembled subject sequence
@::mapping  = ();
    
while(<>)
{
    if(/Alignments:/)
    {
        $inAlignments = 1;
    }
    elsif($inAlignments && /^\>/)
    {
        if($start == 0)
        {
            Process($header, $qStart, $qEnd, $query, $sStart, $sEnd, $sbjct);
        }
        chomp;
        $header = $_;
        $start  = 1;
        $query  = '';
        $sbjct  = '';
    }
    elsif($inAlignments && /^Query/)
    {
        my @fields = split;
        $qStart = $fields[1] if($start);
        $qEnd   = $fields[3];
        $query .= $fields[2];
    }
    elsif($inAlignments && /^Sbjct/)
    {
        my @fields = split;
        $sStart = $fields[1] if($start);
        $sEnd   = $fields[3];
        $sbjct .= $fields[2];

        $start = 0;
    }
}

sub Process
{
    my($header, $qStart, $qEnd, $query, $sStart, $sEnd, $sbjct) = @_;

    #    printf("%6d %s %6d\n",   $qStart, $query, $qEnd);
    #    printf("%6d %s %6d\n\n", $sStart, $sbjct, $sEnd);
    printf("%s\n", $header);
    $sbjct =~ s/\-//g;
    printf("%s\n", $sbjct);
    

    my @inQuerySeq = split(//, $query);
    my @inSbjctSeq = split(//, $sbjct);
    
    if(!scalar($::querySeq))
    {
        # Initialize when there is no sequence yet
        my $outSeqPos = $qStart;
        for(my $inSeqPos = 0; 
            $inSeqPos    < scalar(@inQuerySeq);
            $inSeqPos++)
        {
            $::querySeq[$outSeqPos++] = $inQuerySeq[$inSeqPos];
        }
    }
    else
    {
        # Update to account for new residues and gaps
        my $outSeqPos = $qStart;
        for(my $inSeqPos = 0; 
            $inSeqPos    < scalar(@inQuerySeq);
            $inSeqPos++)
        {
#            if(
            $::querySeq[$outSeqPos++] = $inQuerySeq[$inSeqPos];
        }
        
    }

#    print "Query Seq:\n";
#    foreach my $c (@::querySeq)
#    {
#        print $c;
#    }
#    print "\n";
}
