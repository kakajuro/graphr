import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def createGraph(id=None, toolbar=None, title=None, screenshotName=None, graphRun=None, graphLower=None, graphUpper=None, graphColour=None, graphEquation=None):

    if toolbar == "show":
         pass
    elif toolbar == "hide":
        mpl.rcParams['toolbar'] = 'None'
    else:
        pass

    fig = plt.figure(id)
    ax = fig.add_subplot(111)
    ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    if title:
        ax.set_title(title)

    x = np.linspace(graphLower, graphUpper, 100)
    y = eval(graphEquation)

    plt.plot(x, y, graphColour)

    if screenshotName:
        plt.savefig(f"{screenshotName}.png")

    print(f"Figure {id} created.")

    if graphRun:
        print(f"Figure {id} displayed.")
        plt.show()
    else:
        pass
