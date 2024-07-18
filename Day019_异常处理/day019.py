class OutOfCoffeeException(Exception):
    pass
class KeyboardCatException(Exception):
    pass
def drink_coffee(cups):
    if cups == 0:
        raise OutOfCoffeeException("Oh no! I'm out of coffee!")
    else:
        print("Enjoy your coffee!")
def play_with_cat():
    raise KeyboardCatException("Oops! The keyboard is occupied by a cat!")
    
try:
    drink_coffee(0)
except OutOfCoffeeException as e:
    print(e)
try:
    play_with_cat()
except KeyboardCatException as e:
    print(e)
    