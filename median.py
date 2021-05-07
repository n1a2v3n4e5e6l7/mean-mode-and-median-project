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
newdata.sort()
if num%2 ==0:
    median1 = float(newdata[num//2])
    median2 = float(newdata[num//2-1])
    median = (median1+median2)/2
else:
    median = newdata[n//2]
print ("median: "+str(median))



