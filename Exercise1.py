def trifeca(word):

    index = 0
    rr = False
    if(len(word) < 6):
        return False

    for letter in word :
        if index < len(word)-5:
            if word[index] == word[index + 1] and word[index+2]== word[index+3] and word[index+4]==word[index+5]:
                rr = True
            index += 1

    return rr
        




res = trifeca("jhiaabbcc")
print(res)
