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

N = 12
ind = np.arange(N)  # the x locations for the groups
width = 0.25 # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

stepX = [20,40,60,80,100,40,60,80,20,40,60,80]
nparrayStepX = np.array(stepX)
dummy = [0,0,0,0,0,0,0,0,0,0,0,0]

patterns = [ "/" , "/" , "/" , "-" , "+" , "x", "o", "/", ".", "*" ]

# stepX=[1,2,3,4,5,6]
#DRAWING VERTICAL CHARTS
# vals_igpr = pd.read_csv('rmse_vs_serverNo.csv')
# vals_ra = pd.read_csv('repartitionTime_data_vs_serverno.csv')
# vals_rla = pd.read_csv('replicationTime_data_vs_serverno.csv')
# vals_comp = pd.read_csv('completionTime_vs_serverNo.csv')
# vals__detection = pd.read_csv('detectionTime_data_each_comp.csv')
# vals_eachComp_reassignment = pd.read_csv('reassignmentTime_data_each_comp.csv')
shepherd_computation = (np.array([96,95,96,45,97,94,41,38,95,42,97,94]))
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
ax.bar(ind,dummy,width,color=color_list[1],edgecolor=color_list[1],hatch='/',fill=False,label="Memory utilization",linewidth=2)
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
shepherd_memory = (np.array([70,68,65,97,72,69,52,50,69,50,68,70]))
# static_ra = np.array(vals_ra['static'].tolist())*200*0.164
# static_rla = static_ra
# # static_igpr = np.array(vals_comp['static'].tolist())*180*0.164/1.1 - static_ra - static_rla
# static_igpr_ra = static_igpr + static_ra

# ax.bar(ind+4*width, static_igpr, width, color = 'cyan', edgecolor = 'black', hatch = 'o', label = "Static(C)")
# ax.bar(ind+4*width, static_ra, width, color = 'deeppink', edgecolor = 'black', hatch = 'o',bottom=static_igpr)
# ax.bar(ind+2*width, static_igpr, width, color = 'green', edgecolor = 'black')
ax.bar(ind+1*width, shepherd_memory, width, color = color_list[1], hatch='/',edgecolor = color_list[1],fill=False,linewidth=2)


ax.set_ylabel('Utilization')
ax.set_xlabel("GPUs")

ax.set_xticks(ind+0.5*width)

xvalues = ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12"]

ax.set_yticks([25, 50, 75, 100])
yvalues = ["25%", "50%", "75%", "100%"]

ax.set_yticklabels(yvalues)

ax.set_xticklabels(xvalues, rotation = 45)

ax.grid(color='lightgrey', linestyle='dashed', axis="y", linewidth=2)

# ax.set_ylim(70, 100)
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

# plt.tight_layout()
# # fig.savefig(f'utilization_latency_tradeoff.png', bbox_inches='tight', dpi=500)
# fig.savefig(f'obs_sm_memory_utilization_shepherd_default.pdf', bbox_inches='tight', dpi=500)
# plt.close()