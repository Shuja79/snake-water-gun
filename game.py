import random as rd 

'''
1 for Snake
-1 for Water 
0 for Gun

'''
Key = [1 , -1 , 0]
userdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"Snake", -1:"Water",0:"Gun"}
    
while True:
    usernum = input("Enter your Choice: ")
           
    if usernum not in userdict:
            print("Invalid Input! Please enter correct input.\n")
            continue
    user = userdict[usernum]
    computer = rd.choice(Key)
    print(f"You Choose: {reversedict[user]}\nComputer choose: {reversedict[computer]}")    
                   
    if computer == user:
        print("Match Draw")
    elif computer == -1 and user == 1:
        print("You Win")
    elif computer == 1 and user == -1:
        print("You Lose")
    elif computer == 0 and user == 1:
        print("You Lose")
    elif computer == 1 and user == 0:
        print("You Win")
    elif computer == -1 and user == 0:
        print("You Lose")
    elif computer == 0 and user == -1:
        print("You Win")
    else:
        print("Something went wrong.")
        continue

    again = input("\nDo you want to continue? (y/n): ").strip().lower()
    if again != "y":
        print("Game close. Thank you!")
        break
    
