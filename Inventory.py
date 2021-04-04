from Player import *

class Inventory(Player):
    
    def __init__(self):
        
        self.objects = []
    
    def add_obj(self, obj):
        
        self.objects.append(obj)
        return self.objects
        
    
    def show_objects(self):
        
        print("""
            Inventario """)
        for obj in self.objects:
            print(f"""        |--------------------------------------------------------------------------------|                   
                {obj}                                                                                  
        |--------------------------------------------------------------------------------|""")

 