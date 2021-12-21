import re

def splitit(word):
    return [char for char in word]

def prepTerm(term):

    if term.startswith('-'):
        term = term[1:]
        plus = 0
    else:
        plus = 1

    term = term.replace(" ", "").replace("^", "**")

    if len(term) > 4 and "x**" in term:
        finishTerm = 1
        charsToRemove = len(term) - 4
    else:
        finishTerm = 0

    digThenNum = r'\d[x]'
    digNumTerm = re.findall(digThenNum, term)

    for foundTerm in digNumTerm:
        currentTerm = str(foundTerm)
        splitTerm = splitit(currentTerm)
        splitTerm.insert(1, '*')

        joinedTerm = ''.join([str(split) for split in splitTerm])

        if finishTerm:
            term = joinedTerm + term[charsToRemove+1:]
        else:
            term = term.replace("x", "") + joinedTerm[-2:]

    if plus:
        term = '+' + term
    elif plus == 0:
        term = '-' + term

    return term
