data = []
for line in open('data.csv'):
  row = []
  for col in line.strip().split(','):
    row.append(float(col))
  data.append(row)

print(data)