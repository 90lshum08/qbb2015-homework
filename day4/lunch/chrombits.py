import numpy
import copy

class ChromosomeLocationBitArrays( object ):

    def __init__( self, dicts=None, fname=None ):
        # If dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        # If fname parameter provided, initialize from file
        if fname is not None:
            for line in open( fname ):
                fields = line.split()
                name = fields[0]
                size = int( fields[1] )
                arrays[name] = numpy.zeros( size, dtype=bool )
        self.arrays = arrays

    def set_bits_from_file( self, fname ):
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            self.arrays[ chrom ][ start : end ] = 1
    
    def Start_End_Bed (self, fname):
        bed = []
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chromosome = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            bed.append( [chromosome, start, end] )
        
    def intersect( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts = rval )
        
    def union( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def complement( self ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts = rval )
        
    def copy( self ):
        return ChromosomeLocationBitArrays( 
            dicts=copy.deepcopy( self.arrays ) )
    
    def intervals ( self ):
        interval = []
        for chrom in self.arrays:
            bln1 = False
            startcounter = 0
            for counter, value in enumerate(self.arrays[chrom]):
                if value:
                    if not bln1:
                        bln1 = True
                        startcounter = counter
                else:
                    if bln1:
                        bln1 = False
                        interval.append((chrom,startcounter,counter-1))
        return interval 

            

        
