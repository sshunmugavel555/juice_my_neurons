# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:19:39 2021

@author: sshunmugavel

"""

def revrev(to_rev):
    
    """ This function reverses the words in the input string.
    However it maintains the order of the words as in the input """
    
    revList=[]  # define an empty list
    
    inpList=to_rev.split() # Split the input sentence into a list of words
    
    for each_word in inpList: # Loop through the list of words
        
        ewList=list(each_word) # Make a list of characters of each word
        
        revStr=''.join(ewList[::-1]) # Reverse the characters of each word
        
        revList.append(revStr) # Append the empty list with the reversed words
        
    return ' '.join(revList) # return the reversed string

print(revrev("The quick brown fox"))
print(revrev("My name is Shankar"))

