# data-preprocessing-for-traj-pred
Data preprocessing for the trajnet dataset for pedestrian trajectory prediction


Main goal: To create separate file for each trajectory and the trajectories that may interact with it. It also allows to visualize the trajectory either statically or dynamically (create gif).



Secondary goal: create new data by adding noise for the trajectories and create new columns with new features like speed.

Trajectory prediction has now some state-of-art methods. Number of papers analyses the accuracy of those methods. (Add references and talk about the methods ?). Beyond their respective performance, there is always some cases for which the methods are struggling with the prediction. The idea is to separate trajectories by type, that is the way the pedestrian is moving and the way her/his environment interacts with her/him.

The trajectories are classified according to six different criteria:
1. static trajectory without interaction
1. static trajectory with static interaction
1. static trajectory with dynamic interaction
1. dynamic trajectory without interaction
1. dynamic trajectory with static interaction
1. dynamic trajectory with dynamic interaction

By static we mean a pedestrian travelling less than two meters during the twenty frames (8 seconds and so less than 0.25 m/s) provided by the data. 

Example of type 1 trajectory.

<img src="/figure/0_biwi_md.png?raw=true" width="500">


Example of type 2 trajectory.

<img src="/figure/6_biwi_md.png?raw=true" width="500">


Example of type 3 trajectory.

<img src="/figure/15_biwi_md.png?raw=true" width="500">


Example of type 4 trajectory.

<img src="/figure/22_biwi_md.png?raw=true" width="500">


Example of type 5 trajectory.

<img src="/figure/54_cr1_md.png?raw=true" width="500">


Example of type 6 trajectory.

<img src="/figure/120_biwi_md.png?raw=true" width="500">


To better see interaction between trajectories a dynamic plot is also implemented. It creates a .gif file that makes trajectories appear depending on the frame. The following gif shows the same figure as type 6 trajectory dynamically:

![Alt Text](/figure/dyn_120_biwi.gif?raw=true)
