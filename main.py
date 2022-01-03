import random

def Wingame(comp,you):
    if comp==you:
        None
    if comp=="r":
        if you=="s":
            return False
    elif you=="p":
            return True
    if comp=="p":
        if you=="r":
            return False
    elif you=="s":
            return True
    if comp=="s":
        if you=="p":
            return False
    elif you=="r":
            return True

randomNo=random.randint(1,3)
print("Comp turn:Rock(r) Paper(p) Sisor(s)?")
if randomNo==1:
    comp='r'
elif randomNo==2:
    comp='p'
elif randomNo==3:
    comp='s'
you=input("Your turn:Rock(r) Paper(p) Sisor(s)?")

a = Wingame(comp,you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a==None:
    print("You Win!")
elif a:
    print("Its a tie")
else:
    print("You loose")
    