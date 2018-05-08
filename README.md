# data-preprocessing-for-traj-pred
Data preprocessing for the trajnet dataset for pedestrian trajectory prediction


Main goal: To create separate file for each trajectory and the trajectories that may interact with it. It also allows to visualize the trajectory either statically or dynamically (create gif).



Secondary goal: create new data by adding noise for the trajectories and create new columns with new features like speed.

Trajectory prediction has now some state-of-art methods. Number of papers analyses the accuracy of those methods. (Add references and talk about the methods ?). Beyond their respective performance, there is always some cases for which the methods are struggling with the prediction. The idea is to separare trajectories by type, that is the way the pedestrian is moving and the way her/his environement interacts with her/him.

The trajectories are classified according to six different criteria:
1. static trajectory without interaction
1. static trajectory with static interaction
1. static trajectory with dynamic interaction
1. dynamic trajectory without interaction
1. dynamic trajectory with static interaction
1. dynamic trajectory with dynamic interaction

By static we mean a pedestrian travelling less than two meters during the twenty frames (8 seconds and so less than 0.25 m/s) provided by the data. 


![alt text | width=50](/figure/0_biwi_md.png?raw=true "Type1")
