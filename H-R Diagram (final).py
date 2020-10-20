import csv

filename = "hygdata_v3.csv"

allfields = []
rows = []

with open('/Users/minoli/My Computer Documents/astronomy/2019 summer project/hygdata_v3.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    allfields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print("no of fields ", len(allfields))

fields_required = ['id', 'hip', 'ra', 'dec', 'dist', 'absmag', 'spect', 'ci', 'x', 'y', 'z']
reqcolumn_num = []

for i in range(len(fields_required)):
    for j in range(len(allfields)):
       if fields_required[i] == allfields[j]:
            reqcolumn_num.append(j)


num_input = csvreader.line_num - 1


all_req_data = []
for row in range(num_input):
    req_row_data = []
    for k in range(11):
        offset = reqcolumn_num[k]
        value = rows[row][offset]
        req_row_data.append(value)
    all_req_data.append(req_row_data)

print("number of stars 1 =", len(all_req_data))
for x in all_req_data[:]:
    if x[7] == '':
        all_req_data.remove(x)

print("number of stars 2 =", len(all_req_data))
for i in all_req_data[:]:
    if float(i[7]) > 2.0:
        all_req_data.remove(i)

for i in all_req_data[:]:
    if float(i[8]) < 0:
        all_req_data.remove(i)

for i in all_req_data[:]:
    if float(i[9]) > 0:
        all_req_data.remove(i)


finalnum = len(all_req_data)

ra = []
spect_type = []
absolute_mag = []
colour_index = []
dist = []
dec = []
for star in range(finalnum):
    absolute_mag.append(float(all_req_data[star][5]))
    spect_type.append(all_req_data[star][6])
    checkvar = all_req_data[star][7]
    colour_index.append(float(all_req_data[star][7]))
    ra.append(float(all_req_data[star][9]))
    dec.append(float(all_req_data[star][10]))
    dist.append(float(all_req_data[star][8]))


print("number of stars =", finalnum)

import numpy as np
import matplotlib as mpl

import matplotlib.pyplot as plt

x = colour_index
y = absolute_mag
plt.figure(figsize=(13.2, 15))
cmap = mpl.colors.LinearSegmentedColormap.from_list('custom', ['#161975', '#1f4e89', '#a2d9df', '#ffffff', '#fef467', '#e73626', '#e0fe3f'])
scale = 0.05
plt.scatter(x,y, s=scale, c=x, cmap=cmap)
plt.xticks(np.arange(min(x), max(x), 0.5))
plt.gca().invert_yaxis()
plt.title('Hertzsprung-Russell Diagram')
plt.gca().set_facecolor('black')
plt.xlabel('Colour Index')
plt.ylabel('Absolute Magnitude')
plt.show()




