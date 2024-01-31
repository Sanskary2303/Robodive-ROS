# Robodive-ROS

## Running a Turtle Bot

Go the the workspace and clone the repository of tutle bot
```bash
cd catkin_ws/src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
```
Install the dependent packages

```bash
git clone git@github.com:ROBOTIS-GIT/turtlebot3.git
git clone git@github.com:ROBOTIS-GIT/turtlebot3_msgs.git
```
Build the package and source the setup

```bash
cd ~/catkin_ws
catkin_make
# if you are using bash
source devel/setup.bash
# if you are using zsh
source devel/setup.zsh
```

You can use different models of the robot like burger, waffle, waffle_pi

Now export the model you want to use
```bash
export TURTLEBOT3_MODEL={model_name}
```
Example
```bash
export TURTLEBOT3_MODEL=burger
```

Now launch the bot.
You can use different worlds for launching.

```bash
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
roslaunch turtlebot3_gazebo turtlebot3_world.launch
roslaunch turtlebot3_gazebo turtlebot3_house.launch
```
### Controlling the Robot

Open a new terminal and run the command

```bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

## Multi-Robot System

### Ros Master
First we setup the commnunication between the computers. In this one computer is master and remaining computers are slave. 

#### Setup 
First connect all the computers in the same network. Every computer will have their IP assigned in the network in the subnet mask of 24. Check the IP all computer by typing ***ifconfig*** in the terminal. Note the IP of the master computer.
Run the following command in all the slave computer.

```bash
export ROS_MASTER_URI=http://<master's ip>:11311
```
Now, Every computer should also export their own IP. Type the following command in every computer.

```bash
export ROS_IP=<own ip>
```
To check everything is setup, type the following commands.


```bash
echo $ROS_MASTER_URI
echo $ROS_IP
```
Now, everything is established. You can now run the ***roscore*** on the master computer. Now you can run nodes on computer and view their topics on any computer.

#### Example

I am running talker on one computer 

```bash
rosrun rospy_tutorials talker
```
Check on others computer if this node is running by typing ***rosnode list*** . This will show talker node running. 

Now you can run listener on other computer to see the talker message.

```bash
rosrun rospy_tutorials listener
```
## $${\color{red}Warning}$$

Firewall should be disabled on all the computer for proper communication setup.

You can check it by following command

```bash
sudo ufw status
```
This should show *inactive*. But if it is active, then you have to disable it by following command.

```bash
sudo ufw disable
```