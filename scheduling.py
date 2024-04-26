import sys
import os
import numpy as np
import math
import numpy as np
import pandas

possible_batch_sizes = [2, 4, 8, 16, 32, 64, 128]
possible_model_concurrency = [2, 4, 6, 8, 10, 12, 14, 16]
total_num_of_models_in_a_group = 4

possible_model_concurrency.reverse()

list_batchSize_modelConcurrency_combination = []

for batch_size in possible_batch_sizes:
	for model_concurrency in possible_model_concurrency:
		new_tuple = (batch_size, model_concurrency)
		list_batchSize_modelConcurrency_combination.append(new_tuple)

finishRate_threshold = 1
groupOfModels_id_finalConfigs = []
groupOfModels_id_whichGPUs = []

dummyList = []

total_num_of_models = total_num_of_models_in_a_group*len(groupOfModels)
list_whichGPUs_for_a_model = []
list_whichGPUs_for_a_model_highest_SM_utilization = []
list_whichGPUs_for_a_model_highest_memory_utilization = []

for modelId in range(1, total_num_of_models + 1):
	list_whichGPUs_for_a_model.append(dummyList)
	list_whichGPUs_for_a_model_highest_SM_utilization.append(dummyList)
	list_whichGPUs_for_a_model_highest_memory_utilization.append(dummyList)

for groupId in range(0, len(groupOfModels)):
	groupOfModels_id_whichGPUs.append(dummyList)

nextNewGPUId = 0


list_GPUTypes = []
list_whichGroupOfModelsId = []

list_whichModels_for_a_GPU = []
list_whichModels_for_a_GPU_highest_SM_utilization = []
list_whichModels_for_a_GPU_highest_memory_utilization = []
list_current_GPU_SM_utilization = []
list_current_GPU_memory_utilization = []

groupOfModels_id = 0

for eachGroup in groupOfModels:
	modelId1 = eachGroup[0]
	modelId2 = eachGroup[1]
	modelId3 = eachGroup[3]
	modelId4 = eachGroup[4]

	minCost = DOUBLE_MAX
	config_saved = (list_batchSize_modelConcurrency_combination[0], list_batchSize_modelConcurrency_combination[0], list_batchSize_modelConcurrency_combination[0], list_batchSize_modelConcurrency_combination[0])

	for modelId1_config in list_batchSize_modelConcurrency_combination:
		for modelId2_config in list_batchSize_modelConcurrency_combination:
			for modelId3_config in list_batchSize_modelConcurrency_combination:
				for modelId4_config in list_batchSize_modelConcurrency_combination:
					total_cost, goodput = placement_algorithm(modelId1_config, modelId2_config, modelId3_config, modelId4_config, modelId1, modelId2, modelId3, modelId4, groupOfModels_id)
					if goodput/currentRPS >= finishRate_threshold:
						if total_cost < minCost:
							minCost = total_cost
							config_saved = (modelId1_config, modelId2_config, modelId3_config, modelId4_config)
	
	groupOfModels_id_finalConfigs.append(config_saved)
	final_placement_algorithm(config_saved[0], config_saved[1], config_saved[2], config_saved[3],  modelId1, modelId2, modelId3, modelId4, groupOfModels_id)
	groupOfModels_id = groupOfModels_id + 1

