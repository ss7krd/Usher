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

N = 2
ind = np.arange(N)  # the x locations for the groups
width = 0.25      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
# dummy_1 = [98, 100]#Acc.
# dummy_1 = [98, 100]
# dummy_1 = [98, 100]
dummy_1 = [98, 100]
dummy = [0,0]
# dummy_2 = [232,240] #latency
# dummy_2 = [278,350]
# dummy_2 = [266,345]
dummy_2 = [320,341]
# vals = pd.read_csv('accuracy_data_until_converge.csv')
# vals_eachComp = pd.read_csv('accuracy_data_each_comp.csv')
# dummy_1[0] = vals['our_system'].tolist()[5]
# dummy_1[1] = vals_eachComp['our_system_wo_reassign'].tolist()[5]
# dummy_1[2] = vals_eachComp['our_system_wo_ir'].tolist()[5]
# dummy_1[3] = vals_eachComp['our_system_wo_ie'].tolist()[5]
# dummy_1[4] = vals_eachComp['our_system_wo_partial_task'].tolist()[5]
# dummy_1[5] = vals_eachComp['our_system_wo_all_task'].tolist()[5]
# dummy_1[6] = vals_eachComp['our_system_wo_syn_data'].tolist()[5]
# print(dummy_1)

# vals = pd.read_csv('training_time_data_until_converge.csv')
# vals_eachComp = pd.read_csv('training_time_data_each_comp.csv')
# dummy_2[0] = vals['our_system'].tolist()[5]/10-5
# dummy_2[1] = vals_eachComp['our_system_wo_reassign'].tolist()[5]/10-5
# dummy_2[2] = vals_eachComp['our_system_wo_ir'].tolist()[5]/10-5
# dummy_2[3] = vals_eachComp['our_system_wo_ie'].tolist()[5]/10-5
# dummy_2[4] = vals_eachComp['our_system_wo_partial_task'].tolist()[5]/10-5
# dummy_2[5] = vals_eachComp['our_system_wo_all_task'].tolist()[5]/10-5
# dummy_2[6] = dummy_2[0] - 2.9
#detection: cpu, reassignment: memory
# vals_detection = pd.read_csv('cpu_data_until_converge_1.csv')
# vals_reassignment = pd.read_csv('cpu_data_until_converge_1.csv')
# vals_bw = pd.read_csv('cpu_data_until_converge_1.csv')

# vals_eachComp_detection = pd.read_csv('cpu_data_each_comp_1.csv')
# vals_eachComp_reassignment = pd.read_csv('cpu_data_each_comp_1.csv')
# vals_eachComp_bw = pd.read_csv('cpu_data_each_comp_1.csv')

# our_system_detection = np.array(vals_detection['our_system'].tolist())/100
# our_system_reassignment = np.array(vals_reassignment['our_system'].tolist())/100-0.06
# our_system_bw = np.array(vals_bw['our_system'].tolist())/100+0.05

ax.bar(ind,dummy_1,width,color='darkgrey',edgecolor='black')
# ax.bar(ind,our_system_reassignment,width,color='yellow',edgecolor='black',hatch="O",bottom=our_system_detection)
# ax.bar(ind,our_system_bw,width,color='yellow',edgecolor='black',hatch="-",bottom=our_system_detection+our_system_reassignment)
# ax.bar(ind,dummy,width,color='yellow',edgecolor='black')
ax.bar(ind,dummy,width,color='darkgrey',edgecolor='black',label="Accuracy")
ax.bar(ind,dummy,width,color='deepskyblue',edgecolor='black',label="Overall latency (ms)")
# ax.bar(ind,dummy,width,color='white',edgecolor='black',label="Bandwidth",hatch="-")
# ax.bar(ind,dummy,width,color='yellow',edgecolor='black',label="TrustMe")




ax2.bar(ind+width,dummy_2,width,color='deepskyblue',edgecolor='black')
# ax.bar(ind+width,federated_learning_reassignment,width,color='lime',edgecolor='black',hatch="O",bottom=federated_learning_detection)
# ax.bar(ind+width,federated_learning_bw,width,color='lime',edgecolor='black',hatch="-",bottom=federated_learning_detection+federated_learning_reassignment)

# ax.set_ylim(85, 103)
# ax2.set_ylim(40, 50)

# ytickvalues = []
# for i in range(85, 105, 5):
# 	ytickvalues.append(i)
# ax.set_yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=36)

ax.set_ylabel('Accuracy')
ax2.set_ylabel('Overall latency (ms)')
# ax.set_xlabel(r'$\alpha$')
ax.set_xticks(ind+0.5*width)

# ax.set_ylim(0,.5)
ax.set_ylim(90, 103)
ax2.set_ylim(250, 400)
ytickvalues = []
for i in range(70, 105, 10):
	ytickvalues.append(i)
ax.set_yticks(ytickvalues)
ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=48)

# ax2.set_ylim(0, 500)
# ytickvalues = []
# for i in range(0, 500, 200):
# 	ytickvalues.append(i)
# plt.yticks(ytickvalues)
# ax.set_yticklabels(["%d%%" % x for x in ytickvalues], fontsize=48)
# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 10, 15, 20, 25, 30]
# xvalues = [0.45, 0.5, 0.55, 0.6]
# plt.xticks(xvalues)
# plt.xticks(xvalues)
ax.set_xticklabels(['FP16', 'FP32'],fontsize=48)

# ax.set_ylim(70, 100)
ytickvalues = []
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
ax.set_position([box.x0 + box.width*0.04, box.y0 + box.height*0.04, box.width*0.88, box.height*0.65])
#bbox_to_anchor=(0.5, 1.6)
leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.45), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='48', ncol=3, handleheight=1.3, labelspacing=0.0, frameon=False) 
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