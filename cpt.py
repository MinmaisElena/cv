import random

print("I have been staying home for a while.. I don't know when whould this pandemic end. What should I do?(Please type T for True and F for False.)")
def wrong():
    print("Wrong! please retry")
    main()
def ending1():
    print("I survived from this pandemic. I wore mask and I washed my hands really often. Social distancing also helped me to prevent spreading / getting rid of the virus. Please stay safe until this pandemic ends.")
    bouns = str(input("Do you want to try the bonus question? Answer in Y or N : "))
    if bouns == "Y":
        random_num = random.randint(1,100)
        inputU = int(input("How many masks do I have? : "))
        answer = False
        while answer == False:
            if inputU > random_num:
                print("It is smaller than that number")
                inputU = int(input("Enter a number of masks I got : "))
                answer = False
            elif inputU < random_num:
                print("It is bigger than that number")
                inputU = int(input("Enter a number of masks I got : "))
                answer = False
            else:
                print("You got the number! The number was " + str(random_num))
                answer = True
    else:
        print("Thanks for playing!")
def main():
    count = 0
    usernum1 = str(input("I should stay in home until this pandemic ends. : "))
    if usernum1 == "T":
        count += 1
        usernum2 = str(input("I should wash my hands and keep myself clean to prevent the COVID-19. : "))
        if usernum2 == "T":
            count += 1
            usernum3 = str(input("I should meet my friends because my friends are funnier than staying home. : "))
            if usernum3 == "F":
                count +=1
                usernum4 = str(input("I should wear mask when I go outside. : "))
                if usernum4 == "T":
                    count += 1
                    usernum5 = str(input("I went outside for work and I have a fever. I should not report to the hospital because I am healthy enough to not die."))
                    if usernum5 == "F":
                        count += 1
                        print("Yoohoo! I got " + str(count) + " questions right!")
                        ending1()
                    else:
                        wrong()
                else:
                    wrong()
            else:
                wrong()
        else:
            wrong()
    else:
        wrong()

main()