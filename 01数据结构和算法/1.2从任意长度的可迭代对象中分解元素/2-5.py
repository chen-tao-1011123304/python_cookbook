record = ('chen', 50, 123.45, (2020, 5, 18))
name, *_, (*_, day) = record

print(name)
print(day)


