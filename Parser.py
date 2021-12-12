import re

#Validate and Parse user input
def parseEquation(equation):
    equation=equation.replace(" ", "")
    isValidEquation=re.fullmatch('(\d+[+\-*\/^]{1}|X[+\-*\/^]{1})*(\d+|X){1}',equation,re.IGNORECASE)
    if(not isValidEquation):
        raise TypeError("Equation Must be of X with + - / * ^ operators only")

    #replace power operator to be ** instead of the ^ user added
    equation = equation.replace("^", "**")
    #replace X to x to be valid for matplotlib.pyplot
    equation = equation.replace("X","x")


    #return equation after validating it
    return equation

def validInt(num):
    if (not re.fullmatch('\-*[0-9]+', num)):
        raise TypeError("Value of X must be an integer")
    return int(num)