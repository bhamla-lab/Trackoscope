import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.gridspec as gridspec
import pandas as pd
import mplcursors
import pandas

# reference code: https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
# color map reference: https://matplotlib.org/stable/tutorials/colors/colormaps.html
# decent cmap types - 'turbo', 'gist_rainbow', 'cool', 'hsv', 'nipy_spectral'

# read csv file and create pandas dataframe
csvfile = 'CSVFiles/BrineShrimp1.csv'
df = pd.read_csv(csvfile)

# variables and lists needed
time = []
maxt = df.max()[2]
speed = []
x = []
y = []

# gets x and y values and timestamps
for index, row in df.iterrows():
    x.append(round((row['xval']), 3))
    y.append(round((row['yval']), 3))
    time.append(row['time'])

# calculates speed
# count = 0
# for t in time:
#     changet = time[count + 1] - time[count]
#     # calculate speed based on change in distance/change in time
#     if changet != 0:
#         distance = np.sqrt(((x[count + 1] - x[count]) ** 2) + ((y[count + 1] - y[count]) ** 2))
#         v = round((distance / changet), 2)
#         if v < 1:
#             speed.append(v)
#         else:
#             speed.append(speed[-1])
#     else:
#         speed.append(speed[-1])
#
#     count = count + 1
#
#     if count + 1 >= len(x):
#         break
#
# speed.append(speed[-1])

modtime = []
modspeed = []
totdistance = 0
# calculates modded speed
count = 0
for t in time:
    modtime.append(time[count])
    changet = time[count + 5] - time[count]
    # calculate speed based on change in distance/change in time
    if changet != 0:
        distance = np.sqrt(((x[count + 3] - x[count]) ** 2) + ((y[count + 3] - y[count]) ** 2))
        totdistance = totdistance + distance
        v = round((distance / changet), 2)
        if v < 500:
            modspeed.append(v)
        else:
            modspeed.append(modspeed[-1])
    else:
        modspeed.append(modspeed[-1])

    count = count + 5

    if count + 5 >= len(x):
        break


def smooth(y, box_pts):
    box = np.ones(box_pts) / box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


modspeed = smooth(modspeed, 3)

# define plots
fig = plt.figure(figsize=(8, 6), facecolor='white', constrained_layout=True)
spec = fig.add_gridspec(2, 2)
ax = fig.add_subplot(spec[0, 0], xlabel='X-Movement (μm)', ylabel='Y-Movement (μm)', title='Position vs Time',
                     navigate=False, fc='white')
ax1 = fig.add_subplot(spec[1, :], xlabel='Time (s)', ylabel='Speed (μm/s)', title='Speed vs Time', navigate=False,
                      fc='white')
# ax2 = fig.add_subplot(spec[0, 1], xlabel='X-Movement (μm)', ylabel='Y-Movement (μm)', title='Position vs Speed',
#                       navigate=False,
#                       fc='white')

# Create a set of line segments so that we can color them individually
points1 = np.array([x, y]).T.reshape(-1, 1, 2)
segments1 = np.concatenate([points1[:-1], points1[1:]], axis=1)
# Define gradient and plot pos vs time graph
norm1 = plt.Normalize(0, time[-1])
lc1 = LineCollection(segments1, norm=norm1)
lc1.set_array(np.array(time))
lc1.set_linewidth(1)
line1 = ax.add_collection(lc1)
fig.colorbar(line1, ax=ax)
ax.set_xlim(df.min()[0] - 50, df.max()[0] + 50)
ax.set_ylim(df.min()[1] - 50, df.max()[1] + 50)

# # Create a set of line segments so that we can color them individually
# points2 = np.array([time, speed]).T.reshape(-1, 1, 2)
# segments2 = np.concatenate([points2[:-1], points2[1:]], axis=1)
# # Define gradient and plot speed vs time graph
# norm2 = plt.Normalize(0, max(speed))
# lc2 = LineCollection(segments2, norm=norm2)
# lc2.set_array(np.array(speed))
# lc2.set_linewidth(1)
# line2 = ax1.add_collection(lc2)
# fig.colorbar(line2, ax=ax1)
# ax1.set_xlim(0, time[-1] + 5)
# ax1.set_ylim(0, max(speed) + 50)


# Create a set of line segments so that we can color them individually
points2 = np.array([modtime, modspeed]).T.reshape(-1, 1, 2)
segments2 = np.concatenate([points2[:-1], points2[1:]], axis=1)
# Define gradient and plot speed vs time graph
norm2 = plt.Normalize(0, max(modspeed))
lc2 = LineCollection(segments2, norm=norm2)
lc2.set_array(np.array(modspeed))
lc2.set_linewidth(1)
line2 = ax1.add_collection(lc2)
fig.colorbar(line2, ax=ax1)
ax1.set_xlim(0, modtime[-1] + 5)
ax1.set_ylim(0, max(modspeed) + 0.5)

# # Create a set of line segments so that we can color them individually
# points3 = np.array([x, y]).T.reshape(-1, 1, 2)
# segments3 = np.concatenate([points3[:-1], points3[1:]], axis=1)
# # Define gradient and plot pos vs speed graph
# norm3 = plt.Normalize(0, max(speed))
# lc3 = LineCollection(segments3, norm=norm3)
# lc3.set_array(np.array(speed))
# lc3.set_linewidth(1)
# line3 = ax2.add_collection(lc3)
# fig.colorbar(line3, ax=ax2)
# ax2.set_xlim(df.min()[0] - 400, df.max()[0] + 400)
# ax2.set_ylim(df.min()[1] - 400, df.max()[1] + 400)

# df = pandas.DataFrame(data={"time": modtime, "speed": modspeed})
# df.to_csv("./timevspeed.csv", sep=',', index=False)

print(totdistance)

# show plots
mplcursors.cursor()
plt.show()
