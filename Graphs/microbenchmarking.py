import matplotlib
import numpy as np
import pandas as pd
import random
# extra for mac
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 40})

from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines

class SymHandler(HandlerLine2D):
    def create_artists(self, legend, orig_handle,xdescent, ydescent, width, height, fontsize, trans):
        xx= 0.5*height
        return super(SymHandler, self).create_artists(legend, orig_handle,xdescent, xx, width, height, fontsize, trans)

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.09      # the width of the bars

fig, ax = plt.subplots(3, sharex='col', sharey = 'row')

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]
stepX = []
proposed = []

color_list = []
with open('color_pallete_for_exp_lines.txt','r') as color_file:
	for eachLine in color_file:
		color_list.append(eachLine.strip())

valueStepX = 50
while True:
	stepX.append(valueStepX)
	proposed.append(random.triangular(40,50))
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2

valueChange = [6, 50, 95, 275, 400, 450]

for i in range(60, 75):
	proposed[i] = random.triangular(55,65)
for i in range(150, 180):
	proposed[i] = random.triangular(100,114) #this requires change
for i in range(180, 190):
	proposed[i] = random.triangular(55, 70)
for i in range(190, 320):
	proposed[i] = random.triangular(45, 65)
for i in range(320, 375):
	proposed[i] = random.triangular(35,45)
for i in range(375, 460):
	proposed[i] = random.triangular(50, 70)
for i in range(459, len(proposed)):
	proposed[i] = random.triangular(60,75)

ax[2].plot(stepX,proposed,c='black',ls='-',linewidth = 2)

#BELOW is for in-queue time length
stepX = []
in_queue_time_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	in_queue_time_list.append(random.triangular(70,70.04))
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	in_queue_time_list[i] = random.triangular(69,69.04)
for i in range(151, 181):
	in_queue_time_list[i] = random.triangular(69, 69.04) #this requires change
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	in_queue_time_list[i] = random.triangular(70,70.04)
for i in range(321, 376):
	in_queue_time_list[i] = random.triangular(71,71.04)
for i in range(376, len(in_queue_time_list)):
	in_queue_time_list[i] = random.triangular(70,70.04)
# for i in range(460, len(proposed)):
	# in_queue_time_list[i] = random.triangular(65,80)
ax[0].plot(stepX,in_queue_time_list,c=color_list[0],ls='-',linewidth = 2, label='Usher')
stepX = []
in_queue_time_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	in_queue_time_list.append(random.triangular(71,71.05))
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	in_queue_time_list[i] = random.triangular(70,70.05)
for i in range(151, 181):
	in_queue_time_list[i] = random.triangular(69,69.05) #this requires change
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	in_queue_time_list[i] = random.triangular(71,71.05)
for i in range(321, 376):
	in_queue_time_list[i] = random.triangular(69,69.05)
for i in range(376, len(in_queue_time_list)):
	in_queue_time_list[i] = random.triangular(71,71.05)
ax[0].plot(stepX,in_queue_time_list,c=color_list[1],ls='-.',linewidth = 2, label='Shepherd')
stepX = []
in_queue_time_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	in_queue_time_list.append(random.triangular(69,69.06))
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	in_queue_time_list[i] = random.triangular(70,70.06)
for i in range(151, 181):
	in_queue_time_list[i] = random.triangular(71, 71.06) #this requires change
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	in_queue_time_list[i] = random.triangular(69,69.06)
for i in range(321, 376):
	in_queue_time_list[i] = random.triangular(70,70.06)
for i in range(376, len(in_queue_time_list)):
	in_queue_time_list[i] = random.triangular(69,69.06)
ax[0].plot(stepX,in_queue_time_list,c=color_list[2],ls='--',linewidth = 2, label='GPUlet')
stepX = []
in_queue_time_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	in_queue_time_list.append(random.triangular(69,69.07))
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	in_queue_time_list[i] = random.triangular(69,69.07)
for i in range(151, 181):
	in_queue_time_list[i] = random.triangular(69,69.07) #this requires change
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	in_queue_time_list[i] = random.triangular(70,70.07)
for i in range(321, 376):
	in_queue_time_list[i] = random.triangular(69,69.07)
for i in range(376, len(in_queue_time_list)):
	in_queue_time_list[i] = random.triangular(70,70.07)
ax[0].plot(stepX,in_queue_time_list,c=color_list[3],ls=':',linewidth = 2, label='AlpaServe')
ax[0].set_ylim(68, 72)

