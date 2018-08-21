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
