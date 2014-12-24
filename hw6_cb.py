

import numpy as np


def sortwithloops(input):
    """sorts a list using loop
    returns sorted list"""
    temp = input[:] # create copy of list to change
    pos = temp.index(min(temp))
    NewList=list()  # create empty list to store sorted values
    NewList.append(temp.pop(pos))  # min from L into NewList

    while len(temp) != 0:
        for item in temp:
            pos =temp.index(min(temp))  # pos is position of min in new L
            NewList.append(temp.pop(pos)) # min from L appends to NewList

    return(NewList) #return a value
    

def sortwithoutloops(input):
    """sorts a list using sort function
    returns a sorted list"""
    
    temp = input[:] 
    temp.sort()
    return(temp) #return a value

def searchwithloops(input, value):
    """determines if value is in list using loop
    returns true or false"""
    
    test = False  # Set test to false
    for item in L:
        if item == value: #compare each item if found break
            test = True
            break
    return(test) #return a value

def searchwithoutloops(input, value):
    """determines if value is in list using 'in'
    returns true or false"""
    
    test = value in input
    return(test) #return a value	

def searchwithnp(input, value):
    return(np.any(input == value))

#--------------------------------------------------
# Setup for timer
#--------------------------------------------------
setup = '''
import numpy as np
import copy
import timeit 

L = [5,3,6,3,13,5,6]
input = np.array(L)


def sortwithloops(input):
    """sorts a list using loop
    returns sorted list"""
    temp = input[:] # create copy of list to change
    pos = temp.index(min(temp))
    NewList=list()  # create empty list to store sorted values
    NewList.append(temp.pop(pos))  # min from L into NewList

    while len(temp) != 0:
        for item in temp:
            pos =temp.index(min(temp))  # pos is position of min in new L
            NewList.append(temp.pop(pos)) # min from L appends to NewList

    return(NewList) #return a value
    

def sortwithoutloops(input):
    """sorts a list using sort function
    returns a sorted list"""
    
    temp = input[:] 
    temp.sort()
    return(temp) #return a value

def searchwithloops(input, value):
    """determines if value is in list using loop
    returns true or false"""
    
    test = False  # Set test to false
    for item in L:
        if item == value: #compare each item if found break
            test = True
            break
    return(test) #return a value

def searchwithoutloops(input, value):
    """determines if value is in list using 'in'
    returns true or false"""
    
    test = value in input
    return(test) #return a value	

def searchwithnp(input, value):
    return(np.any(input == value))

'''

setup2 = '''
import numpy as np
import copy
import timeit 

L = range(1,10000,2)
input = np.array(L)


def sortwithloops(input):
    """sorts a list using loop
    returns sorted list"""
    temp = input[:] # create copy of list to change
    pos = temp.index(min(temp))
    NewList=list()  # create empty list to store sorted values
    NewList.append(temp.pop(pos))  # min from L into NewList

    while len(temp) != 0:
        for item in temp:
            pos =temp.index(min(temp))  # pos is position of min in new L
            NewList.append(temp.pop(pos)) # min from L appends to NewList

    return(NewList) #return a value
    

def sortwithoutloops(input):
    """sorts a list using sort function
    returns a sorted list"""
    
    temp = input[:] 
    temp.sort()
    return(temp) #return a value

def searchwithloops(input, value):
    """determines if value is in list using loop
    returns true or false"""
    
    test = False  # Set test to false
    for item in L:
        if item == value: #compare each item if found break
            test = True
            break
    return(test) #return a value

def searchwithoutloops(input, value):
    """determines if value is in list using 'in'
    returns true or false"""
    
    test = value in input
    return(test) #return a value	

def searchwithnp(input, value):
    return(np.any(input == value))

'''
#--------------------------------------------------
# Part one : Sorting and Searching using numpy
#--------------------------------------------------
### Model

if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]
    input = np.array(L)
    print "Sort and search using numpy functions"
    print "Array to process: ", input
    print "\n"
    print "Output using numpy.sort"
    print np.sort(input)
    print "Searching for 5 using numpy.where: "
    print searchwithnp(input,5)
    print "Searching for 5 using numpy.where: "
    print searchwithnp(input, 11)
    print "\n"
