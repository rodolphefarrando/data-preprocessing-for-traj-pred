# data-preprocessing-for-traj-pred
Data preprocessing for the trajnet dataset for pedestrian trajectory prediction

Main goal: To create a separate file for each trajectory and the trajectories that may interact with it. It also allows visualizing the trajectory either statically or dynamically (create gif).

Secondary goal: create new data by adding noise to the trajectories and create new columns with new features like speed.

Trajectory prediction has now some state-of-art methods. Several papers analyses the accuracy of those methods. (Add references and talk about the methods ?). Beyond their respective performance, there is always some cases for which the methods are struggling with the prediction. The idea is to separate trajectories by type, that is the way the pedestrian is moving and the way her/his environment interacts with her/him.

To have a better visualization of the trajectories and simplify learning, all of them are normalized. The first point is shifted towards the origin (0,0) and the trajectory is rotated such that the first segment (between first and second point) is pointing upwards:

Before shift and rotation:

<img src="/figure/beforerot.png?raw=true" width="500">

After shift and rotation:

<img src="/figure/afterrot.png?raw=true" width="500">


Two ways of classification are possible for the trajectories. The first one focuses more on interactions around the trajectory of interest, while the second one focuses on the direction of the trajectory.

For the interaction classification, six different criteria are possible for the trajectories:
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

For the direction classification, three criteria are defined:

1. static trajectory
1. linear trajectory
1. non-linear trajectory





To better see the interaction between trajectories a dynamic plot is also implemented. It creates a .gif file that makes trajectories appear depending on the frame. The following gif shows the same figure as type 6 trajectory dynamically:

<img src="/figure/dyn_120_biwi.gif?raw=true" width="500">


