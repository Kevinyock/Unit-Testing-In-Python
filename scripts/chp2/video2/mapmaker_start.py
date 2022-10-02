class Point():

    def __init__ (self,CityName, Latitutde, Longtitutde):
        self._CityName = CityName
        self._Latitutde = Latitutde
        self._Longtitutde = Longtitutde

    def get_lat_long(self):
        return (self._Latitutde,self._Longtitutde)