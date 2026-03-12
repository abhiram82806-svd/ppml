class employee:
    def __init__(self,empid,name,basic_pay):
        self.empid=empid
        self.name=name
        self.basic_pay=basic_pay
        self.ta=0
        self.da=0
        self.gross_pay=0
    def cale(self):
        self.ta = 0.1*self.basic_pay
        self.da = 0.4*self.basic_pay
        self.gross_pay = self.basic_pay+self.ta+self.da
    def disp(self):
        print("the employee id is :" ,self.empid)
        print("the name is :" ,self.name)
        print("the basic pay is : ",self.basic_pay)
        print("the ta value is : ",self.ta)
        print("the gross pay is : ",self.gross_pay)
        
 

a = int(input("enter the eid : "))
b = input("enter the name : ")
c = int(input("enter the bp : "))

obj = employee(a,b,c)
obj.cale()
obj.disp()
