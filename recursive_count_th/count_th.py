'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if the length of the word is less then 2 then it does not contain 'th'
    if len(word) < 2: # base case
        return 0
    else:
        # checking to see if theres an occurence of 'th'
        if word[0] == 't' and word[1] == 'h':
            # recursive call to keep checking the word for 'th'
            return 1 + count_th(word[1:])
        else:
            return count_th(word[1:])
