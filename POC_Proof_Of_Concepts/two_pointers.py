a = [2, 4, 7, 9]
b = [2, 3, 6, 7, 8]
c = []

while pa < a.len() and pb < b.len():
  if a[pa] <= b[pb]:
    c.append(a[pa])
    pa += 1
  else:
    c.append(b[pb])
    pb += 1
while pa < a.len():
  c.append(a[pa])
  pa += 1
while pb < b.len():
  c.append(b[pb])
  pb += 1
print(c)