#--------------------------------------------------
#  Part two :comparing numpy, loops, and base functions
#--------------------------------------------------    
    
    import timeit
   
    n = 10000
    tloop = timeit.Timer("x = copy.copy(L); sortwithloops(x)", setup = setup)
    tbase = timeit.Timer("x =copy.copy(L); sortwithoutloops(x)", setup = setup)
    tnp = timeit.Timer("x =copy.copy(input); np.sort(x)", setup = setup)
    tloop2 = timeit.Timer("x =copy.copy(L); searchwithloops(x,5)", setup = setup)
    tbase2 = timeit.Timer("x =copy.copy(L); searchwithoutloops(x,5)", setup = setup)
    tnp2 = timeit.Timer("x =copy.copy(input); searchwithnp(x,5)", setup = setup)
    tloop3 = timeit.Timer("x =copy.copy(L); searchwithloops(x,11)", setup = setup)
    tbase3 = timeit.Timer("x =copy.copy(L); searchwithoutloops(x,11)", setup = setup)
    tnp3 = timeit.Timer("x =copy.copy(input); searchwithnp(x,11)", setup = setup)
    print "Compare time using numpy, loops, and base functions"
    print "Itterations: ", n
    
    print "Sorting: "
    print "     with loops: ", tloop.timeit(n)
    print "     with base function .sort : ", tbase.timeit(n)
    print "     with numpy.sort: ", tnp.timeit(n)
    print "\n"
    print "Searching for something that exists (5) : "
    print "     with loops: ", tloop2.timeit(n)
    print "     with base function in : ", tbase2.timeit(n)
    print "     with numpy.where: ", tnp2.timeit(n)
    print "\n"
    print "Searching for something that doesn't exist (11) : "
    print "     with loops: ", tloop3.timeit(n)
    print "     with base function in : ", tbase3.timeit(n)
    print "     with numpy.where: ", tnp3.timeit(n)
    print "\n"
  
    #--------------------------------------------------
    #  Part two again : with larger data set
    #  comparing numpy, loops, and base functions
    #--------------------------------------------------    
   
    n = 100
    tloop = timeit.Timer("x = copy.copy(L); sortwithloops(x)", setup = setup2)
    tbase = timeit.Timer("x =copy.copy(L); sortwithoutloops(x)", setup = setup2)
    tnp = timeit.Timer("x =copy.copy(input); np.sort(x)", setup = setup2)
    tloop2 = timeit.Timer("x =copy.copy(L); searchwithloops(x,5)", setup = setup2)
    tbase2 = timeit.Timer("x =copy.copy(L); searchwithoutloops(x,5)", setup = setup2)
    tnp2 = timeit.Timer("x =copy.copy(input); searchwithnp(x,5)", setup = setup2)
    tloop3 = timeit.Timer("x =copy.copy(L); searchwithloops(x,16)", setup = setup2)
    tbase3 = timeit.Timer("x =copy.copy(L); searchwithoutloops(x,16)", setup = setup2)
    tnp3 = timeit.Timer("x =copy.copy(input); searchwithnp(x,16)", setup = setup2)
    print "Compare time using numpy, loops, and base functions"
    print "With larger data set of 5000 values"
    print "Itterations: ", n
    
    print "Sorting: "
    print "     with loops: ", tloop.timeit(n)
    print "     with base function .sort : ", tbase.timeit(n)
    print "     with numpy.sort: ", tnp.timeit(n)
    print "\n"
    print "Searching for something that exists (5) : "
    print "     with loops: ", tloop2.timeit(n)
    print "     with base function in : ", tbase2.timeit(n)
    print "     with numpy.where: ", tnp2.timeit(n)
    print "\n"
    print "Searching for something that doesn't exist (16) : "
    print "     with loops: ", tloop3.timeit(n)
    print "     with base function in : ", tbase3.timeit(n)
    print "     with numpy.where: ", tnp3.timeit(n)
    print "\n"

