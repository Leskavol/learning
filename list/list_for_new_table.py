guests = [
    "aaa",
    "bbb",
    "ccc"
]
print("Нужно больше гостей!")
guests.insert(0, "ddd")
guests.insert(2, "eee")
guests.append("fff")
print("Я устал звать гостей, приходи " + guests[0])
print("Я устал звать гостей, приходи " + guests[1])
print("Я устал звать гостей, приходи " + guests[2])
print("Я устал звать гостей, приходи " + guests[3])
print("Я устал звать гостей, приходи " + guests[4])
print("Я устал звать гостей, приходи " + guests[5])
print("Все не влезли, придут обадва")
print("Прости, " + guests.pop(0) + ", ты не приглашен")
print("Прости, " + guests.pop(0) + ", ты не приглашен")
print("Прости, " + guests.pop(0) + ", ты не приглашен")
print("Прости, " + guests.pop(0) + ", ты не приглашен")
print("Го, " + guests[0] + ", все в силе")
print("Го, " + guests[1] + ", все в силе")
del guests[1]
del guests[0]
print(guests)
