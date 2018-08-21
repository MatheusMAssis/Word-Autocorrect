#--- Distance of letters in Keyboard ---#
    

qwerty = [['q','w','e','r','t','y','u','i','o','p'],
          ['a','s','d','f','g','h','j','k','l','ç'],
          ['z','x','c','v','b','n','m']]

def keyboard_dist(keyboard, letter1, letter2):
    
    for i in range(len(keyboard)):
        if letter1 in keyboard[i]:
            i1, j1 = i, keyboard[i].index(letter1)    #--- coordinates of letter1 ---#
        if letter2 in keyboard[i]:
            i2, j2 = i, keyboard[i].index(letter2)    #--- coordinates of letter2 ---#
            
    return abs(i2 - i1) + abs(j2 - j1)
