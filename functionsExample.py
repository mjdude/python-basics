def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars

r = input("Enter rate :")
e = input("Euros is :")


print(currency_converter(float(r),float(e)))