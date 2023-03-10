from SMP.motion_planner.node import PriorityNode
from SMP.motion_planner.plot_config import DefaultPlotConfig
from SMP.motion_planner.search_algorithms.best_first_search import GreedyBestFirstSearch

import math
import numpy as np

class StudentMotionPlanner(GreedyBestFirstSearch):
    """
    Motion planner implementation by students.
    Note that you may inherit from any given motion planner as you wish, or come up with your own planner.
    Here as an example, the planner is inherited from the GreedyBestFirstSearch planner.
    """

    def __init__(self, scenario, planningProblem, automata, plot_config=DefaultPlotConfig):
        super().__init__(scenario=scenario, planningProblem=planningProblem, automaton=automata,
                         plot_config=plot_config)

    def evaluation_function(self, node_current: PriorityNode) -> float:
        #######################################################################
        # todo: Implement your own evaluation function here.                   #
        #######################################################################
        node_current.priority = self.heuristic_function(node_current=node_current)
        return node_current.priority
    

    def heuristic_function(self, node_current: PriorityNode) -> float:
        ########################################################################
        # todo: Implement your own heuristic cost calculation here.            #
        # Hint:                                                                #
        #   Use the State of the current node and the information from the     #
        #   planning problem, as well as from the scenario.                    #
        #   Some helper functions for your convenience can be found in         #
        #   ./search_algorithms/base_class.py                             #
        ########################################################################


        factor = 1 
        path_last = node_current.list_paths[-1]

        if self.reached_goal(path_last):
            return 0.0

        state_0 = self.planningProblem.goal.state_list[0]
        if hasattr(state_0, 'time_step'):
            time_start = state_0.time_step.start*0.75
            time_end = state_0.time_step.end*0.75
            time_mean_goal = time_start +time_end 
            
            last_time = path_last[-1].time_step
            if last_time > time_mean_goal:
                dist_time_min = np.inf 
                for iter in path_last:
                    dist_time = abs(iter.time_step - time_mean_goal)
                    if dist_time < dist_time_min: 
                        dist_time_min = dist_time

                dist_time = dist_time_min         
            else:
                dist_time = time_mean_goal - last_time
                
                
            distStartState = self.calc_heuristic_distance(path_last[0])
            distLastState = self.calc_heuristic_distance(path_last[-1])
            if (distLastState is None) or (distStartState < distLastState) :
                return np.inf
            if distLastState < 0.5:
                factor = factor * 0.00001

            
            orientationToGoalDiff_min = np.inf
            
            for state in path_last:
                angleToGoal = self.calc_angle_to_goal(state)
                orientationToGoalDiff = self.calc_orientation_diff(angleToGoal, state.orientation)
                if orientationToGoalDiff < orientationToGoalDiff_min: 
                    orientationToGoalDiff_min = orientationToGoalDiff
            orientationToGoalDiff = orientationToGoalDiff_min    
            
        else:
            dist_time = 0
            orientationToGoalDiff = 0 
            distLastState = 0
                  


        if hasattr(self.planningProblem.goal.state_list[0], 'velocity') and hasattr(self.planningProblem.goal.state_list[0], 'orientation'):
             
            cost_lanelet, final_lanelet_id, start_lanelet_id = self.calc_heuristic_lanelet(path_last)
            
            if start_lanelet_id is None or final_lanelet_id is None or cost_lanelet is None:
                return np.inf

            start_lanelet_cost = self.lanelet_cost[start_lanelet_id[0]]
            final_lanelet_cost = self.lanelet_cost[final_lanelet_id[0]]

            if  ((final_lanelet_cost == -1) or ( final_lanelet_cost > start_lanelet_cost ) ):
                return np.inf
            elif final_lanelet_cost < start_lanelet_cost:
                factor = factor * 0.1
            if self.is_goal_in_lane(final_lanelet_id[0]): 
                factor=factor*0.07
            pathLength = self.calc_travelled_distance(path_last)
            travel_dist_cost = 100 - pathLength 
            cost_time = self.calc_time_cost(path_last)

        else:
            dist_time = dist_time * 0.9
            cost_lanelet=0
            travel_dist_cost=0
            cost_time = 0
           
        if hasattr(self.planningProblem.goal.state_list[0], 'velocity'):   
            v_mean_goal = (self.planningProblem.goal.state_list[0].velocity.start + 
                           self.planningProblem.goal.state_list[0].velocity.end) / 2
            dist_vel = abs(path_last[-1].velocity - v_mean_goal)
        else:
            dist_vel = 0

            
        weigths = np.zeros(7) 
        weigths[0] = 9
        if abs(orientationToGoalDiff) > 1.1 and (distStartState >= distLastState):
            weigths[1] = 10
        else:
            weigths[1] = 0.02
        weigths[2] = 0.5
        weigths[3] = 0.06
        weigths[4] = 0.05
        weigths[5] = 1.2
        if distStartState < distLastState:
            weigths[6] = 11
        else: weigths[6] = 0.04; 
  

        cost = weigths[0] * (cost_lanelet / len(path_last)) + \
               weigths[1] * abs(orientationToGoalDiff) + \
               weigths[2] * distLastState + \
               weigths[3] * cost_time + \
               weigths[4] * travel_dist_cost + \
               weigths[5] * dist_vel + \
               weigths[6] * dist_time 
        
        if cost<0: 
            cost = 0                             
        return cost * factor