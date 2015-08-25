#!/usr/bin/env python

# Integer - unlimited size
i = 4537289

# Floating point or Real number
f = 0.333
i_as_f = float(i)
f_as_i = int(f)

# String
s = "string"

# Boolean
truthy = True
falsy = False

# Lists - square brackets - convention contains only one type
l = [1,2,3,4,5]
l.append( 7 ) # Adds to a list

# Tuple - elements can have different types - cannot be ammended
t = (1,"foo",5.0)

# Dictionary
d1 = { "key1": ["lions","tigers","bears"], "key2" : "value2" }
d2 = dict( key1="value1", key2="value2")
d3 = dict( [ ("key1","value1"), ("key2","value2") ] )

for value in ( i, f, s, truthy, l, t, d1, d2, d3 ):
    print value, type( value )
    