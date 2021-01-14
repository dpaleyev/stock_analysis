import csv
import datetime

with open('new.csv') as csv_file:
    prices = []
    basis_time = datetime.datetime(2015, 1, 1)

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            date = row[1]
            time = row[2]
            price = row[3]

            d_time = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:8]), int(time[:2]), int(time[2:4]))
            delta = (d_time - basis_time).total_seconds() / 60.0

            prices.append((int(delta), float(price), d_time))

        line_count += 1

    high_price = []
    low_price = []

    for i in range(len(prices)):
        if i == 0:
            if prices[i][1] < prices[i + 1][1]:
                low_price.append(prices[i])
        elif i == len(prices) - 1:
            if prices[i][1] > prices[i - 1][1]:
                high_price.append(prices[i])
        else:
            if prices[i - 1][1] > prices[i][1] and prices[i + 1][1] > prices[i][1]:
                low_price.append(prices[i])
            elif prices[i - 1][1] < prices[i][1] and prices[i + 1][1] < prices[i][1]:
                high_price.append(prices[i])

    k = int(input('Введите количество транзакций: '))
    best_k = 1
    r = (0, 0)
    if k == 1:
        for i in low_price:
            for j in high_price:
                if i[0] < j[0]:
                    if j[1]/i[1] > best_k:
                        r = (i[2], j[2])
                        best_k = j[1]/i[1]
    print("Купить:", r[0])
    print('Продать:', r[1])
    print("Прибыль: +", '%06.2f' % ((best_k - 1) * 100), '%')




