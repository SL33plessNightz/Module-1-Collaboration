secret = 4
guess = 6
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")
    
small = True
green = False

if small and green:
    print("pea")
elif small and not green:
    print("cherry")
elif green and not small:
    print("watermelon")
else:
    print("pumpkin")
    
list = [3,2,1,0]
for i in list:
    print(i)
    
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1

guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break   

    