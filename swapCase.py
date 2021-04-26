def swap_case(s):
    """ Function swaps the case of the input string """
    
    newS=""
    
    for eC in s:
        
       if ord(eC) >= 97 and ord(eC) <= 122:
        
            newS+=eC.upper()
            
       elif ord(eC) >= 65 and ord(eC) <= 90:
        
            newS+=eC.lower()
        
       else :
        
            newS+=eC
            
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
