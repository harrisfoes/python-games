def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21 and not on_break and time >= 5 and time <= 10:
        return True
    else:
        return False

