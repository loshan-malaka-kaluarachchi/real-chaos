class cube:
    def __init__(self,length:float,width:float,height:float) -> None:
        self.length =  length
        self.width = width
        self.height = height
        
    def get_volume(self) -> float:
        return self.length*self.width*self.height
    
    def get_surface_area(self) -> float:
        return 2*(self.length*self.width + self.length*self.height + self.height*self.width)
    
    def get_SA2Vol_ratio(self) -> float:
        ans = self.get_volume()/self.get_surface_area()
    
#x = cube(5,2,3)
'''
volume = f'Volume = {x.get_volume()}'
surfArea = f'Surface area = {x.get_surface_area()}'
Sf_Vol_ratio = f'Surface area to Volume ratio = {x.get_SA2Vol_ratio()}'
print(volume + '\n' + surfArea +'\n' + Sf_Vol_ratio)
'''
#############################################################################

