from collections import Counter
import csv
with open('data.csv',newline = '')as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range (len(filedata)):
    n = filedata[i][2]
    newdata.append(float(n))

data = Counter(newdata)
mode_for_range = {"50-60":0,"60-70":0,"70-80":0}
for height,occurence in data.items():
    if 50<float(height)<60:
        mode_for_range["50-60"]+=occurence
    elif 60<float(height)<70:
        mode_for_range["60-70"]+=occurence
    elif 70<float(height)<80:
        mode_for_range["70-80"]+=occurence
moderange,modeoccurence =0,0
for range,occurence in mode_for_range.items():
    if occurence>modeoccurence:
        moderange,modeoccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((moderange[0]+moderange[1])/2)
print (f"mode: is->{mode:2f} ")
