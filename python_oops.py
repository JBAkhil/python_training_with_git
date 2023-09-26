'''demonstration of oops'''
class Employee:
    '''stores the details of an Employee'''

    def __init__(self,name,age,designation):
        '''initializing employee name,age and designation'''
        self.name=name
        self.age=age
        self.designation=designation

    def get_name(self):
        '''to access the name of an employee'''
        return self.name

class Company:
    '''The company in which all the employees are registered to'''

    def __init__(self,name,maxemp):
        self.name=name
        self.maxemp=maxemp
        self.role=[]
        '''employee details initializing'''

    def set_role(self,post):
        '''to set the role of an employee and return success or failure'''
        if len(self.role) < self.maxemp:
            self.role.append(post)
            print("success")
        else:
            print("cant")

e1=Employee("ep1",20,"noob")
e2=Employee("ep2",25,"mid")
e3=Employee("ep3",30,"pro")
c1=Company("bc",2)
c1.set_role("intern")
c1.set_role("junior")

class Pet:
    '''Pet details'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        '''pet params initialization'''
    def show(self):
        '''print pet details'''
        print("name: ",self.name,"age: ",self.age)

class Dog(Pet):
    '''a inherited class of pet - dog'''
    def __init__(self,name,age,likes):
        '''initializing dog params from cat and what dog likes'''
        super().__init__(name,age)
        self.likes=likes
    def speak(self):
        '''an unique method for dog'''
        print("barks")
    def likes_what(self):
        '''accessing the new param introduced in this class'''
        print("likes to get ",self.likes)
class Cat(Pet):
    '''a inherited class of pet - cat'''
    def speak(self):
        '''an unique method for cat'''
        print("meows")

p1=Pet("doggy",10)
p1.show()
d1=Dog("doggy",10,"pat")
d1.speak()
d1.likes_what()
