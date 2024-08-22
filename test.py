import pandas as pd

def print_function():
    df = pd.DataFrame(columns=["col_a","col_b"])

    print(df)

    df["col_a"] = 5
    print(df["col_a"])


def loop_function():
    x = [1,2,3,4,5]

    for i in x:
        print(i)

if __name__ == "__main__":
    loop_function()