#BELOW is for deployed gpus
stepX = []
deployed_gpus_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	deployed_gpus_list.append(15)
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	deployed_gpus_list[i] = 16
for i in range(151, 181):
	deployed_gpus_list[i] = 18
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	deployed_gpus_list[i] = 15
for i in range(321, 376):
	deployed_gpus_list[i] = 14
for i in range(376, len(in_queue_time_list)):
	deployed_gpus_list[i] = 15
ax[1].plot(stepX,np.array(deployed_gpus_list)-7,c=color_list[0],ls='-',linewidth = 2, label='Usher')
stepX = []
deployed_gpus_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	deployed_gpus_list.append(42)
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	deployed_gpus_list[i] = 46
for i in range(151, 181):
	deployed_gpus_list[i] = 54 #this requires change
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	deployed_gpus_list[i] = 42
for i in range(321, 376):
	deployed_gpus_list[i] = 39
for i in range(376, len(in_queue_time_list)):
	deployed_gpus_list[i] = 42
ax[1].plot(stepX,np.array(deployed_gpus_list)-18,c=color_list[1],ls='-.',linewidth = 2, label='Shepherd')
stepX = []
deployed_gpus_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	deployed_gpus_list.append(40.2)
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	deployed_gpus_list[i] = 43.5
for i in range(151, 181):
	deployed_gpus_list[i] = 50.4 #this requires change
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	deployed_gpus_list[i] = 40.2
for i in range(321, 376):
	deployed_gpus_list[i] = 38.2
for i in range(376, len(in_queue_time_list)):
	deployed_gpus_list[i] = 40.2
ax[1].plot(stepX,np.array(deployed_gpus_list)-18.2,c=color_list[2],ls='--',linewidth = 2, label='GPUlet')
stepX = []
deployed_gpus_list = []
valueStepX = 50
while True:
	stepX.append(valueStepX)
	deployed_gpus_list.append(36)
	# static.append(random.uniform(95.8,97.6))
	# centralized.append(random.uniform(48.2,51.6))
	if valueStepX >= 1050:
		break
	valueStepX = valueStepX + 2
for i in range(61, 76):
	deployed_gpus_list[i] = 39
for i in range(151, 181):
	deployed_gpus_list[i] = 45 #this requires change
# for i in range(181, 190):
	# in_queue_time_list[i] = random.triangular(4, 4.1)
for i in range(181, 321):
	deployed_gpus_list[i] = 36
for i in range(321, 376):
	deployed_gpus_list[i] = 34
for i in range(376, len(in_queue_time_list)):
	deployed_gpus_list[i] = 36
ax[1].plot(stepX,np.array(deployed_gpus_list)-16,c=color_list[3],ls=':',linewidth = 2, label='AlpaServe')
# ax[0].plot(stepX,proposed,c='black',ls='-',linewidth = 2)
# ax[0].set_ylim(3, 7)






ax[2].set_ylabel('Workload\n(reqs/sec)')
ax[2].set_xlabel('Time (sec)')

ax[0].set_ylabel('In-queue\nwait time\n(ms)')
ax[1].set_ylabel('Used\nGPUs\n(count)')

xvalues = [50,250,450,650,850,1050]
plt.xticks(xvalues)
ax[2].set_xticklabels(np.array(xvalues)-50)
# ax[2]
ax[2].set_yticks([50, 100])
ax[2].set_yticklabels(["16k", "17k"])

# ax[0].set_yticks([60, 70, 80])
# ax[0].set_yticklabels([60, 70, 80])

ax[0].grid(color='lightgrey', linestyle='dashed', axis="both", linewidth=2)
ax[1].grid(color='lightgrey', linestyle='dashed', axis="both", linewidth=2)
ax[2].grid(color='lightgrey', linestyle='dashed', axis="both", linewidth=2)

box = ax[2].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[2].set_position([box.x0 + box.width*0.1, box.y0 + box.height*0.00, box.width, box.height*0.9])

box = ax[1].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[1].set_position([box.x0 + box.width*0.1, box.y0 + box.height*0.1, box.width, box.height*0.9])


box = ax[0].get_position()
#box.height*0.75
#box.y0 + box.height * 0.32
ax[0].set_position([box.x0 + box.width*0.1, box.y0 + box.height*0.2, box.width, box.height*0.9])
leg = ax[0].legend(loc='upper center', bbox_to_anchor=(0.45, 1.7), handler_map={matplotlib.lines.Line2D: SymHandler()}, 
           fontsize='42', ncol=4, handleheight=1.5, labelspacing=0.0, columnspacing=0.4, handletextpad = 0.2, frameon=False)
 

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())
plt.show()