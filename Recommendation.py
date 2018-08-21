import time as t

def Recommendation(string):
    start = t.time()
    
    #--- reading txt common_words_usa.txt (with 10000 words) ---#
    
    file = "common_words_usa.txt"
    f = open(file)
    data = f.readlines()
    f.close()
    data = map(lambda s: s.strip(), data)
    
    #--- getting the first 10 (or less) similar words ---#
    
    ans = [] 
    for i in data:
        if len(string) - len(i) < 2: #--- we optimize by avoid doing Levenshtein for all string ---#
            value = Levenshtein(string, i)
            if value < 2 and value != 0: #--- it cannot recommend the string itself ---#
                ans.append(i)
            if len(ans) > 10:
                return ans, t.time() - start
    return ans, t.time() - start
