
import lunar_lockout_world
import sys
import problems

#problem_file = sys.argv[1]
#init_state = lunar_lockout_world.State([(4,4),(2,1),(4,0),(1,2),(3,3)])
#goal_state = [2,2]
#init_state = State([(2,0),(4,1),(0,1),(0,3),(4,3),(2,4)]) # 36

###############################################################
############ BREADTH FIRST SEARCH FOR LUNAR LOCKOUT ###########
###############################################################

problem = problems.Problems()
for i in range(len(problem.init_state_vector)):
    count = 0
    print "PROBLEM", problem.problem_map[i]
    init_state = lunar_lockout_world.State(problem.init_state_vector[i])    
    env = lunar_lockout_world.LunarLockout(init_state)
    open_list = []
    open_list.append((init_state, None, None, None, env.getNodeID(init_state)))
    print env.getNodeID(init_state)
    closed_list = {}
    
    while open_list:
        now = open_list.pop()
        count += 1
        closed_list[now[4]] = now
        if now[0].position[0] == problem.goal_state:
            break
        successor_list = env.getSuccessors(now[0])
        if successor_list:
            for successor in successor_list:
                if successor[4] not in closed_list:
                    open_list.append(successor)
    
    plan = []
    while env.getNodeID(init_state) != env.getNodeID(now[0]):
        plan.insert(0,now)
        now =  closed_list[env.getNodeID(now[1])]
    
    plan.insert(0, now)
    for node in plan:
        env.state_grid(node[0])
        print ''
        
    print "NUMBER OF STATES NEEDED", count