def placement_algorithm (modelId1_config, modelId2_config, modelId3_config, modelId4_config, modelId1, modelId2, modelId3, modelId4, groupOfModels_id):
	previous_list_GPUTypes = list_GPUTypes
	previous_list_whichGroupOfModelsId = list_whichGroupOfModelsId
	previous_nextNewGPUId = nextNewGPUId
	previous_list_whichGPUs_for_a_model = list_whichGPUs_for_a_model
	previous_list_whichModels_for_a_GPU = list_whichModels_for_a_GPU
	previous_list_current_GPU_SM_utilization = list_current_GPU_SM_utilization
	previous_list_current_GPU_memory_utilization = list_current_GPU_memory_utilization
	# previous_list_modelConcurriencies_unallocated = list_modelConcurriencies_unallocated

	modelId1_how_many_concurriencies = modelId1_config[1]
	modelId2_how_many_concurriencies = modelId2_config[1]
	modelId3_how_many_concurriencies = modelId3_config[1]
	modelId4_how_many_concurriencies = modelId4_config[1]

	modelId1_batchSize = modelId1_config[0]
	modelId2_batchSize = modelId2_config[0]
	modelId3_batchSize = modelId3_config[0]
	modelId4_batchSize = modelId4_config[0]

	list_modelConcurriencies_unallocated = {}
	list_modelConcurriencies_unallocated[modelId1] = modelId1_how_many_concurriencies
	list_modelConcurriencies_unallocated[modelId2] = modelId2_how_many_concurriencies
	list_modelConcurriencies_unallocated[modelId3] = modelId3_how_many_concurriencies
	list_modelConcurriencies_unallocated[modelId4] = modelId4_how_many_concurriencies


	class ModelId_GPUType:
		self_modelId = None
		self_batchSize = None
		self_modelConcurrency = None
		self_GPUType = None
		self_SMreq = None
		self_memoryReq = None
		self_SM_memory_score = None

		def __init__(self, modelId, batchSize, modelConcurrency, GPUType):
			self.self_modelId = modelId
			self.self_batchSize = batchSize
			self.self_modelConcurrency = modelConcurrency
			self.self_GPUType = GPUType

	ModelId_GPUType_list = []

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId1, modelId1_batchSize, modelId1_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId2, modelId2_batchSize, modelId2_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId3, modelId3_batchSize, modelId3_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId4, modelId4_batchSize, modelId4_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)


	for i in range(0, len(ModelId_GPUType_list)):
		current_ModelId_GPUType_object = ModelId_GPUType_list[i]
		current_ModelId_GPUType_object.self_SMreq = #SM_req
		current_ModelId_GPUType_object.self_memoryReq = #memory_req
		current_ModelId_GPUType_object.self_SM_memory_score = #

	ModelId_GPUType_list.sort(key=lambda x: x.self_SM_memory_score, reverse = True)

	for i in range(0, len(ModelId_GPUType_list)):
		current_ModelId_GPUType_object = ModelId_GPUType_list[i]
		current_GPUgroup = groupOfModels_id_whichGPUs[groupOfModels_id]

		

		for j in range(0, list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId]):
			current_GPUgroup_shortlisted_GPUs = []
			for k in current_GPUgroup:
				current_GPUType = list_GPUTypes[k]
				if current_GPUType == current_ModelId_GPUType_object.self_GPUType:
					current_GPU_SM_utilization_remaining = 100-list_current_GPU_SM_utilization[k]
					list_current_GPU_memory_utilization_remaining = 100 - list_current_GPU_memory_utilization[k]

					if (current_GPU_SM_utilization_remaining >= current_ModelId_GPUType_object.self_SMreq and current_GPU_memory_utilization_remaining >= current_ModelId_GPUType_object.self_memoryReq):
						score_howMuchResourceRemaining = current_GPU_SM_utilization_remaining - current_ModelId_GPUType_object.self_SMreq + current_GPU_memory_utilization_remaining - current_ModelId_GPUType_object.self_memoryReq
						current_GPUgroup_shortlisted_GPUs.append((k, score_howMuchResourceRemaining))
			if (len(current_GPUgroup_shortlisted_GPUs) > 0):
				current_GPUgroup_shortlisted_GPUs.sort(key=lambda x:x[1])
				#assign happen;
				chosenGPUId = current_GPUgroup_shortlisted_GPUs[0]
				list_whichGPUs_for_a_model[current_ModelId_GPUType_object.self_modelId].append(chosenGPUId)
				list_whichModels_for_a_GPU[chosenGPUId].append(current_ModelId_GPUType_object)
				list_current_GPU_SM_utilization[chosenGPUId] = list_current_GPU_SM_utilization + current_ModelId_GPUType_object.self_SMreq
				list_current_GPU_memory_utilization[chosenGPUId] = list_current_GPU_memory_utilization + current_ModelId_GPUType_object.self_memoryReq
				list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId] -= 1
			else:
				current_GPUgroup_shortlisted_GPUs = []
				for GPUId in range(0, nextNewGPUId):
					if GPUId in current_GPUgroup:
						continue
					current_GPUType = list_GPUTypes[GPUId]
					if current_GPUType == current_ModelId_GPUType_object.self_GPUType:
						current_GPU_SM_utilization_remaining = 100-list_current_GPU_SM_utilization[k]
						list_current_GPU_memory_utilization_remaining = 100 - list_current_GPU_memory_utilization[k]

						if (current_GPU_SM_utilization_remaining >= current_ModelId_GPUType_object.self_SMreq and current_GPU_memory_utilization_remaining >= current_ModelId_GPUType_object.self_memoryReq):
							score_howMuchResourceRemaining = current_GPU_SM_utilization_remaining - current_ModelId_GPUType_object.self_SMreq + current_GPU_memory_utilization_remaining - current_ModelId_GPUType_object.self_memoryReq
							current_GPUgroup_shortlisted_GPUs.append((k, score_howMuchResourceRemaining))
				if (len(current_GPUgroup_shortlisted_GPUs) > 0):
					current_GPUgroup_shortlisted_GPUs.sort(key=lambda x:x[1])
					#assign happen;
					chosenGPUId = current_GPUgroup_shortlisted_GPUs[0]
					list_whichGPUs_for_a_model[current_ModelId_GPUType_object.self_modelId].append(chosenGPUId)
					list_whichModels_for_a_GPU[chosenGPUId].append(current_ModelId_GPUType_object)
					list_current_GPU_SM_utilization[chosenGPUId] = list_current_GPU_SM_utilization + current_ModelId_GPUType_object.self_SMreq
					list_current_GPU_memory_utilization[chosenGPUId] = list_current_GPU_memory_utilization + current_ModelId_GPUType_object.self_memoryReq
					list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId] -= 1	

				else:
					no_action = 1

	#new gpu
	tot_cost = 0
	for i in range(0, list_modelConcurriencies_unallocated[modelId1]): 
		shortlisted_newGPUs = []
		for gpuType in range(0, totalGPUTypes):
			how_much_time = #time_duration_find_for_a_batchsize
			goodput = modelId1_batchSize/how_much_time
			if goodput/additional_currentRPS_list[modelId1] >= finishRate_threshold:
				shortlisted_newGPUs.append(gpuType)
		minCost = 1e10
		minGPUType = -1
		for j in range(0, len(shortlisted_newGPUs)):
			current_gpuType = shortlisted_newGPUs[j]
			if cost[current_gpuType] < minCost:
				minCost = cost[current_gpuType]
				minGPUType = current_gpuType
		tot_cost += minCost
		#assign-2
		list_GPUTypes.append(minGPUType)
		list_whichGroupOfModelsId.append(groupOfModels_id)
		list_whichModels_for_a_GPU.append(dummyList)
		list_current_GPU_SM_utilization.append(0)
		list_current_GPU_memory_utilization.append(0)
		nextNewGPUId += 1

		chosenGPUId = nextNewGPUId - 1
		list_whichGPUs_for_a_model[modelId1].append(chosenGPUId)
		new_object = ModelId_GPUType(modelId1, modelId1_batchSize, modelId1_how_many_concurriencies, minGPUType)
		list_whichModels_for_a_GPU[chosenGPUId].append(new_object)
		new_object.self_SMreq = #
		new_object.self_memoryReq = #
		list_current_GPU_SM_utilization[chosenGPUId] = list_current_GPU_SM_utilization + new_object.self_SMreq
		list_current_GPU_memory_utilization[chosenGPUId] = list_current_GPU_memory_utilization + new_object.self_memoryReq
		list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId] -= 1



	
	

	#goodput finding.
	how_many_requests_withinSLO = {}
	how_many_requests_withinSLO[modelId1] = 0
	how_many_requests_withinSLO[modelId2] = 0
	how_many_requests_withinSLO[modelId3] = 0
	how_many_requests_withinSLO[modelId4] = 0

	how_much_time = {}
	how_much_time[modelId1] = -10000
	how_much_time[modelId2] = -10000
	how_much_time[modelId3] = -10000
	how_much_time[modelId4] = -10000

	for gpuId in range(0, nextNewGPUId):
		whichModels_gpuId_objects = list_whichModels_for_a_GPU[gpuId]
		for whichModel_object in whichModels_gpuId_objects:
			whichModel_object_modelId = whichModel_object.self_modelId
			whichModel_object_timeDuration = #time_duration_find_for_a_batchsize
			whichModel_object_batchSize = whichModel_object.self_batchSize
			how_many_requests_withinSLO[whichModel_object_modelId] += whichModel_object_batchSize
			how_much_time[whichModel_object_modelId] = max(how_much_time[whichModel_object_modelId], whichModel_object_timeDuration)


	avg_goodput = 0
	for modelId in how_many_requests_withinSLO:
		avg_goodput += how_many_requests_withinSLO[modelId]/how_much_time[modelId]
	avg_goodput = avg_goodput/4

	list_GPUTypes = previous_list_GPUTypes
	list_whichGroupOfModelsId = previous_list_whichGroupOfModelsId
	nextNewGPUId = previous_nextNewGPUId
	list_whichGPUs_for_a_model = previous_list_whichGPUs_for_a_model
	list_whichModels_for_a_GPU = previous_list_whichModels_for_a_GPU
	list_current_GPU_SM_utilization = previous_list_current_GPU_SM_utilization
	list_current_GPU_memory_utilization = previous_list_current_GPU_memory_utilization

	return tot_cost, avg_goodput

