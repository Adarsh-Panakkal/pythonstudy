class Embloyee :
    company_name = 'ABCD TECH'
    location = "calicut"
    def __init__(self,id,name,salary):
        self.emp__id = id
        self.emp__name = name
        self.emp__salary = salary
    def get_details(self):
        print(self.emp__id,self.emp__name,self.emp__salary)

obj1 = Embloyee(101,"arun",100000)
obj2 = Embloyee(102,"Ajay",1000000)

obj1.get_details()
obj2.get_details()