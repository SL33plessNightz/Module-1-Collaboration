#7.4 - 7.7 stuff
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
print(things)

things[0] = things[0].upper()
print(things)

del things[2]
print(things)

#9.1 and 9.2 Part
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

count = 0
for number in get_odds():
    count += 1

    if count == 3:
        print(number)
        break
