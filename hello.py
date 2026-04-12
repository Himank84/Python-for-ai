class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        return(f'{self.name} is eating')

    def sleeping(self):
        return(f'{self.name}, is sleeping')

    class Lamma(Animal):
        def sound(self):
            return(f'{self.name},is saying meh eh meh!!')

    Animal.name='Jerry'

    print(Animal.eat(Animal))


#----------------------------------------------------------------------


        
    



    















   

    

     






    

