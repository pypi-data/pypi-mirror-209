<p align="center">
<img src="https://raw.githubusercontent.com/TilburgRobotics/tilburg-hand/a66f435ea946a8c50239da2eb4c4453a50820b7a/docs/images/logo.png" alt= "Tilburg Robotics" width="300px">
</p>

The tilburg-hand repository contains the main Python library used to control the [Tilburg Hand](https://www.tilburg-robotics.eu). The repository also includes documentation, examples, a motor gui (installed as `tilburg_hand_motorgui`), and urdf + Mujoco xml models for the robot.

<br/>
Required libraries:<br/>
- dynamixel_sdk<br/>
- pyserial<br/>
- Tk (for the motor gui)<br />


## Installation

Install the library using `pip`, either download one of the pre-built packages, or from PyPI (`pip install tilburg-hand`), or directly from this repository (`pip install -e .` for in-path installation).

