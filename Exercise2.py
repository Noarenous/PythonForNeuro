def palindrome(number):
    word = str(number)
    index=0
    ans = True
    for letter in word:
        if word[index] != word[len(word)-1-index]:
            ans= False
        index += 1

    return ans


def check_palindrome():
    for i in range(100000,999999,1):
        digit4 = i % 10000
        digit5 = (i+1) % 100000
        digitmiddle= (i+2) % 100000
        digitmiddle4= int(digitmiddle/10)
        digitfinal= i+3

        if palindrome(digit4) and palindrome (digit5) and palindrome (digitmiddle4) and palindrome(digitfinal):
            print(i)
    
check_palindrome()

        