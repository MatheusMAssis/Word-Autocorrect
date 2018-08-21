import time as t

#--- ---#
    
def different_letters(str1, str2, keyboard):  #--- keyboard is used just to have a alphabet ---#
    ans = {}
    res = []
    for line in keyboard:
        for letter in line:
            if letter != None:
                ans[letter] = 0
                
    for letter in str1:
        ans[letter] = 1
        
    for letter in str2:
        if ans[letter] == 1:
            ans[letter] = -1
        else:
            ans[letter] = 2
    
    for letter in ans:
        if ans[letter] != 0 and ans[letter] != -1:
            res.append(letter)
    
    return res


#--- Word Recommendation using Levenshtein Distance ---#


def recommendation(string):
    start = t.time()
    
    #--- reading txt common_words_usa.txt (with 10000 words) ---#
    
    file = "common_words_usa.txt"
    f = open(file)
    data = f.readlines()
    f.close()
    data = map(lambda s: s.strip(), data)
    
    #--- getting all similar words (with one edit distance) ---#
    
    ans = [] 
    for word in data:
        if len(string) - len(word) < 2: #--- we optimize by avoid doing Levenshtein for all string ---#
            value = levenshtein(string, word)
            if value < 2 and value != 0: #--- it cannot recommend the string itself ---#
                ans.append(word)
    return ans, t.time() - start
