x = int(input()) #предыдущее
y = int(input()) #текущее
if y >= x:
    used = y - x
else:
    used = (10000 - x) + y
if used <= 300:
    cost = 21.0
elif used <= 600:
    cost = 21 + (used - 300) * 0.06
elif used <= 800:
    cost = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
avg_price = cost / used
print("Предыдущее:", x)
print("Текущее:", y)
print("Использовано:", used)
print("К оплате:", round(cost, 2))
print("Ср. цена m^3:", round(avg_price, 2))