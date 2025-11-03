pred = int(input()) #предыдущее
tek = int(input()) #текущее
if tek >= pred:
    used = tek - pred #счетчик сбросился
else:
    used = (10000 - pred) + tek
if used <= 300:
    prise = 21.0
elif used <= 600:
    prise = 21 + (used - 300) * 0.06
elif used <= 800:
    prise = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    prise = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
avg_price = cost / used
print("Предыдущее:", pred)
print("Текущее:", tek)
print("Использовано:", used)
print("К оплате:", round(prise, 2))
print("Ср. цена:", round(avg_price, 2))
