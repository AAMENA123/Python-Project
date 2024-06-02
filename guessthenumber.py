import random 

def guess(x):
    r_num = random.randint(1,x)
    no = 0
    while no != r_num:
        no = int(input(f"Enter the number in the range 1 to {x}:"))
        if(no<r_num):
         print(no,"is not the number and is smaller than chosen number.")
        elif no > r_num:
         print(no, "is not the number and is higher than the chosen number")
    print(no, "is the number")
guess(int(input("Enter the range:")))
        