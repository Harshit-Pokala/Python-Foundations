print("Welcome to treasure island.")
print("Your mission is to find the treasure.")

a = input("Youre at a crossroad, Where do you wanna go(left or right)? ")
if (a ==  "right"):
    print("fall into a hole \n Game Over")
elif (a == "left"):
    print("Youve come to a lake. There is an island in the middle of the lake,")
    b = input("Do you wanna wait for the boat or swim till the island? ")

    if (b == "swim"):
        print("Attacked by a trout\n Game over.")

    elif (b == "wait"):
        print("you have now come to the island.")
        c = input("choose a door from the red,blue and yellow. ")

        if(c == "red"):
            print("Burned by fire.\n Game Over")

        elif (c == "blue"):
            print("Eaten by beasts.\n Game Over.")

        elif (c == "yellow"):
            print("You Win!!!")

        else:
            print("Game Over.")