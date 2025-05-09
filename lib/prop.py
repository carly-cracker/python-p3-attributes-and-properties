class Human:
    species = "Homo sapiens"

    def __init__(self,age):
        self.age = age

    def get_age(self):
        print("getting age")
        return self._age
    
    def set_age(self,age):
        if (type(age) in (int,float)) and (0<=age<=120):
            print(f"setting age to {age}")
            self._age=age
        else:
            print("thats way too old!")
            self._age = age

    age = property(get_age,set_age)


carlos = Human(15) 
print(carlos.age)