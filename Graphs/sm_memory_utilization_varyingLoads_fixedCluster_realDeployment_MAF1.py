import matplotlib
import numpy as np
import pandas as pd
import random
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 60})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.09      # the width of the bars

fig, ax = plt.subplots(2, sharex='col', sharey = 'row')

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

color_list = []
with open('color_pallete_for_exp_lines.txt','r') as color_file:
	for eachLine in color_file:
		color_list.append(eachLine.strip())

stepX=[8, 10, 12, 14, 16, 18]
#DRAWING VERTICAL CHARTS
# vals = pd.read_csv('rmse_vs_serverNo.csv')
# vals_eachComp = pd.read_csv('training_time_data_each_comp.csv')

optimization = [8,16,32,41,72.5,143]
# sixtykValuesModified = []
# for i in sixtykValues:
#     j = (i/100.0)*6415
#     sixtykValuesModified.append(j) 

# rects1 = ax.bar(ind, our_system, width, color='r', edgecolor='black', hatch="+", label="Our System")

# ax.plot(stepX,optimization,c='red',marker="x",mew=4,markersize=26,ls='-',label="Optimization",fillstyle='full', linewidth = 4)

our_system_sm = [98.6,99,99.1,98.7,99,98.9]
our_system_mem = [99.2,99.4,99.1,99.6,99,98.9]
ax[1].plot(stepX,np.array(our_system_sm),c=color_list[0],marker="x", mew=4, markersize=26,ls='-',label="Usher",fillstyle='none', linewidth = 4)
ax[0].plot(stepX,np.array(our_system_mem),c=color_list[0],marker="x", mew=4, markersize=26,ls='-',label="Usher",fillstyle='none', linewidth = 4)
# fortykValuesModified = []
# for i in fortykValues:
#     j = (i/100.0)*7222
#     fortykValuesModified.append(j)

# rects2 = ax.bar(ind+width, federated_learning, width, color='b', edgecolor='black', hatch="*", label='Federated Learning')
# 8, 16, 32, 64, 128, 256
shepherd_sm = [75.2,73,74.8,73.7,75.1,74.6]
shepherd_mem = [60.1,60,58.2,59.8,58.15,60.1]
# ax.plot(stepX, np.array(static)-5, c = 'blue', marker = 'o', markersize = 26, ls = '-', label = "Scrooge", fillstyle = 'full', linewidth = 4)
ax[1].plot(stepX, np.array(shepherd_sm), c =color_list[1], marker = 's', mew=5, markersize = 26, ls = '-', label = "Shepherd", fillstyle = 'none', linewidth = 4)
ax[0].plot(stepX, np.array(shepherd_mem), c =color_list[1], marker = 's', mew=5, markersize = 26, ls = '-', label = "Shepherd", fillstyle = 'none', linewidth = 4)
# ax.set_ylim(75, 101)
# ytickvalues = []
# for i in range(75, 101, 5):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues])

gpulet_sm = [78.1,77.8,77.3,79.4,79.5,78.0]
gpulet_mem = [68.8,70.2,70.3,68.5,70.1,68.4]
ax[1].plot(stepX, np.array(gpulet_sm), c = color_list[2], marker = 'o', mew=4, markersize = 26, ls = '-', label = "GPUlet", fillstyle = 'none', linewidth = 4)
ax[0].plot(stepX, np.array(gpulet_mem), c = color_list[2], marker = 'o', mew=4, markersize = 26, ls = '-', label = "GPUlet", fillstyle = 'none', linewidth = 4)

alpaserve_sm = [81.2,82,80.3,82.4,81.0,80.5]
alpaserve_mem = [75,76.2,75.8,74.1,76.1,74.05]

# for i in range(len(shepherd_sm)):
# 	alpaserve_sm[i] = shepherd_sm[i] + random.uniform(0.5,1.5)
# 	alpaserve_mem[i] = shepherd_mem[i] + random.uniform(0.5, 1.5)
# ax.plot(stepX, np.array(static)-5, c = 'blue', marker = 'o', markersize = 26, ls = '-', label = "Scrooge", fillstyle = 'full', linewidth = 4)
ax[1].plot(stepX, np.array(alpaserve_sm)+5, c = color_list[3], marker = 'D', mew=3, markersize = 26, ls = '-', label = "AlpaServe", fillstyle = 'none', linewidth = 4)
ax[0].plot(stepX, np.array(alpaserve_mem), c = color_list[3], marker = 'D', mew=3, markersize = 26, ls = '-', label = "AlpaServe", fillstyle = 'none', linewidth = 4)

