import pandas as pd
from os import path



#for comparing GDP per capita
class GDPData:

    def __init__(self, GDPdata, sizeData, areaOrPop, year):
        self = self
        self.GDPdata = GDPdata
        self.sizeData = sizeData
        self.areaOrPop = areaOrPop
        self.year = year
        self.combine()

    #creates a dataFrame by merging the GDP and area/pop dataFrames. It saves the data into a csv file and finally returns the dataFrame.
    def combine(self):

        GDPdata = self.GDPdata
        sizeData = self.sizeData
        areaOrPop = self.areaOrPop
        year = self.year

        #create a dataframe with the population and gdp per capita of the chosen year. The year can be changed
        RecentGDP = GDPdata.loc[:, ["Country Name", year]]
        combined = RecentGDP.merge(sizeData, left_on="Country Name", right_on="Country Name")

        if(areaOrPop=="0"):
            combined.columns = ["Country", "GDP per capita", "Area"]    #if we have areas
        else:
            combined.columns = ["Country", "GDP per capita", "Population"]  #if we have populations

        #save to file
        resultPath = path.join(path.dirname(__file__), "Results/countryData.csv")
        combined.to_csv(resultPath, index=False)

        return combined




#for comparing growth rates
class growthData:


    def __init__(self, data, sizeData):
        self = self
        self.data=data
        self.sizeData = sizeData
        self.calculate()


    #calculate growth rates, save them into a csv file and return the dataFRame which contains the growth rates
    def calculate(self):

        data = self.data
        sizeData = self.sizeData
        startYear = 1990
        endYear = 2017

        #calculations
        totalGrowth = data[str(endYear)] / data[str(startYear)]
        power = 1/(endYear-startYear)
        perYear = totalGrowth**power

        #make into percentages
        totalGrowthPercentage = (totalGrowth - 1)*100
        perYearPercentage = (perYear - 1)*100

        #round values to the nearest two decimal points
        totalGrowthPercentage = round(totalGrowthPercentage, 2)
        perYearPercentage = round(perYearPercentage, 2)
        
        #create a dataFrame that contains the growth data for each country
        growthDf = pd.DataFrame(data=[data["Country Name"], totalGrowthPercentage, perYearPercentage]).T
        growthDf.columns = ["Country", f"Total growth (%) from {startYear} to {endYear}", "Growth per year (%)"]

        #save into a file
        growthPath = path.join(path.dirname(__file__), "Results/growthData.csv")
        growthDf.to_csv(growthPath, index=False)


        #merge growthDf with area/pop data
        combined = growthDf.merge(sizeData, left_on="Country", right_on="Country Name")
        combined = combined.loc[:, ["Country", "Growth per year (%)", "2017"]]

        import numpy as np
        #drop infinite values. We need to covert them into "nan" to be able to drop them
        combined.replace([np.inf, -np.inf], np.nan, inplace=True) 
        combined.dropna(inplace=True)

        return combined


