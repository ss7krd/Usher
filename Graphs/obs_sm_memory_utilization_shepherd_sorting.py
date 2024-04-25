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

# matplotlib.rcParams["figure.figsize"] = (8, 2)  # (4, 1.3)
# matplotlib.rcParams['pdf.fonttype'] = 42
# matplotlib.rcParams['ps.fonttype'] = 42

color_list = []
with open('color_pallete_for_obs_bars.txt','r') as color_file:
	for eachLine in color_file:
		color_list.append(eachLine.strip())

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 9
ind = np.arange(N)  # the x locations for the groups
width = 0.25 # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

stepX = [20,40,60,80,100,40,60,80,20,40,60,80]
nparrayStepX = np.array(stepX)
dummy = [0,0,0,0,0,0,0,0,0]

patterns = [ "/" , "/" , "/" , "-" , "+" , "x", "o", "/", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
# vals_igpr = pd.read_csv('rmse_vs_serverNo.csv')
# vals_ra = pd.read_csv('repartitionTime_data_vs_serverno.csv')
# vals_rla = pd.read_csv('replicationTime_data_vs_serverno.csv')
# vals_comp = pd.read_csv('completionTime_vs_serverNo.csv')
# vals__detection = pd.read_csv('detectionTime_data_each_comp.csv')
# vals_eachComp_reassignment = pd.read_csv('reassignmentTime_data_each_comp.csv')
shepherd_computation = (np.array([96,85,86,95,92,85,87,88,87]))-9
# proposed_igpr = (np.array([50,87,125,152]))

# proposed_ra = (np.array(vals_ra['proposed'].tolist())+0.2)*200*0.164
# proposed_rla = (np.array(vals_rla['proposed'].tolist())+0.45)*200*0.164
# proposed_igpr = np.array(vals_comp['proposed'].tolist())*180*0.164/1.1 - proposed_ra - proposed_rla
# proposed_igpr_ra = proposed_igpr + proposed_ra

# ax.bar(ind,proposed_igpr,width,color='r',edgecolor='black',hatch="+",label="Proposed(C)")
# ax.bar(ind,proposed_ra,width,color='bisque',edgecolor='black',hatch="+",label="Proposed(RA)",bottom=proposed_igpr)
# ax.bar(ind,proposed_igpr,width,color='yellow',edgecolor='black')
ax.bar(ind,shepherd_computation,width,color=color_list[0],hatch='+',edgecolor=color_list[0],fill=False,linewidth=2)
# ax.bar(ind,proposed_ra,width,color=[(1,0.7,0)],edgecolor='black',hatch="/",bottom=proposed_igpr)
# ax.bar(ind,proposed_rla,width,color=[(1,0.7,0)],edgecolor='black',hatch="-",bottom=proposed_igpr_ra)
# ax.bar(ind,dummy,width,color='white',edgecolor='black',bottom=proposed_igpr,label="E")

ax.bar(ind,dummy,width,color=color_list[0],edgecolor=color_list[0],hatch='+',fill=False,label="Computation utilization",linewidth=2)
# ax.bar(ind,dummy,width,color='lime',edgecolor='black',label="CSIR")
ax.bar(ind,dummy,width,color=color_list[1],edgecolor=color_list[1],hatch='',fill=True,label="Memory utilization",linewidth=2)
# ax.bar(ind,dummy,width,color='tomato',edgecolor='black',label="Early-exit version 2")
# ax.bar(ind,dummy,width,color='darkgrey',edgecolor='black',label="DESP/IF")
# ax.bar(ind,dummy,width,color='yellow',edgecolor='black',label="DESP/HB")
# ax.bar(ind,dummy,width,color='tomato',edgecolor='black',label="DESP/RA")
# ax.bar(ind,dummy,width,color='deepskyblue',edgecolor='black',label="DESP/RL")
# ax.bar(ind,dummy,width,color='lime',edgecolor='black',label="DESP/PC")
# ax.bar(ind,dummy,width,color='deepskyblue',edgecolor='black',label="Early-exit version 3")
# ax.bar(ind,dummy,width,color='white',edgecolor='black',hatch="/",label="RA")
# ax.bar(ind,dummy,width,color='white',edgecolor='black',hatch="-",label="RL")

# centralized_igpr = np.array(vals_igpr['centralized'].tolist())
# centralized_ra = np.array(vals_ra['centralized'].tolist())*360
# centralized_rla = np.array(vals_rla['centralized'].tolist())*360
# centralized_igpr_ra = centralized_igpr + centralized_ra

# ax.bar(ind+2*width,centralized_igpr,width,color='b',edgecolor='black',hatch="*",label="Centralized(C)")
# ax.bar(ind+2*width,centralized_ra,width,color='tan',edgecolor='black',hatch="*",bottom=centralized_igpr)
# ax.bar(ind+width,centralized_igpr,width,color='lime',edgecolor='black')
# ax.bar(ind+width,centralized_ra,width,color='lime',edgecolor='black',hatch="/")
# ax.bar(ind+width,centralized_rla,width,color='lime',edgecolor='black',hatch="-",bottom=centralized_ra)

# 96,95,96,45,97,94,41,38,95,42,97,94
# 89,89,89,89,89,89,89,89,88
# 96,85,86,95,92,85,87,88,87
shepherd_memory = (np.array([89,90,83,89,95,88,90,86,91]))-9
# static_ra = np.array(vals_ra['static'].tolist())*200*0.164
# static_rla = static_ra
# # static_igpr = np.array(vals_comp['static'].tolist())*180*0.164/1.1 - static_ra - static_rla
# static_igpr_ra = static_igpr + static_ra

# ax.bar(ind+4*width, static_igpr, width, color = 'cyan', edgecolor = 'black', hatch = 'o', label = "Static(C)")
# ax.bar(ind+4*width, static_ra, width, color = 'deeppink', edgecolor = 'black', hatch = 'o',bottom=static_igpr)
# ax.bar(ind+2*width, static_igpr, width, color = 'green', edgecolor = 'black')
ax.bar(ind+1*width, shepherd_memory, width, color = color_list[1], hatch='',edgecolor = color_list[1],fill=True,linewidth=2)
# ax.bar(ind+1*width, static_ra, width, color = 'deepskyblue', edgecolor = 'black', hatch = "/",bottom=static_igpr)
# ax.bar(ind+1*width, static_rla, width, color = 'deepskyblue', edgecolor = 'black', hatch = '-',bottom=static_igpr_ra)

# time_varying_igpr = (np.array([395,380,350,365]))
# time_varying_ra = (np.array(vals_ra['proposed_wo_ml'].tolist())+0.31)*200*0.164
# time_varying_rla = (np.array(vals_rla['proposed_wo_ml'].tolist())+0.54)*200*0.164
# # time_varying_igpr = np.array(vals_comp['time_varying'].tolist())*180*0.164/1.1 - time_varying_ra - time_varying_rla
# time_varying_igpr_ra = time_varying_igpr + time_varying_ra
# print(time_varying_igpr)
# print(time_varying_ra)
# print(time_varying_rla)

# ax.bar(ind+6*width, time_varying_igpr, width,color='purple', edgecolor='black',hatch='/o', label='Time_varying(C)')
# ax.bar(ind+6*width, time_varying_ra, width,color='palegreen', edgecolor='black',hatch='/o', label='Time_varying(RA)',bottom=time_varying_igpr)
# ax.bar(ind+3*width, time_varying_igpr, width,color='cyan', edgecolor='black')
# ax.bar(ind+2*width, time_varying_igpr, width,color='tomato', edgecolor='black')
# ax.bar(ind+2*width, time_varying_ra, width,color='cyan', edgecolor='black',hatch="/",bottom=time_varying_igpr)
# ax.bar(ind+2*width, time_varying_rla, width,color='cyan', edgecolor='black',hatch='-',bottom=time_varying_igpr_ra)

# proposed_wo_af_igpr = (np.array(vals_igpr['proposed_wo_af'].tolist()))
# proposed_wo_af_ra = (np.array(vals_ra['proposed_wo_af'].tolist())+0.2)*200*0.164
# proposed_wo_af_rla = (np.array(vals_rla['proposed_wo_af'].tolist())+0.45)*200*0.164
# # proposed_wo_af_igpr = np.array(vals_comp['proposed_wo_af'].tolist())*180*0.164/1.12 - proposed_wo_af_ra - proposed_wo_af_rla
# proposed_wo_af_igpr_ra = proposed_wo_af_igpr + proposed_wo_af_ra

# ax.bar(ind+8*width,proposed_wo_af_igpr,width,color='grey',edgecolor='black',hatch="x",label="Proposed/AF(C)")
# ax.bar(ind+8*width,proposed_wo_af_ra,width,color='khaki',edgecolor='black',hatch="x",label="Proposed/AF(RA)",bottom=proposed_wo_af_igpr)
# ax.bar(ind+4*width,proposed_wo_af_igpr,width,color='grey',edgecolor='black')
# ax.bar(ind+3*width,proposed_wo_af_igpr,width,color='darkgrey',edgecolor='black')
# ax.bar(ind+3*width,proposed_wo_af_ra,width,color='darkgrey',edgecolor='black',hatch="/",bottom=proposed_wo_af_igpr)
# ax.bar(ind+3*width,proposed_wo_af_rla,width,color='darkgrey',edgecolor='black',hatch="-",bottom=proposed_wo_af_igpr_ra)

# new_fl_detection = vals_detection['FL'].tolist()
# new_fl_reassignment = vals_reassignment['FL'].tolist()

# ax.bar(ind+3*width, new_fl_detection, width,color='purple', edgecolor='black',hatch='/o', label='BFL1(D)')
# ax.bar(ind+3*width, new_fl_reassignment, width,color='palegreen', edgecolor='black',hatch='/o', label='BFL1(R)',bottom=new_fl_detection)

# proposed_wo_hb_igpr = (np.array(vals_igpr['proposed_wo_hb'].tolist()))
# proposed_wo_hb_ra = (np.array(vals_ra['proposed'].tolist())+0.23)*200*0.164
# proposed_wo_hb_rla = (np.array(vals_rla['proposed'].tolist())+0.48)*200*0.164
# # proposed_wo_hb_igpr = np.array(vals_comp['proposed_wo_hb'].tolist())*180*0.164/1.1 - proposed_wo_hb_ra - proposed_wo_hb_rla
# proposed_wo_hb_igpr_ra = proposed_wo_hb_igpr + proposed_wo_hb_ra

# ax.bar(ind+1*width, proposed_wo_hb_igpr, width, color='red', edgecolor='black', hatch='\\|', label='Proposed/HB(C)')
# ax.bar(ind+1*width, proposed_wo_hb_ra, width, color='lightseagreen', edgecolor='black', hatch='\\|', label='Proposed/HB(RA)', bottom = proposed_wo_hb_igpr)
# ax.bar(ind+5*width, proposed_wo_hb_igpr, width, color='beige', edgecolor='black')
# ax.bar(ind+4*width, proposed_wo_hb_igpr, width, color='yellow', edgecolor='black')
# ax.bar(ind+4*width, proposed_wo_hb_ra, width, color='yellow', edgecolor='black', hatch="/",bottom=proposed_wo_hb_igpr)
# ax.bar(ind+11*width, proposed_wo_hb_igpr_ra, width, color='red', edgecolor='black', hatch='\\|')
# ax.bar(ind+4*width, proposed_wo_hb_rla, width, color='yellow', edgecolor='black', hatch='-', bottom = proposed_wo_hb_igpr_ra)
# rects4 = ax.bar(ind+width*3, drop, width, color = 'purple', edgecolor = 'black', hatch = '-', label = 'Drop')

#!!nicher parai change korte hobe


# our_system_wo_group_detection = vals_eachComp_detection['our_system_wo_group'].tolist()
# our_system_wo_group_reassignment = vals_eachComp_reassignment['our_system_wo_group'].tolist()

# ax.bar(ind+5*width,our_system_wo_group_detection,width,color='crimson',edgecolor='black',hatch="|*",label="TrustMe/H(D)")
# ax.bar(ind+5*width,our_system_wo_group_reassignment,width,color='lime',edgecolor='black',hatch="|*",label="TrustMe/H(R)", bottom = our_system_wo_group_detection)
# rects4 = ax.bar(ind+width*4, our_system_wo_group, width, color='b', edgecolor='black', hatch="*", label='Our System/G')

# proposed_wo_ra_igpr = (np.array(vals_igpr['proposed_wo_ra'].tolist()))
# proposed_wo_ra_ra = np.array(vals_ra['proposed_wo_ra'].tolist())*200*0.164
# proposed_wo_ra_rla = (np.array(vals_rla['proposed'].tolist())+0.445)*200*0.164
# # proposed_wo_ra_igpr = np.array(vals_comp['proposed_wo_ra'].tolist())*180*0.164/1.1 - proposed_wo_ra_ra - proposed_wo_ra_rla
# proposed_wo_ra_igpr_ra = proposed_wo_ra_igpr + proposed_wo_ra_ra

# ax.bar(ind+12*width,proposed_wo_ra_igpr,width,color='black',edgecolor='white',hatch="-\\",label="Proposed/RA(C)")
# ax.bar(ind+12*width,proposed_wo_ra_ra,width,color='beige',edgecolor='black',hatch="-\\", bottom = proposed_wo_ra_igpr)
# ax.bar(ind+6*width,proposed_wo_ra_igpr,width,color='lavender',edgecolor='black')
# ax.bar(ind+5*width,proposed_wo_ra_igpr,width,color='tomato',edgecolor='black')
# ax.bar(ind+5*width,proposed_wo_ra_ra,width,color='tomato',edgecolor='black',hatch="/",bottom=proposed_wo_ra_igpr)
# ax.bar(ind+13*width,proposed_wo_ra_igpr_ra,width,color='black',edgecolor='white',hatch="-\\")
# ax.bar(ind+5*width,proposed_wo_ra_rla,width,color='tomato',edgecolor='black',hatch="-", bottom = proposed_wo_ra_igpr_ra)
# rects5 = ax.bar(ind+width*5, our_system_wo_reassign, width, color='grey', edgecolor='black', hatch="x", label='Our System/R')

# proposed_wo_rl_igpr = (np.array(vals_igpr['proposed_wo_rl'].tolist()))
# proposed_wo_rl_ra = (np.array(vals_ra['proposed'].tolist())+0.21)*200*0.164
# proposed_wo_rl_rla = np.array(vals_rla['proposed_wo_rl'].tolist())*200*0.164
# # proposed_wo_rl_igpr = np.array(vals_comp['proposed_wo_rl'].tolist())*180*0.164/1.1 - proposed_wo_rl_ra - proposed_wo_rl_rla
# proposed_wo_rl_igpr_ra = proposed_wo_rl_igpr + proposed_wo_rl_ra

# ax.bar(ind+14*width,proposed_wo_rl_igpr,width,color='deepskyblue',edgecolor='black',hatch="+o",label="Proposed/RL(C)")
# ax.bar(ind+14*width,proposed_wo_rl_ra,width,color='cadetblue',edgecolor='black',hatch="+o",label="Proposed/RL(RA)", bottom = proposed_wo_rl_igpr)
# ax.bar(ind+7*width,proposed_wo_rl_igpr,width,color='brown',edgecolor='black')
# ax.bar(ind+6*width,proposed_wo_rl_igpr,width,color='deepskyblue',edgecolor='black')
# ax.bar(ind+6*width,proposed_wo_rl_ra,width,color='deepskyblue',edgecolor='black',hatch="/",bottom=proposed_wo_rl_igpr)
# ax.bar(ind+15*width,proposed_wo_rl_igpr_ra,width,color='deepskyblue',edgecolor='black',hatch="+o")
# ax.bar(ind+6*width,proposed_wo_rl_rla,width,color='deepskyblue',edgecolor='black',hatch="-", bottom = proposed_wo_rl_igpr_ra)

# proposed_wo_ml_igpr = (np.array(vals_igpr['proposed_wo_ml'].tolist()))
# proposed_wo_ml_ra = (np.array(vals_ra['proposed_wo_ml'].tolist())+0.309)*200*0.164
# proposed_wo_ml_rla = (np.array(vals_rla['proposed_wo_ml'].tolist())+0.539)*200*0.164
# # proposed_wo_ml_igpr = np.array(vals_comp['proposed_wo_ml'].tolist())*180*0.164/1.1 - proposed_wo_ml_ra - proposed_wo_ml_rla
# proposed_wo_ml_igpr_ra = proposed_wo_ml_igpr + proposed_wo_ml_ra

# ax.bar(ind+16*width,proposed_wo_ml_igpr,width,color='gold',edgecolor='black',hatch="x*",label="Proposed/ML(C)")
# ax.bar(ind+16*width,proposed_wo_ml_ra,width,color='thistle',edgecolor='black',hatch="x*",label="Proposed/ML(RA)",bottom=proposed_wo_ml_igpr)
# ax.bar(ind+8*width,proposed_wo_ml_igpr,width,color='deepskyblue',edgecolor='black')
# ax.bar(ind+7*width,proposed_wo_ml_igpr,width,color='lime',edgecolor='black')
# centralized_igpr = np.array([360,375,380,390])
# ax.bar(ind+3*width, centralized_igpr, width, color = 'deepskyblue', edgecolor = 'black')
# ax.bar(ind+7*width,proposed_wo_ml_ra,width,color='lime',edgecolor='black',hatch="/",bottom=proposed_wo_ml_igpr)
# ax.bar(ind+7*width,proposed_wo_ml_rla,width,color='lime',edgecolor='black',hatch="-",bottom=proposed_wo_ml_igpr_ra)

# our_system_wo_partial_task_detection = vals_eachComp_detection['our_system_wo_partial_task'].tolist()
# our_system_wo_partial_task_reassignment = vals_eachComp_reassignment['our_system_wo_partial_task'].tolist()

# ax.bar(ind+8*width, our_system_wo_partial_task_detection, width, color = 'cyan', edgecolor = 'black', hatch = 'o', label = "TrustMe/PT(D)")
# ax.bar(ind+8*width, our_system_wo_partial_task_reassignment, width, color = 'deeppink', edgecolor = 'black', hatch = 'o', label = "TrustMe/PT(R)",bottom=our_system_wo_partial_task_detection)

# # rects6 = ax.bar(ind+width*6, our_system_wo_partial_task, width, color = 'purple', edgecolor = 'black', hatch = 'o', label = 'Our System/PT')

# our_system_wo_all_task_detection = vals_eachComp_detection['our_system_wo_all_task'].tolist()
# our_system_wo_all_task_reassignment = vals_eachComp_reassignment['our_system_wo_all_task'].tolist()

# ax.bar(ind+9*width, our_system_wo_all_task_detection, width, color = 'blue', edgecolor='black',hatch = 'o-', label = "TrustMe/AT(D)")
# ax.bar(ind+9*width, our_system_wo_all_task_reassignment, width, color = 'lavender', edgecolor='black',hatch = 'o-', label = "TrustMe/AT(R)",bottom=our_system_wo_all_task_detection)
# # rects5 = ax.bar(ind+width*7, our_system_wo_all_task, width, color = 'blue', edgecolor = 'black', hatch = 'O', label = 'Our System/AT')


# our_system_wo_syn_data_detection = vals_eachComp_detection['our_system_wo_syn_data'].tolist()
# our_system_wo_syn_data_reassignment = vals_eachComp_reassignment['our_system_wo_syn_data'].tolist()

# ax.bar(ind+1*width, our_system_wo_syn_data_detection, width, color = 'g', edgecolor='black',hatch = 'O|', label = "TrustMe/SD(D)")
# ax.bar(ind+1*width, our_system_wo_syn_data_reassignment, width, color = 'tomato', edgecolor='black',hatch = 'O|', label = "TrustMe/SD(R)",bottom=our_system_wo_syn_data_detection)
# rects6 = ax.bar(ind+width*8, our_system_wo_syn_data, width, color = 'lightgreen', edgecolor = 'black', hatch = '-', label = 'Our System/SD')
# h2tdrValues_knn = vals['h2tdrValues_knn'].tolist()

# # twelvekValuesModified = []
# # for i in twelvekValues:
# #     j = (i/100.0)*10400
# #     twelvekValuesModified.append(j)

# rects4 = ax.bar(ind+width*3, h2tdrValues_knn, width, color='g', edgecolor='black', hatch="o")

# xvalueNames = ["Step 1","Step 2","Step 3","Step 4","Step 5","Step 6","Step 7","Step 8", "Step 9", "Step 1"]

ax.set_ylabel('Utilization')
ax.set_xlabel("GPUs")
# ax.set_xlabel('Request batch size')
ax.set_xticks(ind+0.5*width)
# ax.set_ylim(0.7,1.45)

# ax.set_ylim(0,.5)


# ax.set_ylim(0,4500)
# ax.set_xticks(ind+4*width)
#ax.set_xticklabels(vals['error_type'].tolist())

# xvalues = [5, 1, 15, 20, 25, 1]
xvalues = ["G1","G2","G3","G4","G5","G6","G7","G8","G9"]

ax.set_ylim(35, 100)
ax.set_yticks([50, 75, 100])
yvalues = ["50%", "75%", "100%"]
ax.set_yticklabels(yvalues)

# plt.xticks(xvalues)
# plt.xticks(xvalues)
ax.set_xticklabels(xvalues, rotation = 45)
ax.grid(color='lightgrey', linestyle='dashed', axis="y", linewidth=2)

# ax.set_ylim(70, 100)
ytickvalues = []
# for i in range(70, 105, 1):
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

ytickvalues = []

box = ax.get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax.set_position([box.x0 + box.width*0.1, box.y0 + box.height*0.2, box.width, box.height*0.68])
#bbox_to_anchor=(0.5, 1.6)
leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.5), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
            fontsize='60', ncol=1, handleheight=1, labelspacing=0.2, frameon=False) 

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

plt.show()