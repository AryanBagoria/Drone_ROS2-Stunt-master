from drone_interfaces.srv import Move
from std_srvs.srv import Empty
import rclpy
import time


def takeoff(node):
    cli = node.create_client(Empty, 'takeoff')
    req = Empty.Request()
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('takeoff service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('takeoff service call failed %r' % (e,))
    else:
        node.get_logger().info("takeoff successful")


def move_forward(node, distance):
    cli = node.create_client(Move, 'move_forward')
    req = Move.Request()
    req.distance = distance
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('move_forward service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('move_forward service call failed %r' % (e,))
    else:
        node.get_logger().info("move forward successful")
        
def move_left(node, distance):
    cli = node.create_client(Move, 'move_left')
    req = Move.Request()
    req.distance = distance
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('move_left service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('move_left service call failed %r' % (e,))
    else:
        node.get_logger().info("move left successful")
        
def move_right(node, distance):
    cli = node.create_client(Move, 'move_right')
    req = Move.Request()
    req.distance = distance
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('move_right service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('move_right service call failed %r' % (e,))
    else:
        node.get_logger().info("move right successful")


def rotate_clockwise(node, angle):
    cli = node.create_client(Move, 'rotate_clockwise')
    req = Move.Request()
    req.distance = angle

    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('rotate_clockwise service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('rotate_clockwise service call failed %r' % (e,))
    else:
        node.get_logger().info("rotate clockwise successful")
        
def arotate_clockwise(node, angle):
    cli = node.create_client(Move, 'arotate_clockwise')
    req = Move.Request()
    req.distance = angle

    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('arotate_clockwise service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('arotate_clockwise service call failed %r' % (e,))
    else:
        node.get_logger().info("anti rotate clockwise successful")


def land(node):
    cli = node.create_client(Empty, 'land')
    req = Empty.Request()
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('land service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('land service call failed %r' % (e,))
    else:
        node.get_logger().info("land successful")


def curve(node, x1, y1, z1, x2, y2, z2, speed):
    cli = node.create_client(Move, 'curve')
    req = Move.Request()
    req.x1 = x1
    req.y1 = y1
    req.z1 = z1
    req.x2 = x2
    req.y2 = y2
    req.z2 = z2
    req.speed = speed

    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('curve service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('curve service call failed %r' % (e,))
    else:
        node.get_logger().info("curve successful")
        
def go(node, x, y, z, speed):
    cli = node.create_client(Move, 'go')
    req = Move.Request()
    req.x = x
    req.y = y
    req.z = z
    req.speed = speed

    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('go service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('go service call failed %r' % (e,))
    else:
        node.get_logger().info("go successful")



def draw_alphabet(node, alphabet):
    movements = {
        'X': [('curve', 70, 70, 0, 140, 0, 0, 50)],
        'N': [('move_forward', 60), ('rotate_clockwise', 135), ('move_forward', 100), ('arotate_clockwise', 135), ('move_forward', 80)],
        '8': [('curve', -50, -50, 0, -100, 0, 0, 50),('curve', 51, 51, 0, 101, 0, 0, 50),('curve', 50, -50, 0, 100, 0, 0, 50),('curve', -51, 51, 0, -101, 0, 0, 50)],
        '3': [('curve', -51, -50, 0, -100, 0, 0, 50),('curve', -51, -51, 0, -101, 0, 0, 50)],
        'I': [('go', 0, 0, 100, 50),('go', -70, 0, -100, 50),('go', 0, 0, 101, 50)],
        # we can add more alphabet movements as needed
    }

    if alphabet not in movements:
        node.get_logger().info(f"Alphabet '{alphabet}' is not supported.")
        return

    for movement in movements[alphabet]:
        movement_name, *args = movement
        if movement_name == 'move_forward':
            move_forward(node, *args)
        elif movement_name == 'rotate_clockwise':
            rotate_clockwise(node, *args)
        elif movement_name == 'arotate_clockwise':
            arotate_clockwise(node, *args)    
        elif movement_name == 'move_left':
            move_left(node, *args)
        elif movement_name == 'move_right':
            move_right(node, *args)
        elif movement_name == 'go':
            go(node, *args)
        elif movement_name == 'curve':
            curve(node, *args)

        time.sleep(0.7)


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('drone_service_client')

    takeoff(node)
    time.sleep(2)

    while True:
        print("Menu:")
        print("1. Draw figures")
        print("2. Land")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            alphabet = input("Enter the figure you want to draw: ")
            draw_alphabet(node, alphabet.upper())
        elif choice == '2':
            land(node)
        else:
            print("Invalid choice. Please try again.")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

