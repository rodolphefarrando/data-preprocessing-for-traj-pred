# data-preprocessing-for-traj-pred
Data preprocessing for the trajnet dataset for pedestrian trajectory prediction


Main goal: To create separate file for each trajectory and the trajectories that may interact with it. It also allows to visualize the trajectory either statically or dynamically (create gif).

Secondary goal: create new data by adding noise for the trajectories and create new columns with new features like speed.

The trajectories are classified according to six different criteria:
1. static trajectory without interaction
1. static trajectory with static interaction
1. static trajectory with dynamic interaction
1. dynamic trajectory without interaction
1. dynamic trajectory with static interaction
1. dynamic trajectory with dynamic interaction

