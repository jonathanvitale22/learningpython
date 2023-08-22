#Title
import time

course = "Python for beginners"
print(course.upper().replace(" ", "..."))

    #Ask user for name
name = input("First thing's first, who am I speaking with today? ")
name = name.strip().title()

    #Greet user
print(f"Nice to meet you, {name}!")

a = input("Would you like to do some math? (y/n) ")

#Basic addition
if "y" == a:
    a = print("Great!")
    x = int(input("Let's do some addition. What's x? "))
    y = int(input("What's y? "))
    a = print(f"That equals {x + y}!")
    time.sleep(3)
#end program
    print("I'm tired. Goodnight.")
    

    #User is being a butt
elif a == "n":
    a = print("Well that sucks.")
    
    
    #User wants to infinitely expand their knowledge
else:
    a = print("Nice try, wise-guy.")


    
    