def final_placement_algorithm (modelId1_config, modelId2_config, modelId3_config, modelId4_config, modelId1, modelId2, modelId3, modelId4, groupOfModels_id):


	modelId1_how_many_concurriencies = modelId1_config[1]
	modelId2_how_many_concurriencies = modelId2_config[1]
	modelId3_how_many_concurriencies = modelId3_config[1]
	modelId4_how_many_concurriencies = modelId4_config[1]

	modelId1_batchSize = modelId1_config[0]
	modelId2_batchSize = modelId2_config[0]
	modelId3_batchSize = modelId3_config[0]
	modelId4_batchSize = modelId4_config[0]

	list_modelConcurriencies_unallocated = {}
	list_modelConcurriencies_unallocated[modelId1] = modelId1_how_many_concurriencies
	list_modelConcurriencies_unallocated[modelId2] = modelId2_how_many_concurriencies
	list_modelConcurriencies_unallocated[modelId3] = modelId3_how_many_concurriencies
	list_modelConcurriencies_unallocated[modelId4] = modelId4_how_many_concurriencies
	tot_cost = 0

	class ModelId_GPUType:
		self_modelId = None
		self_batchSize = None
		self_modelConcurrency = None
		self_GPUType = None
		self_SMreq = None
		self_memoryReq = None
		self_SM_memory_score = None

		def __init__(self, modelId, batchSize, modelConcurrency, GPUType):
			self.self_modelId = modelId
			self.self_batchSize = batchSize
			self.self_modelConcurrency = modelConcurrency
			self.self_GPUType = GPUType

	ModelId_GPUType_list = []

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId1, modelId1_batchSize, modelId1_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId2, modelId2_batchSize, modelId2_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId3, modelId3_batchSize, modelId3_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)

	for i in range(0, total_no_of_GPUTypes):
		new_object = ModelId_GPUType(modelId4, modelId4_batchSize, modelId4_how_many_concurriencies, i)
		ModelId_GPUType_list.append(new_object)


	for i in range(0, len(ModelId_GPUType_list)):
		current_ModelId_GPUType_object = ModelId_GPUType_list[i]
		current_ModelId_GPUType_object.self_SMreq = #SM_req
		current_ModelId_GPUType_object.self_memoryReq = #memory_req
		current_ModelId_GPUType_object.self_SM_memory_score = #

	ModelId_GPUType_list.sort(key=lambda x: x.self_SM_memory_score, reverse = True)

	for i in range(0, len(ModelId_GPUType_list)):
		current_ModelId_GPUType_object = ModelId_GPUType_list[i]
		current_GPUgroup = groupOfModels_id_whichGPUs[groupOfModels_id]

		

		for j in range(0, list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId]):
			current_GPUgroup_shortlisted_GPUs = []
			for k in current_GPUgroup:
				current_GPUType = list_GPUTypes[k]
				if current_GPUType == current_ModelId_GPUType_object.self_GPUType:
					current_GPU_SM_utilization_remaining = 100-list_current_GPU_SM_utilization[k]
					list_current_GPU_memory_utilization_remaining = 100 - list_current_GPU_memory_utilization[k]

					if (current_GPU_SM_utilization_remaining >= current_ModelId_GPUType_object.self_SMreq and current_GPU_memory_utilization_remaining >= current_ModelId_GPUType_object.self_memoryReq):
						score_howMuchResourceRemaining = current_GPU_SM_utilization_remaining - current_ModelId_GPUType_object.self_SMreq + current_GPU_memory_utilization_remaining - current_ModelId_GPUType_object.self_memoryReq
						current_GPUgroup_shortlisted_GPUs.append((k, score_howMuchResourceRemaining))
			if (len(current_GPUgroup_shortlisted_GPUs) > 0):
				current_GPUgroup_shortlisted_GPUs.sort(key=lambda x:x[1])
				#assign happen;
				chosenGPUId = current_GPUgroup_shortlisted_GPUs[0]
				list_whichGPUs_for_a_model[current_ModelId_GPUType_object.self_modelId].append(chosenGPUId)
				list_whichModels_for_a_GPU[chosenGPUId].append(current_ModelId_GPUType_object)
				list_current_GPU_SM_utilization[chosenGPUId] = list_current_GPU_SM_utilization + current_ModelId_GPUType_object.self_SMreq
				list_current_GPU_memory_utilization[chosenGPUId] = list_current_GPU_memory_utilization + current_ModelId_GPUType_object.self_memoryReq
				list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId] -= 1
			else:
				current_GPUgroup_shortlisted_GPUs = []
				for GPUId in range(0, nextNewGPUId):
					if GPUId in current_GPUgroup:
						continue
					current_GPUType = list_GPUTypes[GPUId]
					if current_GPUType == current_ModelId_GPUType_object.self_GPUType:
						current_GPU_SM_utilization_remaining = 100-list_current_GPU_SM_utilization[k]
						list_current_GPU_memory_utilization_remaining = 100 - list_current_GPU_memory_utilization[k]

						if (current_GPU_SM_utilization_remaining >= current_ModelId_GPUType_object.self_SMreq and current_GPU_memory_utilization_remaining >= current_ModelId_GPUType_object.self_memoryReq):
							score_howMuchResourceRemaining = current_GPU_SM_utilization_remaining - current_ModelId_GPUType_object.self_SMreq + current_GPU_memory_utilization_remaining - current_ModelId_GPUType_object.self_memoryReq
							current_GPUgroup_shortlisted_GPUs.append((k, score_howMuchResourceRemaining))
				if (len(current_GPUgroup_shortlisted_GPUs) > 0):
					current_GPUgroup_shortlisted_GPUs.sort(key=lambda x:x[1])
					#assign happen;
					chosenGPUId = current_GPUgroup_shortlisted_GPUs[0]
					list_whichGPUs_for_a_model[current_ModelId_GPUType_object.self_modelId].append(chosenGPUId)
					list_whichModels_for_a_GPU[chosenGPUId].append(current_ModelId_GPUType_object)
					list_current_GPU_SM_utilization[chosenGPUId] = list_current_GPU_SM_utilization + current_ModelId_GPUType_object.self_SMreq
					list_current_GPU_memory_utilization[chosenGPUId] = list_current_GPU_memory_utilization + current_ModelId_GPUType_object.self_memoryReq
					list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId] -= 1	

				else:
					no_action = 1

	for i in range(0, list_modelConcurriencies_unallocated[modelId1]): 
		shortlisted_newGPUs = []
		for gpuType in range(0, totalGPUTypes):
			how_much_time = #time_duration_find_for_a_batchsize
			goodput = modelId1_batchSize/how_much_time
			if goodput/additional_currentRPS_list[modelId1] >= finishRate_threshold:
				shortlisted_newGPUs.append(gpuType)
		minCost = 1e10
		minGPUType = -1
		for j in range(0, len(shortlisted_newGPUs)):
			current_gpuType = shortlisted_newGPUs[j]
			if cost[current_gpuType] < minCost:
				minCost = cost[current_gpuType]
				minGPUType = current_gpuType
		tot_cost += minCost
		#assign-2
		list_GPUTypes.append(minGPUType)
		list_whichGroupOfModelsId.append(groupOfModels_id)
		list_whichModels_for_a_GPU.append(dummyList)
		list_current_GPU_SM_utilization.append(0)
		list_current_GPU_memory_utilization.append(0)
		nextNewGPUId += 1

		chosenGPUId = nextNewGPUId - 1
		list_whichGPUs_for_a_model[modelId1].append(chosenGPUId)
		new_object = ModelId_GPUType(modelId1, modelId1_batchSize, modelId1_how_many_concurriencies, minGPUType)
		list_whichModels_for_a_GPU[chosenGPUId].append(new_object)
		new_object.self_SMreq = #
		new_object.self_memoryReq = #
		list_current_GPU_SM_utilization[chosenGPUId] = list_current_GPU_SM_utilization + new_object.self_SMreq
		list_current_GPU_memory_utilization[chosenGPUId] = list_current_GPU_memory_utilization + new_object.self_memoryReq
		list_modelConcurriencies_unallocated[current_ModelId_GPUType_object.self_modelId] -= 1

	#goodput finding.
	how_many_requests_withinSLO = {}
	how_many_requests_withinSLO[modelId1] = 0
	how_many_requests_withinSLO[modelId2] = 0
	how_many_requests_withinSLO[modelId3] = 0
	how_many_requests_withinSLO[modelId4] = 0

	how_much_time = {}
	how_much_time[modelId1] = -10000
	how_much_time[modelId2] = -10000
	how_much_time[modelId3] = -10000
	how_much_time[modelId4] = -10000

	for gpuId in range(0, nextNewGPUId):
		whichModels_gpuId_objects = list_whichModels_for_a_GPU[gpuId]
		for whichModel_object in whichModels_gpuId_objects:
			whichModel_object_modelId = whichModel_object.self_modelId
			whichModel_object_timeDuration = #time_duration_find_for_a_batchsize
			whichModel_object_batchSize = whichModel_object.self_batchSize
			how_many_requests_withinSLO[whichModel_object_modelId] += whichModel_object_batchSize
			how_much_time[whichModel_object_modelId] = max(how_much_time[whichModel_object_modelId], whichModel_object_timeDuration)


	avg_goodput = 0
	for modelId in how_many_requests_withinSLO:
		avg_goodput += how_many_requests_withinSLO[modelId]/how_much_time[modelId]
	avg_goodput = avg_goodput/4



	return tot_cost, avg_goodput














