#!/usr/bin/env python

import chrombits as chrm
import sys


CTCF = chrm.ChromosomeLocationBitArrays( fname = sys.argv[1])
BEAF = chrm.ChromosomeLocationBitArrays( fname = sys.argv[1])

CTCF.set_bits_from_file( fname = sys.argv[2])
BEAF.set_bits_from_file( fname = sys.argv[3])


inter = CTCF.intersect(BEAF)
comp = inter.complement()


compint = comp.intervals()

print compint

