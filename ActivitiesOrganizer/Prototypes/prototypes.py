class Activity:
    #Metodo constructor de una clase
    def __init__(self,name,hours,days,shift):
        self.name = name
        self.hours = hours
        self.days = days
        self.shift = shift

    def shiftCheck(self):
        if self.shift == 'm':
            return 'morning'
        else:
            return 'afterNoon'



class Day:
    def __init__(self):
        self.morning  = []
        self.afterNoon = []
