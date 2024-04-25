import matplotlib
import numpy as np
import pandas as pd
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

fig = plt.figure()
ax = fig.add_subplot(111)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

color_list = []
with open('color_pallete_for_exp_lines.txt','r') as color_file:
	for eachLine in color_file:
		color_list.append(eachLine.strip())

stepX=[10, 12, 14, 16, 18]
#DRAWING VERTICAL CHARTS
# vals = pd.read_csv('rmse_vs_serverNo.csv')
# vals_eachComp = pd.read_csv('training_time_data_each_comp.csv')

#!!FEEDBACK: IN GENERAL COST ARO BARAITE HOBE

optimization = [8,16,32,41,72.5,143]
# sixtykValuesModified = []
# for i in sixtykValues:
#     j = (i/100.0)*6415
#     sixtykValuesModified.append(j) 

# rects1 = ax.bar(ind, our_system, width, color='r', edgecolor='black', hatch="+", label="Our System")

# ax.plot(stepX,optimization,c='red',marker="x",mew=4,markersize=26,ls='-',label="Optimization",fillstyle='full', linewidth = 4)

divider = 8
# our_system = [48,48,62,85,85,132]
our_system = [73.44,122,200,240,385]#[336: 8 A100 + 3 V100, so heterogeneous better, also higher capacity GPU types preferred]
ax.plot(stepX,np.array(our_system)/divider+3.06,c=color_list[0],marker="x", mew=4, markersize=26,ls='-',label="Usher",fillstyle='none', linewidth = 4)

# fortykValuesModified = []
# for i in fortykValues:
#     j = (i/100.0)*7222
#     fortykValuesModified.append(j)

# rects2 = ax.bar(ind+width, federated_learning, width, color='b', edgecolor='black', hatch="*", label='Federated Learning')
# 8, 16, 32, 64, 128, 256
shepherd = [260,260,310,360]
shepherd = np.array(shepherd)*2.2
# ax.plot(stepX, np.array(static)-5, c = 'blue', marker = 'o', markersize = 26, ls = '-', label = "Scrooge", fillstyle = 'full', linewidth = 4)
ax.plot(stepX[:-1], np.array(shepherd)/divider+3.06, c =color_list[1], marker = 's', mew=5, markersize = 26, ls = '-', label = "Shepherd", fillstyle = 'none', linewidth = 4)

gpulet = [230,250,275,350]
gpulet = np.array(gpulet)*2.2
# ax.plot(stepX, np.array(static)-5, c = 'blue', marker = 'o', markersize = 26, ls = '-', label = "Scrooge", fillstyle = 'full', linewidth = 4)
ax.plot(stepX[:-1], np.array(gpulet)/divider+3.06, c = color_list[2], marker = 'o', mew=4, markersize = 26, ls = '-', label = "GPUlet", fillstyle = 'none', linewidth = 4)

alpaserve = [170,200,250,300]
alpaserve = np.array(alpaserve)*2.2
# ax.plot(stepX, np.array(static)-5, c = 'blue', marker = 'o', markersize = 26, ls = '-', label = "Scrooge", fillstyle = 'full', linewidth = 4)
ax.plot(stepX[:-1], np.array(alpaserve)/divider+3.06, c = color_list[3], marker = 'D', mew=3, markersize = 26, ls = '-', label = "AlpaServe", fillstyle = 'none', linewidth = 4)

ax.set_ylabel('Cost/hr')
ax.set_xlabel('Workload (reqs/sec)')
# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
xvalues = [10, 12, 14, 16, 18]
# plt.xticks(xvalues)
plt.xticks(xvalues)
# ax.set_xticklabels(["%d%%" % x for x in xvalues], fontsize=36)
# ax.set_xticklabels(["8k", "16k", "32k", "64k", "128k", "256k"])
ax.set_xticklabels(["2k", "4k", "8k", "16k", "32k"])

plt.yticks([25, 50, 75, 100])
ax.set_yticklabels(["25$", "50$", "75$", "100$"])
plt.axhline(y = 105, color = 'green', linestyle = '--', linewidth = 2)

ax.grid(color='lightgrey', linestyle='dashed', axis="both", linewidth=2)

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

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0 + box.width*0.08, box.y0 + box.height*0.09, box.width, box.height*0.75])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.44, 1.5), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
           fontsize='60', ncol=2, handleheight=1.5, labelspacing=0.0, columnspacing=0.4, handletextpad = 0.2, frameon=False) 
# leg = plt.legend(loc='upper center', bbox_to_anchor=(0.3, 1.55), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            # fontsize='36', ncol=2, handleheight=1.5, labelspacing=0.0, frameon=False)
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          # fancybox=True, shadow=True, ncol=5)
# plt.legend(frameon=False)
# leg.get_frame().set_linewidth(0.0)
# fig.tight_layout()
# plt.tight_layout()

# plt.tight_layout()
# # fig.savefig(f'utilization_latency_tradeoff.png', bbox_inches='tight', dpi=500)
# fig.savefig(f'goodput_varyingLoads_fixedCluster_realDeployment_MAF1.pdf', bbox_inches='tight', dpi=500)
# plt.close()

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

# figure = plt.gcf()  # get current figure
# figure.set_size_inches(50, 30)
# plt.savefig("/home/sudipta/Desktop/image_filename_test.png")

plt.show()