# /usr/bin/env python3
class People(object):
    def __init__(self,name,edad,dni,region):
        self.name=name
        self.edad=edad
        self.dni=dni
        self.region=region
        
    def crecer(self):
        self.edad=self.edad+1

    def __str__(self):
        return "{}, {} años con DNI {}".format(self.name,self.edad,self.dni)