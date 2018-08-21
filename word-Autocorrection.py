import time as t


#--- Word Autocorrection using Levenshtein Distance ---#


def autocorrect(string, keyboard):
    start = t.time()
    
    #--- reading txt common_words_usa.txt (with 10000 words) ---#
    
    file = "common_words_usa2.txt"
    f = open(file)
    data = f.readlines()
    f.close()
    data = map(lambda s: s.strip(), data)
    
    #--- getting all similar words (with one edit distance) ---#
    
    ans = [] 
    for word in data:
        if len(string) - len(word) < 2:                 #--- we optimize by avoid doing Levenshtein for all string ---#
            value = levenshtein(string, word)
            if value < 2 and value != 0:                #--- it cannot recommend the string itself ---#
                if len(string) == len(word):            #--- if they have the same lenght, we will see the distance between different letters on the keyboard ---#
                    for i in range(len(string)):
                        if string[i] != word[i]:
                            if keyboard_dist(keyboard, string[i], word[i]) < 2:
                                ans.append(word)
                else:
                    ans.append(word)
                    
    return ans, t.time() - start







#--------------------------------------------------#

#--- Word Autocorrection using Levenshtein Distance ---#

#--- return order of preference ---#
    
def preference(string, data):
    if string in data:
        return data.index(string)
    else:
        return 1

#--- ---#

def autocorrect(string):
    start = t.time()
    
    #--- alphabet search =---#
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
                'm','n','o','p','q','r','s','t','u','v','w','x',
                'y','z']
    
    #--- reading corpus.txt (a literature text) and reading the 10000 most common words in english usa ---#
    
    file = "corpus.txt"
    f = open(file)
    data = f.read().split(' ')
    f.close()
    data = map(lambda s: s.strip(), data)
    data = list(map(lambda k: k.lower(), data))
    
    file2 = "common_words_usa.txt"
    g = open(file2)
    data2 = g.readlines()
    g.close()
    data2 = map(lambda s: s.strip(), data2)
    data2 = list(map(lambda k: k.lower(), data2))
    
    #--- getting all similar words (with one edit distance) ---#
   
    possibilities = []
    
    #--- adding a letter ---#
    for i in range(len(string)):
        for letter in alphabet:
            word = string[:i] + letter + string[i:]
            if word in data:
                if word not in possibilities:
                    possibilities.append(word)
                
    #--- removing a letter ---#
    for i in range(len(string)+1):
        word = string[:i] + string[i+1:]
        if word in data:
            if word not in possibilities:
                possibilities.append(word)
            
    #--- substitute a letter ---#
    for i in range(1, len(string)+1):
        for letter in alphabet:
            if letter != string[i-1]:
                word = string[:i-1] + letter + string[i:]
                if word in data:
                    if word not in possibilities:
                        possibilities.append(word)
    
    #--- switching adjacents letters ---#
    perm = list(it.permutations(string[2:]))
    for word in perm:
        aux = string[:2]
        for letter in word:
            aux += letter
        if aux in data:
            if aux not in possibilities:
                possibilities.append(aux)
    
    
    return sorted(possibilities, key=lambda i: preference(i, data2))[-1::-1], t.time() - start
