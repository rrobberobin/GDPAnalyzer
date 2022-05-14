
#for checking errors
class errorChecker:

    def __init__(self, year:str):
        self.year = year

    #for checking that the given year is a number and between 1960 and 2020
    def errorCheck(self):
        year = self.year

        #check if the year is valid. Otherwise report the error
        if not year.isnumeric():
            raise Exception(f"The inputted year is not a number. Your input was {year}. The year needs to be a number between 1960 and 2020")
        elif int(year) < 1960 or int(year) > 2020:
            raise Exception(f"The year needs to be a number between 1960 and 2020. Your input was {year}")
        


    