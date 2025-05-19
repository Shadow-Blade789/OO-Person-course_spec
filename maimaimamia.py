class Person:
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def PrintName(self):
        print(f"{self.firstname} {self.lastname}")

class Student(Person):
    def __init__ (self, studentid, housegroup, firstname, lastname):
        self.studentid = int(studentid)
        self.housegroup = housegroup
        super().__init__(firstname, lastname)
        classes = []
    
    def enrolclass(self):
        clas = input("What classes do you actually pay attention in?")
        self.classes.append(clas)
        print(self.classes)

yum = Student(182746458364856374735485985348454, "gvhfukes gvryeuk", "bvfhuks fgfehwuk vfeghuwk vgfuwke gvfuewk gvyfukw gvyfuwk gvyfuwek", "gfeywukbhwdqjcvbnsmhejkwhfukewgceh fhejkwhfejdkwjgcd hjwk cgjk")
yum.enrolclass()