import matplotlib
import numpy as np
import pandas as pd
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 60})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

matplotlib.rcParams['hatch.linewidth'] = 2

color_list = []
with open('color_pallete_for_obs_bars.txt','r') as color_file:
	for eachLine in color_file:
		color_list.append(eachLine.strip())

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.25     # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
# batchSize_time = (np.array([20,35,68,152]))

# comm_time = np.array([500, 400, 240, 220])
# comm_time = np.array([600, 520, 350, 332])
# comm_time = np.array([610, 525, 345, 370])
comm_time = np.array([2, 8, 56, 34])

# dummy = [10.9,10.8,10.8,10.9]
# dummy2 = [2.2,2.3,2.2,2.2]

ax.bar(ind,comm_time,width,color=color_list[2],hatch='x',edgecolor=color_list[2],fill=False,linewidth=2)
# ax.bar(ind, batchSize_time-comm_time, width, color='darkgrey', edgecolor='black', label='Computation time in\nGPU computation space', bottom = comm_time)

# ax.set_ylim(335, 615)
# ytickvalues = []
# for i in range(70, 101, 5):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=32)
ax.set_xlabel('Number of GPU kernel APIs called')
ax.set_ylabel('Operators')
# ax.set_xlabel('Number of other datasets in combination')
ax.set_xticks(ind)

xvalues = [1, 2, 3, 4]
ax.set_xticklabels(xvalues)

ax.set_yticks([20, 40, 60])
yvalues = ["20%", "40%", "60%"]
ax.set_yticklabels(yvalues)

ax.grid(color='lightgrey', linestyle='dashed', axis="y", linewidth=2)

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.25, box.width, box.height*0.6])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.95), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='48', ncol=1, handleheight=1.2, labelspacing=0.7, frameon=False)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()