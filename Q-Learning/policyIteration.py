import numpy

discount = 0.5
probs = [[0.05, 0.05, 0.9], [0.25, 0.5, 0.25], [0.01, 0.02, 0.97]]
numActions = len(probs)

rewards = [1, -1, 0] # [None, Against, For]
init_policy = [1, 2, 0] # [Balanced = 0 , Offensive = 1, Defensive = 2]
policy = init_policy

state_values = [0, 0, 0]

def updatePolicy(policy):
	currentPolicy = policy
	for i in range(len(state_values)):
		sum = 0
		for j in range(len(state_values)):
			sum += probs[currentPolicy[i]][j]*state_values[j]
		state_values[i] = rewards[i] + discount * sum
	vals = [0]*numActions
	for i in range(len(state_values)):
		for j in range(numActions):
			sum = 0
			for k in range(len(state_values)):
				sum += probs[j][k]*state_values[k]
			vals[j] = rewards[i] + discount*sum
		currentPolicy[i] =  vals.index(max(vals))
	#print "policy", policy	
	return currentPolicy

i = 0
while (1):	
	new_policy = updatePolicy(policy)
	i+=1
	if (new_policy == policy):
		break
	policy = new_policy

print new_policy