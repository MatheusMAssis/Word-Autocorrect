#--- Distance of a point to all others in a matrix ---#

def matrix_distance(matrix, initial):
    ...

#--- Distance of letters in Keyboard ---#
    

qwerty = [['q','w','e','r','t','y','u','i','o','p'],
          ['a','s','d','f','g','h','j','k','l','ç'],
          ['z','x','c','v','b','n','m',None,None,None]]

def keyboard_dist(keyboard):
    
    ans = {}
    
    for line in keyboard:
        for letter in line:
            if letter != None:
                ans[letter] = {}
            
    #find distance between letters
    #append into ans
    
    return ans
