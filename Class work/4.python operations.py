#1.Arithametic operations
a=20
b=10
print("Addition(+):",a+b)              #Addition(+): 30
print ("Subraction(-):",a-b)           #Subraction(-): 10
print("Multiplication(*):",a*b)        # Multiplication(*): 200
print("Division (/):,a/b")             # Division (/):,a/b 
print("Floordivision(//):",a//b)       #Floordivision(//): 2
print("Modules(%):",a%b)               #Modules(%): 0
print("exponenation(**):",a**b)        #exponenation(**): 10240000000000

#2.comparison operators                                                                                                                                                                                                                                                                       
print("Equal to (==):",a==b)                     #Equal to (==): False
print("Not Equal to (!=):",a!=b)                 # Not Equal to (!=): True
print("greater than(>):",a>b)                    #greater than(>): True
print("Less than(<):",a<b)                       #Less than(<): False
print("Greater than or equal to(>=):",a>=b)      #Greater than or equal to(>=): True
print("Less than or equal to (<=):",a<=b)        #Less than or equal to (<=): False

#3.Assignments operators
a=10
print("Assign(=):",a)                       # Assign(=): 10
a=a+10
print("Addition &Assign(+=):",a)            #Addition &Assign(+=): 20
a=a-10
print("Sub & Assign(-+):",a)                #Sub & Assign(-+): 10
a=a*4
print("Multiplication & Assign(*=):",a)     #Multiplication & Assign(*=): 40
a=a/4
print("Division & Assign(/=):",a)            #Division & Assign(/=): 10.0
a=a//2
print("Floor division & Assign(//=):",a)     #Floor division & Assign(//=): 5.0
a=a%3
print("Module & Assign(%=):",a)               #Module & Assign(%=): 2.0
a=a**4
print("Exponentation & Assign(**=):",a)       #Exponentation & Assign(**=): 16.0

#4.Logical operation
a=20
b=30
print("AND:",a%2==0 and b%3==1 and a%4==0)     # AND: False
print("AND:",a%2==0 and b%1==0 and a%4==0)     #AND:True
print("OR:",a%3==0 or b%4==0 or a%5==0)       # OR: True
print("NOT:",a%4==0)                          #NOT: True

#5.Membership operations
#list
L=["Bhavana","Hema","safna"",Mounika"]
print("Hema" in L)                           #statement True
print("vishva" not in L)                     #statement True
print("bhavana" in L)                        #statement False
#set
S={1,2,3,4,5,6}
print(3 in S)                   #statement True
print(8 not in S)               #statement True
print(0  in S)                  #statement False

#tuple 
t=[1,3,4,5,6]
print(7 in t)               #statement False
print(3 in t)               #statement True 
print(10 not in t)          #statement True

#Dictionary
d={'name':'Bhavana','Age':'21','branch':'DS',}
print('Age' in d)                                #statement True
print('srija' not in d)                          #statement True
print('branch' in d)                             #statement True
print('bhavana' in d)                            #statement False

#Identity operations
a=[2,3,4,5,6]
b=[2,3,4,5,6]
c=[2,3,4,5,6]
a=b
print(a is c)                             # statement False
print(b is a)                             #statement true
print(c not in a)                         #statement True
