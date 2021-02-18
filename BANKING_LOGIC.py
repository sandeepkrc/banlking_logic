class Custemer:
	"""custeme application"""
	bank="SBI"
	def __init__(self, cname,cadd,cbal,cac):
		self.cname = cname
		self.cadd = cadd
		self.cac = cac
		self.cbal = cbal		
	def deposit(self,damt):		
		self.cbal = self.cbal+damt
		print("Amount Deposited ",damt," Successfully")
	def withdraw(self,dwth):
		self.cbal = self.cbal -dwth
		print("Amount withdraw ",dwth," Successfully  ")
	def display(self):
		print(" BRANCH NAME -- ",Custemer.bank)
		print("Custemer NAME -- ",self.cname)
		print("Custemer ADD -- ",self.cadd)
		print("Custemer ACCOUNT NO-- ",self.cac)
		print(" Custemer BAL -- ",self.cbal)
a1=input("enter the Custemer NAME = ")
b1 = input(" enter your address ")
c1= input("enter the balance =")
d1 = input("enter the custemer account no = ")

try:
        a=str(a1)
        b=str(b1)
        c=int(c1)

        d=int(d1)
        c1= Custemer(a,b,c,d)
        c1.display()
        n=input("enter withdraw amt= ")
        while True:
                w=int(n)
                c1.withdraw(w)   
#RAJ.SANDIP96@GMAIL.COM
                c1.display()
                break
                print("plase inter wamtt ")      

#RAJ.SANDIP96@GMAIL.COM
        while True:
                wd=int(input("enter deposit amt= "))
                c1.deposit(wd)
                c1.display()
                print("end ")
                break
                print("iiiiiiiiii")
        
except:
        print("""failed
                you enter wrong detailed
                """)

        






		




    
