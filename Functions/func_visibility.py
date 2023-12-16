
marks = [4, 5, 3, 2, 7]

def increase(marks):
    marks = [1,2,3,4]
    print(*marks)

def new_marks(marks):
    marks += [777]
    print(increase(marks))

increase(marks)

new_marks(marks)

def gcd(x, y):
    gcd = min(x, y)
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            return gcd

num_1 = gcd(1440, 680)
print(num_1)

def number_length(number):
    number = abs(number)
    len = 1
    decim = 10
    while decim < number:
        decim *= 10
        len += 1
    return len

print(number_length(-88887))

def month(number, lang):
    months = {1: ['January', 'Январь'], 2: ['February', 'Февраль'], 3: ["March", "Март"],
              4: ["April", "Апрель"], 5: ["May", "Май"], 6: ["June", "Июнь"],
              7: ["July", "Июль"], 8: ["August", "Август"], 9: ["September", "Сентябрь"],
              10: ["October", "Октябрь"], 11: ["November", "Ноябрь"], 12: ["December", "Декабрь"]}
    if lang == "en":
        return months[number][0]
    else:
        return months[number][1]

months = month(8, "ru")

print(months)