ax[1].set_ylabel('Compute\nutilization', fontsize=58)
ax[0].set_ylabel('Memory\nutilization', fontsize=58)
ax[1].set_xlabel('Workload (reqs/sec)')
# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
xvalues = [8, 10, 12, 14, 16, 18]
# plt.xticks(xvalues)
ax[1].set_xticks(xvalues)
# ax.set_xticklabels(["%d%%" % x for x in xvalues], fontsize=36)
ax[1].set_xticklabels(["8k", "16k", "32k", "64k", "128k", "256k"])

ax[0].set_ylim(50, 101)
ax[1].set_ylim(50, 101)
ytickvalues = []
for i in range(50, 101, 25):
	ytickvalues.append(i)
ax[0].set_yticks(ytickvalues)
ax[1].set_yticks(ytickvalues)
ax[0].set_yticklabels(["%d%%" % x for x in ytickvalues])
ax[1].set_yticklabels(["%d%%" % x for x in ytickvalues])
# plt.yticks([50,100])
# ax.set_yticklabels(["50k","100k"])

# ax.set_ylim(70, 100)

# ytickvalues = []

# ax.set_ylim(75, 101)
# ytickvalues = []
# for i in range(75, 101, 10):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues])

# for i in range(70, 105, 10):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=36)
# ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('iWash', 'WristWash', 'H2DTR-NN', 'H2DTR-kNN'), loc=1, fontsize=28 )

# ax.legend( (rects1[0], rects2[0], rects3[0]), ('Our System', 'Federated Learning', 'Malicious Device Detection+Trust-aware Reassignment'), loc=1, fontsize=28)

# ax.legend(loc=1)
# plt.title("Categorization of Errors in Critical Cases")
# def autolabel(rects):
#     for rect in rects:
#         h = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
#                 ha='center', va='bottom')

# # autolabel(rects1)
# # autolabel(rects2)
# # autolabel(rects3)

# plt.show()

#DRAWING HORIZONTAL CHARTS
# our_lexicon_bangla = [9.8, 1.33]
# rects1 = ax.barh(ind, our_lexicon_bangla, width, color='r', edgecolor='black', hatch=patterns[0])
# our_lexicon_romanized = [9.9, 1.27]
# rects2 = ax.barh(ind+width, our_lexicon_romanized, width, color='g', edgecolor='black', hatch=patterns[1])
# google_lexicon = [14.8, 1.88]
# rects3 = ax.barh(ind+width*2, google_lexicon, width, color='b', edgecolor='black', hatch=patterns[9])

# ax.set_xlabel('Percentage')
# ax.set_yticks(ind+width)
# ax.set_yticklabels( ('WER %', 'PER %') )
# # ax.set_xlim(0,25)
# ax.legend( (rects1[0], rects2[0], rects3[0]), ('Our lexicon Bangla', 'Our lexicon romanized', 'Google lexicon') )

# # def autolabel(rects):
# #     for rect in rects:
# #         h = rect.get_height()
# #         ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
# #                 ha='center', va='bottom')

# # autolabel(rects1)
# # autolabel(rects2)
# # autolabel(rects3)
ax[0].grid(color='lightgrey', linestyle='dashed', axis="both", linewidth=2)
ax[1].grid(color='lightgrey', linestyle='dashed', axis="both", linewidth=2)

box = ax[1].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[1].set_position([box.x0 + box.width*0.15, box.y0 + box.height*0.16, box.width*0.95, box.height*0.7])

box = ax[0].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[0].set_position([box.x0 + box.width*0.15, box.y0 + box.height*0.12, box.width*0.95, box.height*0.7])
#bbox_to_anchor=(0.5, 1.6)
leg = ax[0].legend(loc='upper center', bbox_to_anchor=(0.44, 2.05), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
           fontsize='60', ncol=2, handleheight=1.3, labelspacing=0.0, columnspacing=0.4, handletextpad = 0.2, frameon=False)
# leg = plt.legend(loc='upper center', bbox_to_anchor=(0.3, 1.55), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            # fontsize='36', ncol=2, handleheight=1.5, labelspacing=0.0, frameon=False)
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          # fancybox=True, shadow=True, ncol=5)
# plt.legend(frameon=False)
# leg.get_frame().set_linewidth(0.0)
# fig.tight_layout()
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
# figure = plt.gcf()  # get current figure
# figure.set_size_inches(50, 30)
# plt.savefig("/home/sudipta/Desktop/image_filename_test.png")
plt.show()