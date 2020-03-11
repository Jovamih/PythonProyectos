# /usr/bin/env/ python3
class People(object):
    def __init__(self,name,edad,dni,region):
        self.name=name
        self.edad=edad
        self.dni=dni
        self.region=region
        
    def crecer(self):
        self.edad=self.edad+1
    
    def getName(self):
        return self.name
    
    
class Employee(People):
    def __init__(self,name,edad,dni,region,especialidad,empresa):
        self.especialidad=especialidad
        self.empresa=empresa
        People.__init__(self,name,edad,dni,region)
        
    def changeEnterprise(self,empresa):
        self.empresa=empresa
        
    def __str__(self):
        return "Empleado {}\nEspecialidad: {}\nEmpresa: {}".format(People.getName(self),self.especialidad,self.empresa)
        
if __name__=="__main__":
    emp=Employee("johan",19,"74804782","Peru","Ing.Sistemas","IBM")
    print(emp)