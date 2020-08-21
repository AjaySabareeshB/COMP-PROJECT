#movies
#the date and timing function shd come before the seat type...define and make changes
#make variables like date,movie and all global
import random
n=0
movie=""
date=""
price=0
cost=0
type=''
nu=0
l=['SHAWSHANK REDEMPTION','INCEPTION','INTERSTELLAR','FORD VS FERRARI']
def dates():
    global movie
    global date
    
    print("your movie choice ",movie,"  is available on the following days ")
    days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    temp=[]
    for i in range(0,3):
        temp.append(random.choice(days))
    for i in temp:
        print(i)
    print()   
    print("enter 1 for ",temp[0])
    print("enter 2 for ,",temp[1])
    print("enter 3 for ",temp[2])
    d=int(input())
    if d==1:
        print("date chosen is ",temp[0])
        date=temp[0]
    elif d==2:
        print("date chosen is ",temp[1])
        date=temp[1]
    elif d==3:
        print("date chosen is ",temp[2])
        date=temp[2]
    print()
    print("enter 1 to choose seating")
    print("if   you wish to go back enter B")
    d=input()
    if ( d=='B'):
        menumovie1()
    elif(d=='1'):
        seattype()
    
    
def aftermenu1():
    global n
    global movie
    if(n==1):
        movie=l[0]
        print("you have chosen shawshank redemption")
        print("press 1 to go back and make ur movie choice again")
        print("press 2 to continue with booking")
        n=int(input())
        if(n==1):
            menumovie1()
        else:
            dates()
    elif(n==2):
        movie=l[1]
        print("you have chosen inception")
        print()
        print("press 1 to go back and make ur movie choice again")
        print("press 2 to continue with booking")
        n=int(input())
        if(n==1):
            menumovie1()
        else:
            dates()
    elif(n==3):
        movie=l[2]
        print("you have chosen interstellar")
        print()
        print("press 1 to go back and make ur movie choice again")
        print("press 2 to continue with booking")
        n=int(input())
        if(n==1):
            menumovie1()
        else:
            dates()
    elif(n==4):
         movie=l[3]
         print("you have chosen ford vs ferrari")
         print()
         print("press 1 to go back and make ur movie choice again")
         print("press 2 to continue with booking")
         n=int(input())
         if(n==1):
            menumovie1()
         else:
             dates()
    elif(n==5):
         print("going back just a second..")
    else:
            print("response does not match with any options")
            menumovie1()

def menumovie1():
    global n
    print("enter 1 for ",l[0])
    print("enter 2 for ",l[1])
    print("enter 3 for ",l[2])
    print("enter 4 for ",l[3])
    print("enter 5 to go back ")
    n=int(input("enter your response"))
    aftermenu1()
def seattype():
    global price
    global type
    print("the seating is available in 3 types ")
    print("PLATINUM-Rs 500")
    print("GOLD-  Rs 400 /-")
    print("SILVER- Rs 200/-")
    print("enter ' P' for platinum , 'G' for gold or 'S' for silver")
    print("enter 5 to go back")
    s=input()
    input()
    if(s=='p' or s=='P'):
        type="PLATINUM"
        price=500
        numberofseats()
    elif(s=='g' or s=='G'):
        type="GOLD"
        price=400
        numberofseats()
    elif(s=='s' or s=='S'):
        type="SILVER"
        price=200
        numberofseats()
    elif(s=='5'):
        dates()
def numberofseats():
    global price
    global nu
    global cost
    print("maximum seats per person is 10")
    print("enter  100 to go back ")
    nu=int(input("enter the number of seats you wish to book"))
    
    number=[1,2,3,4,5,6,7,8,9,10]
    if nu in number:
        cost=price*nu
    elif nu==100:
        seattype()  
    else:
        print("maximum number of seats is 10 or you have entered non integer value ")
        numberofseats()
    print()   
    print("Enter 1 to checkout")
    print("Entter 2 to go back")
    t=int(input())
    if t==1:
        bill()
    elif t==2:
        numberofseats()
        
def bill():
    global date
    global movie
    global price
    global type
    global cost
    global nu
    print("MOVIE:",movie)
    print("DAY:",date)
    print("SEAT TYPE",type)
    print("NUMBER OF SEATS",nu)
    print("PRICE:",cost)
    
    
        
          
    
        
    
menumovie1()  
