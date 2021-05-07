import csv
with open('data.csv',newline = '')as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range (len(filedata)):
    n = filedata[i][1]
    newdata.append(float(n))
num = len(newdata)
total = 0
for x in newdata:
    total+=x
mean = total/num
print ("mean: "+str(mean))



