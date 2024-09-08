#IT5001 Week 2

def compare_2_values():
    z = 1000
    x = z < 1
    print(x)

def marry_decision():
    age = 12
    consent = True
    if age > 21 or age < 21 and consent == True:
        print("you can get MR")
    else:
        print("you cannot get MR")

def string_operation():
   #compare if both string acsii value are less or more
    s = 'ba'
    t = 'bab'
    x = t > s
    print(x)

def multiply(*args):
    z = 1
    for i in args:
        z += i
        print(f' current value {z}')
    return z

def input_integers(*args):
    i = 0
    number = args[0]
    while i < int(number):
        i += 1
        print(i)

def execute_integers():
    number = input('key in number of integers to use:')
    input_integers(number)

def add_2_things(a,b):
    try:
        c = a + b
        print(c)
    except Exception as e:
        print(f' an error occurred {e}')
    finally:
        print(f'exit the loop')


if __name__ == "__main__":
    add_2_things(a=1,b='bbb')