print ("rules:")
print ("1. if its errors its because you tries to cheat") 
print ("2. if you cant try again its because you tried to cheat")
print ("do not enter your valute everything here is in dolar$")
print ("Have fun!")



def account(name, surname, gmail, password):
    if len (name) == 0:
        return "incorrect try again"
    if len (surname) == 0:
        return "incorrect try again"
    if gmail.endswith ("@gmail.com"):
        return ""
    if len (password) < 8:
        return "your password should have at least 8 digits try again"
    else:
        return "congrats you have made an account"
print (account (input("name: "), input ("surname: "), input ("gmail: "), input ("password: ")))

def deposit (money):
    print (f"you have {money}$ in your account do you want to add?")
    if "yes":
        something = int (input ("please enter money that you want to add in the bank: "))
    else: pass
    return f"you have {money + something}$ on your deposit balance"
    

print (deposit (int (input ("please enter money that you want to have in the bank: "))))

def withdraw (money1):
    print ("do you want to take some money?")
    if "yes":
        j1 =  (int(input ("enter the money that you want to take: ")))
        print (j1)
        print (f"you have {(money1 + j1) * -1}$ on your withdraw balance")


print (withdraw(int(input("enter the money thet you want to take: "))))

def exit ():
    print ("just in case we will look over everything one more time")
    s1 =  (int(input ("how much money do you want to add? ")))
    print (s1)
    print (f"you have added {s1}$ on your account")
    print ("want to go to withdraw?")

    w1 =  (int(input("how much money do you want to take? "))) 
    print (w1)
    print (f"you have added {w1}$ to your account")
    a1 = (int(input("how much money do you want to take? ")))
    print (a1)
    print (f"you have added {a1}$ to your account")
    print ("want to go to deposit?")
    b1 =  (int(input ("how much money do you want to add? ")))
    print (b1)
    print (f"you have added {b1}$ on your account")
    print ("BYE!")


print (exit ())