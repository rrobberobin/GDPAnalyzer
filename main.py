import pandas as pd
from os import path
from paths import paths
import plotting
import dataHandler
from errorCheck import errorChecker

def main():

    print("\nWelcome! This program displays GDP per capita data of different countries.",
    "It compares the data to the population and to the area of the country.",
    "It also calculates the GDP per capita growth through the years")

    GDPOrGrowth = input("\nEnter 0 for GDP per capita growth. Enter any other key for GDP per capita\n")
    PPPOrNot = input("\nEnter 0 for normal GDP. Enter any other key: PPP will be used.\n")

    if(PPPOrNot=="0"):
        #import gdp per capita PPP data by country
        GDP_Path = path.join(path.dirname(__file__), paths.GDPPerCapitaPPP)
    else:
        #import gdp per capita data by country
        GDP_Path = path.join(path.dirname(__file__), paths.GDPPerCapita)

    GDP_Data = pd.read_csv(GDP_Path, header=2)  #import GDP data from file

    #import gdp metadata
    GDPMetaPath = path.join(path.dirname(__file__), paths.GDPMeta)
    GDPMetaData = pd.read_csv(GDPMetaPath)  #import GDP meta data. We need it for the sole purpose of filtering out aggregates.
    GDPMetaData = GDPMetaData.loc[GDPMetaData["Region"].notna(), :] #filter out aggregates. Aggregates have no "region" data, that's why we're using ".notna" command

   
    #merge the data and metadata. Here aggregates disappear, because when merging, extra rows are removed.
    GDP_Data = GDP_Data.merge(GDPMetaData, left_on="Country Code", right_on="Country Code")


    areaOrPop = input("\nCompare GDP to area or population. Enter 0 for area. Enter any other key: population will be used\n")
    if(areaOrPop == "0"):
        #import areal data
        areaOrPopPath = path.join(path.dirname(__file__), paths.area)

    else:
        #import population data by country
        areaOrPopPath = path.join(path.dirname(__file__), paths.pop)

    sizeData = pd.read_csv(areaOrPopPath, header=2)  #import area/pop data from file



    if(GDPOrGrowth == "0"):
        #calculate growth rates and combine them with sizeData
        combined = dataHandler.growthData(GDP_Data, sizeData).calculate()

        #create a plot and display it
        plotting.growthPlotter().growthPlot(combined, areaOrPop)


    else:

        #prompt for a year until we get a valid year
        while True:
            #choose the year to use for analysis
            year = input("""\nEnter year. The year needs to be a number between 1960 and 2020.
All countries do not have data for all years. Best data availability is between 1990 and 2017\n""")

            try:
                errorChecker(year).errorCheck()
                break
            except Exception as e:
                print(e)


        #remove excess data and years
        sizeData = sizeData.loc[:,["Country Name", year]]

        scale = input("\nEnter 0 for lin-log scale. Enter any other key: log-log scale will be used\n")

        #combine data using GDPData class in dataHandler
        combined = dataHandler.GDPData(GDP_Data, sizeData, areaOrPop, year).combine()

        #plot GDP and size
        plotting.GDPPlotter().GDPplot(combined, areaOrPop, scale)




if __name__ == "__main__":
    main()




