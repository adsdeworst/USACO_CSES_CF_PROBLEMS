import datetime
a = datetime.datetime.now()
for i in range(100000):
    continue

diff = a - datetime.datetime.now()
print(diff.microseconds/1000)