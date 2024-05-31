def purchase(price, money_available):
    if price > money_available:
        raise Exception("not enough money")

    return money_available - price 
