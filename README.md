# ROS 2 DRONE AERIAL STUNT Control Stack

This repository contains a ROS 2 package designed for controlling a drone, specifically integrating with a Tello drone via UDP communication. It provides a robust server for receiving and executing drone commands, along with a client application for interactive control and drawing predefined aerial figures.

---

## 1. `drone_server.py`

This script defines a **ROS 2 node** (`DroneServer`) that acts as the primary interface between your ROS 2 environment and the Tello drone. It handles the low-level UDP communication and exposes various drone functionalities as ROS 2 services.

### Features:

* **UDP Communication:** Manages sending commands to the drone and receiving acknowledgments or status updates over UDP.
* **Asynchronous Response Handling:** Utilizes a separate threading mechanism to continuously listen for and process responses from the drone, ensuring non-blocking operation.
* **Comprehensive ROS 2 Services:** Offers a wide range of services for granular drone control:
    * `move_forward`, `move_backward`, `move_left`, `move_right`: Control linear movement by a specified distance.
    * `rotate_clockwise`, `arotate_clockwise`: Perform rotational movements by a given angle.
    * `go`: Execute a direct flight to a specified 3D coordinate (`x, y, z`) at a defined speed.
    * `curve`: Enable curved flight paths by defining two intermediate points and a speed.
    * `takeoff`, `land`: Initiate and terminate drone flight.
    * `flip_forward`, `flip_backward`: Command the drone to perform aerial flips.

### How to Run:

To start the drone server, ensure your ROS 2 environment is sourced and execute the script:

```bash
python3 drone_server.py
