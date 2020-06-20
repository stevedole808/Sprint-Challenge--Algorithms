'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # length must be greatet then two because "th" is the base value
    if len(word) < 2:
        return 0
    else:
        # check to see if index 0,1 is == "th"
        if word[0] == "t" and word[1] == "h":
        # if so add one 
        # recurse to check all values on right side after the 1st index has been removed
            return 1 + count_th(word[1:])
        else:
        # recurse till theres no occurences 
            return count_th(word[1:])

