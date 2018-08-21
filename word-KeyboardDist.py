#--- Distance of letters in Keyboard ---#
    

qwerty = [['q','w','e','r','t','y','u','i','o','p'],
          ['a','s','d','f','g','h','j','k','l','ç'],
          ['z','x','c','v','b','n','m']]

def keyboard_dist(keyboard):
    
    ans = []
    
    for line in keyboard:
        for letter in line:
            ans.append([letter, []])
    
    #find distance between letters
    #append into ans
    
    return ans
