from forex_python.converter import *
c = CurrencyRates()

primary = input("Convert from :")
secondary = input("convert to :")

rates = c.get_rate(primary,secondary)

print(rates)
