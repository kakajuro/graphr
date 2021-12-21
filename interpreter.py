from os import error
import sys
from random import choice

from util.createGraph import createGraph
from util.prepTerm import prepTerm

fileExtension="graphr"
sysArgs = sys.argv

colourArray = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']
commands = ["OPTIONS", "EQUATION", "COLOUR", "COLOR", "RANGE", "TITLE", "SCREENSHOT", "SHOW"]

try:
    if sysArgs[1].split('.')[1] == fileExtension:
        readable = True
    else:
        errorMsg = "Must be .graphr file to run."
        raise Exception(errorMsg)
except IndexError:
    errorMsg = "Specify a .graphr file to run"
    raise Exception(errorMsg)

for file in sysArgs:

    graphToolbar = ""
    graphWarnings = ""

    graphID = 0
    graphTitle = ""
    graphScreenshotName = ""
    graphRun = ""
    graphLower, graphUpper = 0, 0
    graphColour = ""
    graphEquation = ""

    if sysArgs.index(file) == 0:
        pass
    else:
        with open('./' + str(file)) as f:
            lineCount = 0

            graphID = sysArgs.index(file)

            for line in f:
                notCommand = 0
                lineCount += 1

                line = line.replace('\n','')
                keywords = line.split(' ')

                for command in commands:
                    if not keywords[0] == command:
                        notCommand += 1

                if line == "" or line == " ":
                    pass
                elif keywords[0].startswith('$'):
                    pass
                elif notCommand == len(commands):
                    errorMsg = f"Line {lineCount}: Command '{line}' not recognised."
                    raise Exception(errorMsg)

                if keywords[0] == "OPTIONS":
                    if keywords[1] == "TOOLBAR":
                        try:
                            if keywords[2] == "":
                                errorMsg = f"Line {lineCount}: No argument provided for {keywords[1]}."
                                raise Exception(errorMsg)
                            elif keywords[2] == "SHOW":
                                graphToolbar = "show"
                            elif keywords[2] == "HIDE":
                                graphToolbar = "hide"
                            else:
                                errorMsg = f"Line {lineCount}: Command '{keywords[2]}' not recognised."
                                raise Exception(errorMsg)
                        except IndexError:
                            errorMsg = f"Line {lineCount}: No argument provided for {keywords[1]}."
                            raise Exception(errorMsg)
                    elif keywords[1] == "WARNINGS":
                        try:
                            if keywords[2] == "":
                                errorMsg = f"Line {lineCount}: No argument provided for {keywords[1]}."
                                raise Exception(errorMsg)
                            elif keywords[2] == "SHOW":
                                graphWarnings = "show"
                            elif keywords[2] == "HIDE":
                                graphWarnings = "hide"
                            else:
                                errorMsg = f"Line {lineCount}: Command '{keywords[2]}' not recognised."
                                raise Exception(errorMsg)
                        except IndexError:
                            errorMsg = f"Line {lineCount}: No argument provided for {keywords[1]}."
                            raise Exception(errorMsg)
                    elif keywords[1] == "" or keywords[1] == " ":
                        errorMsg = f"Line {lineCount}: No argument provided for {keywords[0]}."
                        raise Exception(errorMsg)
                    else:
                        errorMsg = f"Line {lineCount}: Command '{keywords[1]}' not recognised."
                        raise Exception(errorMsg)

                if keywords[0] == "EQUATION":
                    try:
                        eqString = ''

                        for keyword in keywords:
                            if keyword == keywords[0]:
                                pass
                            else:
                                term = prepTerm(keyword)
                                eqString += term

                        graphEquation = eqString

                    except IndexError:
                        errorMsg = f"Line {lineCount}: No argument provided for {keywords[0]}."
                        raise Exception(errorMsg)

                if keywords[0] == "COLOUR" or keywords[0] == "COLOR":
                    try:

                        if keywords[1] == "" or keywords[1] == " ":
                            errorMsg = f"Line {lineCount}: No argument provided for {keywords[0]}."
                            raise Exception(errorMsg)

                        colourFound = False

                        for colour in colourArray:
                            if keywords[1] == colour:
                                graphColour = colour
                                colourFound = True
                            elif keywords[1].startswith('#') and len(keywords[1]) == 7:
                                graphColour = keywords[1]
                                colourFound = True
                            elif keywords[1].startswith('#') and len(keywords[1]) == 4:

                                graphColour = keywords[1]
                                colourFound = True
                        if colourFound:
                            pass
                        else:
                            errorMsg = f"Line {lineCount}: Argument '{keywords[1]}' not recognised."
                            raise Exception(errorMsg)

                    except IndexError:
                        raise Exception(errorMsg)
                        errorMsg = f"Line {lineCount}: Not enough arguments provided for {keywords[0]} command."

                if keywords[0] == "RANGE":
                    try:
                        if keywords[1] == "" or keywords[1] == " " or keywords[2] == "" or keywords[2] == " ":
                            errorMsg = f"Line {lineCount}: Range values must be digits."
                            raise Exception(errorMsg)

                        if keywords[1].lstrip('+-').isdigit() and keywords[2].lstrip('+-').isdigit():
                            graphLower = keywords[1]
                            graphUpper = keywords[2]
                        else:
                            errorMsg = f"Line {lineCount}: Arguments for {keywords[0]} must be digits."
                            raise Exception(errorMsg)

                    except IndexError:
                        errorMsg = f"Line {lineCount}: Not enough arguments provided for {keywords[0]} command."
                        raise Exception(errorMsg)

                if keywords[0] == "TITLE":
                    try:
                        titleString = ""

                        if keywords[1] == "" or keywords[1] == " ":
                            errorMsg = f"Line {lineCount}: No argument provided for {keywords[0]}."
                            raise Exception(errorMsg)
                        elif keywords[1] == "NONE":
                            pass
                        else:
                            for kw in keywords[1:]:
                                word = kw+" "
                                titleString+=word

                        titleString[-1:].replace(" ", "")
                        graphTitle = titleString
                    except IndexError:
                        errorMsg = f"Line {lineCount}: No argument provided for {keywords[0]}."
                        raise Exception(errorMsg)

                if keywords[0] == "SCREENSHOT":
                    try:
                        screenshotString = ""

                        if keywords[1] == "" or keywords[1] == " ":
                            errorMsg = f"Line {lineCount}: No argument provided for {keywords[0]}."
                            raise Exception(errorMsg)
                        elif keywords[1] == "NONE":
                            pass
                        else:
                            for kw in keywords[1:]:
                                word = kw+" "
                                screenshotString+=word

                        screenshotString = screenshotString[:-1]
                        graphScreenshotName = screenshotString
                    except IndexError:
                        errorMsg = f"Line {lineCount}: No argument provided for {keywords[0]}."
                        raise Exception(errorMsg)

                if keywords[0] == "SHOW":
                    graphRun = "y"

            createGraph(graphID, graphToolbar, graphTitle, graphScreenshotName, graphRun, int(graphLower), int(graphUpper), graphColour, graphEquation)

if graphEquation == "":
    errorMsg = f"No equation specified."
    raise Exception(errorMsg)
  
if graphLower == "" or graphUpper == "":
    errorMsg = f"No range specified."
    raise Exception(errorMsg)

if graphWarnings == "show" or graphWarnings == "":
    if graphColour == "":
        print("Warning: No colour specified so a random one has been picked.")
        graphColour = choice(colourArray)

    if graphTitle == "":
        print("Warning: No title specified.")
