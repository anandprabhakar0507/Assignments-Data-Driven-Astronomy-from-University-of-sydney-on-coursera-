data = []
for line in open('data.csv'):
  data.append(line.strip().split(','))

print(data)