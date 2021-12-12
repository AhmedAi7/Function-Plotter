import matplotlib.pyplot as plt
import numpy as np

class GraphPlotter :

    def __init__(self):
        self.minX= None
        self.maxX= None
        self.equation= None
        self.plottEquation = False #if False => plott X and Y axises only

    def plott(self):
        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        if not self.plottEquation: #if plottEquation is false -> plot the axises only
            return fig

        # 100 linearly spaced numbers
        x = np.linspace(self.minX,self.maxX,100)

        # eval the equation that the user entered
        ast= eval(self.equation)
        # Y = equation
        y = ast

        # plot the function
        plt.plot(x, y)
        return fig
