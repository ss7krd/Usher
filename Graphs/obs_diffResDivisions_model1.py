import matplotlib
import numpy as np
import pandas as pd
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 48})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.2     # the width of the bars

# fig = plt.figure()
# ax = fig.add_subplot(111)
fig, ax = plt.subplots(4, sharex='col', sharey = 'row')

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
# batchSize_time = (np.array([20,35,68,152]))

# comm_time = np.array([500, 400, 240, 220])
# comm_time = np.array([600, 520, 350, 332])
# comm_time = np.array([610, 525, 345, 370])
comm_time_3 = np.array([20, 30, 37, 45])
comm_time_2 = np.array([35, 39, 42, 48])
comm_time_1 = np.array([42, 48, 53, 57])
comm_time_0 = np.array([47, 51, 54, 59])
# dummy = [10.9,10.8,10.8,10.9]
# dummy2 = [2.2,2.3,2.2,2.2]

ax[3].bar(ind, comm_time_3, width, color=[(1,0.7,0)], hatch = '//', edgecolor='black')
ax[2].bar(ind, comm_time_2, width, color=[(1,0.7,0)], hatch = '//', edgecolor='black')
ax[1].bar(ind, comm_time_1, width, color=[(1,0.7,0)], hatch = '//', edgecolor='black')
ax[0].bar(ind, comm_time_0, width, color=[(1,0.7,0)], hatch = '//', edgecolor='black')

# ax.bar(ind, batchSize_time-comm_time, width, color='darkgrey', edgecolor='black', label='Computation time in\nGPU computation space', bottom = comm_time)
ax[3].set_title('Batch size=2',fontsize=38)
ax[2].set_title('Batch size=4',fontsize = 38)
ax[1].set_title('Batch size=8',fontsize = 38)
ax[0].set_title('Batch size=16',fontsize = 38)

ax[3].set_ylim(15, 65)
ax[2].set_ylim(15, 65)
ax[1].set_ylim(15, 65)
ax[0].set_ylim(15, 65)
# ytickvalues = []
# for i in range(70, 101, 5):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=32)
ax[3].set_xlabel('GPU computation space allocated to MobileNetv2')
# ax[0].set_ylabel('Latency (ms)', rotation='horizontal', ha='right', va='center')
fig.text(0.04,0.5, 'Required memory space (%)', va = 'center', rotation = "vertical")
# ax[2].set_ylabel('Latency (ms)')
# ax[1].set_ylabel('Latency (ms)')
# ax[0].set_ylabel('Latency (ms)')
# ax.set_xlabel('Number of other datasets in combination')
ax[3].set_xticks(ind)

xvalues = ["13%", "23%", "33%", "43%"]
ax[3].set_xticklabels(xvalues)

# yvalues = ["25%", "50%"]
# ax[3].set_yticklabels(yvalues)
# ax[2].set_yticklabels(yvalues)
# ax[1].set_yticklabels(yvalues)
# ax[0].set_yticklabels(yvalues)

box = ax[3].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[3].set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.15, box.width, box.height*0.85])
box = ax[2].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[2].set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.2, box.width, box.height*0.85])
box = ax[1].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[1].set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.25, box.width, box.height*0.85])
box = ax[0].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[0].set_position([box.x0 + box.width*0.05, box.y0 + box.height*0.3, box.width, box.height*0.85])
#bbox_to_anchor=(0.5, 1.6)
# leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.95), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
#             fontsize='48', ncol=1, handleheight=1.2, labelspacing=0.7, frameon=False)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()