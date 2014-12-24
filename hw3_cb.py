# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 20:40:22 2014

@author: Cheryl
"""
import pandas as pd
import Tkinter
import tkFileDialog
import pandas as pd
    
def readfile():
    """open dialog to pick file, reads csv file into data
    returns false if file cannot be read"""
    root = Tkinter.Tk()  
    root.withdraw()
    filename = tkFileDialog.askopenfilename(parent = root, 
                                            filetypes=[("Text files","*.csv")])
    try:
        f = pd.read_csv(filename)
        return(f)
    except:
        return(False)
        

def printsort (df, col, asc, num, tail):
    """prints out the specified number of rows sorted by the column provided
    agrs:
        col: the name of the col sorted on
        df: data
        asc: true for ascending, false for dec
        num: number of rows to return"""  
    s = df[col].apply(lambda x: mapvalues(x))
    df['sorter'] = s
    dfsort = df.sort(columns = 'sorter', ascending = asc)
    if num == "All":
        print(dfsort)  
    elif tail == True:
        print(dfsort.tail(num))
    else:
        print(dfsort.head(num))
    return()


def mapvalues(x):
    """maps x from sorting columns to key in trans dictionary
    try except if item is not mapped in trans dict
    args: x - a single value of x"""
    try: 
        int(x)
    except:     
        try:
            z = trans[x]
        except:
            print("Found a value that is not a valid entry for sorting: ", x)
            print ("valid entry pairs:")
            print(trans)
            add = raw_input("Would you like to add it? Y or N, E to exit -->")
            if add == 'E':
                exit
            if add == "Y":
                val = raw_input("What numeric value should this have? -->")
                trans[x] = val
                z = val
            else:
                z = x
    else:
        z = x
    return(z)


def filterhigh(dfcars):
    '''filter df for high, input is df'''
    regex = "\s*v*[hH]igh"
    d = dfcars[dfcars['price_buy'].str.contains(regex) &
    dfcars['price_maint'].str.contains(regex) &  
    dfcars['safety'].str.contains(regex)]
    printsort(d, 'doors', True, False, 'All')
    
 
def filterB(dfcars):
    '''filter df for high, input is df'''
    regex = "\s*[vV][hH]igh"
    regex2 = "\s*[mM]ed"
    regex3 = "\s*4?[5a-zA-Z]*"
    d = dfcars[dfcars['price_buy'].str.contains(regex) |
    dfcars['price_maint'].str.contains(regex2) |
    dfcars['doors'].str.contains('4') |
    dfcars['persons'].str.contains(regex3)]
    return(d)
    
    
def userinput(dfcars):
    '''get user input for sort'''
    coln = raw_input("Enter column name to sort -->")
    ascn = raw_input("Sort asc? T or F -->")
    numn = raw_input("Enter the number or rows -->")
    tailn= raw_input("Pull tail instead? T or F -->")
    if tailn == "T":
        tailn = True
    else:
        ascn = False
        
    if ascn == "T":
        ascn = True
    else:
        ascn = False
        
    if numn != "All":
        numn = int(numn)
    
    if coln not in colnames:
        print("cannot sort on that column name")
        exit
    return(dfcars, coln, ascn, numn, tailn)

    
    
    print('\n')
    return()
#--------------------------------------------------
# Main Body
#--------------------------------------------------

#reads into a data frame
dfcars = readfile()
if dfcars.empty:
    print "Error reading file"
    exit()
    

#give data col names: 
colnames = ['price_buy', 'price_maint', 'doors', 'persons', 'trunk',
                'safety', 'class']
dfcars.columns = colnames
dfcars.index.name = 'row'


#translate
trans = {'vhigh':4, 'high':3, 'med':2, 'low':1, 'small':1, 
         'big': 3, '5-more':5, 'more': 5, '5more': 5}


#show summary
print("Data Header")
print(dfcars.head(5))
print('\n')

coln = "safety"
ascn = False
numn = 10
tailn = False
print("top 10 sorted by safety descending")
printsort(dfcars, coln, ascn, numn, tailn)
print('\n')

coln = "price_maint"
ascn = True
numn = 15
tailn = True
print("bottom 15 sorted by maintenece cost , dec")
printsort(dfcars, coln, ascn, numn, tailn)
print('\n')

#user input 


#specific filter & sort
filterhigh(dfcars)

#get save file name
savename = "C:\Users\Cheryl\Documents\GitHub\AdvProg\Gottobe.betterway.csv"
try:
    filterB(dfcars).to_csv(savename)
except:
    print("can't save this file, do you have it open?")

printsort(*userinput(dfcars))
            
    
    