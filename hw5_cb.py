# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 18:51:34 2014

@author: Cheryl
Assignment # 5
"""

import pandas as pd
import Tkinter
import tkFileDialog

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
        
def simplelm(x,y):
    """calcuates simple linear model for given x, y
    returns b_hat and a as a list, with r squar value
    for y = b_hat(x) + a"""
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)
    b_hat =  sum((x -mean_x) * (y - mean_y))/sum((x-mean_x)**2)
    a = mean_y - b_hat*mean_x
    y_hat = b_hat*x +a
    ssres = sum((y - y_hat)**2)
    sstot = sum((y - mean_y)**2)
    rsqr = 1 - ssres/sstot
    model = [b_hat, a, rsqr]
    return(model)
    
#--------------------------------------------------
# Main Body
#--------------------------------------------------
### Model
    
dfbrains = readfile()

colnames = ['animal', 'body', 'brain']
dfbrains.columns = colnames
x = dfbrains['body']
y = dfbrains['brain']

lm = simplelm(x,y)
print('Linear model for brain as predicted by body size')
print('including all data:')
print ('y = ', lm[0], ' * x + ', lm[1])
print('r squared value: ', lm[2])
result = """This model is confusing, as it seems to be saying that brain size is
only slightly related to body size"""
print(result)
print('\n')
print('\n')

### exclude the dinos
df_nodinos = dfbrains[dfbrains['body'] < 9400]

x = df_nodinos['body']
y = df_nodinos['brain']

lm = simplelm(x,y)
print('The linear model for brain as predicted by body size')
print('excluding the three dinosaurs makes a lot more sense')
print ('y = ', lm[0], ' * x + ', lm[1])
print('r squared value: ', lm[2])
print('\n')
print('\n')


