x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if ((x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0) or
        (x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0) or
        (x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0) or
        (x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0)):

    if (x1 > 0 and y1 > 0):
        print("Yes, I четверть")
    elif (x1 < 0 and y1 > 0):
        print("Yes, II четверть")
    elif (x1 < 0 and y1 < 0):
        print("Yes, III четверть")
    elif (x1 > 0 and y1 < 0):
        print("Yes, IV четверть")
else:
    print("No")