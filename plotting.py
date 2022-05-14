import matplotlib.pyplot as plt
import seaborn as sns
from os import path


def maxAndShow():
    try:
        #this maximizes the plot to fullscreen and displays it
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()
    except:
        plt.show()




class GDPPlotter:

    def __init__(self):
        self = self

    #plotting
    def GDPplot(self, data, areaOrPop, scale):

        #if area
        if(areaOrPop=="0"):
            #create a logarithmic regression plot, with the datapoints included.
            plot = sns.lmplot(data=data, y="GDP per capita", x="Area", logx=True)
            plt.xlabel('Area (km^2)')
            plt.ylabel('GDP per capita ($)')
            plt.xscale("log")

            #lin-log scale
            if(scale=="0"):
                #plot area data on lin-log scale and save as png
                plt.title('GDP per capita in relation to country area (lin-log)')
                plot.savefig(path.join(path.dirname(__file__), "Results/AreaLinLog.png"))

            #log-log scale
            else:
                #plot area data on logarithmic scale and save as png
                plt.title('GDP per capita in relation to country area (log-log)')
                plt.yscale("log")
                plot.savefig(path.join(path.dirname(__file__), "Results/AreaLogarithm.png"))

        #if population
        else:
            plot = sns.lmplot(data=data, y="GDP per capita", x="Population", logx=True)
            plt.xlabel('Population')
            plt.ylabel('GDP per capita ($)')
            plt.xscale("log")

            #lin-log scale
            if(scale=="0"):
                #plot data on lin-log scale and save as png
                plt.title('GDP per capita in relation to country population (lin-log)')
                plot.savefig(path.join(path.dirname(__file__), "Results/PopLinLog.png"))

            #log-log scale
            else:
                #plot data on logarithmic scale and save as png
                plt.title('GDP per capita in relation to country population (log-log)')
                plt.yscale("log")
                plot.savefig(path.join(path.dirname(__file__), "Results/PopLogarithm.png"))


        maxAndShow()


class growthPlotter:

    def __init__(self):
        self = self

    def growthPlot(self, data, areaOrPop):

        #create a logarithmic regression plot
        plot = sns.lmplot(data=data, y="Growth per year (%)", x="2017", logx=True)
        plt.title('GDP per capita in relation to country size')
        
        if(areaOrPop=="0"):
            plt.xlabel('Area (km^2)')
        else:
            plt.xlabel('Population')

        plt.ylabel('GDP per capita growth per year($). Years: 1990 to 2017')
        plt.xscale("log")

        #plot area data on lin-log scale and save as png
        plot.savefig(path.join(path.dirname(__file__), "Results/GrowthToSize.png"))
        
        
        maxAndShow()