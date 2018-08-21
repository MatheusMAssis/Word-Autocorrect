import numpy as np

#--- Levenshtein Distance between two strings ---#

def levenshtein(str1, str2):
    
    m, n = len(str1), len(str2)
    cost = 0
    
    if not m:
        return n      #--- m = "", n = some string ---#
    elif not n:
        return m      #--- n = "", m = some string ---#
    else:
        
        #--- creating work array ---#
        
        arr = np.array([[0 for j in range(n + 1)] for i in range(m + 1)])
        arr[0] = np.array([k for k in range(n + 1)])
        for k in range(m + 1):
            arr[k][0] = k
        
        #--- updating array ---#
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1].lower() == str2[j - 1].lower():
                    cost = 0
                else:
                    cost = 1
                arr[i][j] = min([arr[i-1][j] + 1,
                                 arr[i][j-1] + 1,
                                 arr[i-1][j-1] + cost])
        
    return arr[m][n]
