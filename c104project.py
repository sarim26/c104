import csv

with open("SOCR-HeightWeight.csv", newline = "") as f:
    reader = csv.reader(f)
    fd = list(reader)

fd.pop(0)
nd = []

for i in range(len(fd)):
    n_num = fd[i][1]
    nd.append(float(n_num))

n = len(nd)
total = 0

for x in nd:
    total = total + x

mean = total/n
print("mean = "+ str(mean)