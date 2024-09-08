def burgerPrice(order):

    price_dict = {
        'B': 0.5,
        'C': 0.8,
        'P': 1.5,
        'V': 0.7,
        'O': 0.4,
        'M': 0.9
    }

    final_price = 0

    for i in order:
        price = price_dict.get(i)
        final_price = final_price + price

    print(final_price)


if __name__ == "__main__":
    burgerPrice('BVPB')
