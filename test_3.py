a = 1
def check_():
    if 5 < a:
        print('y')
        b = "y"

    else:
        b = "n"
    return b

if __name__ == "__main__":
    response = check_()
    print(f' response == {response}')

