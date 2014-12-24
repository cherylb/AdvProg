#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
zz
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
    

#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input):
    """sorts a list using sort function
    returns a sorted list"""
    
    temp = input[:] 
    temp.sort()
    return(temp) #return a value


#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    """determines if value is in list using loop
    returns true or false"""
    
    test = False  # Set test to false
    for item in L:
        if item == value: #compare each item if found break
            test = True
            break
    return(test) #return a value


#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    """determines if value is in list using 'in'
    returns true or false"""
    
    test = value in input
    return(test) #return a value	


if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]
    input = L
    print sortwithloops(input)  # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(input) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(input, 5) #true
    print searchwithloops(input, 11) #false
    print searchwithoutloops(input, 5) #true
    print searchwithoutloops(input, 11) #false
