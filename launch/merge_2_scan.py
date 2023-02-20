import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class MergeLaserNode(Node):
    def __init__(self):
        super().__init__('merge_laser_node')
        self.laser1_data = None
        self.laser2_data = None

        self.laser1_sub = self.create_subscription(
            LaserScan, 'amr_mini_description/front_lidar_amr_mini_laser', self.laser1_callback, 10)
        self.laser2_sub = self.create_subscription(
            LaserScan, 'amr_mini_description/back_lidar_amr_mini_laser', self.laser2_callback, 10)

        self.merged_pub = self.create_publisher(
            LaserScan, '/scan', 10)

    def laser1_callback(self, msg):
        self.laser1_data = msg

    def laser2_callback(self, msg):
        self.laser2_data = msg

    def merge_and_publish(self):
        if self.laser1_data and self.laser2_data:
            merged_msg = LaserScan()

            self.merged_pub.publish(merged_msg)


def main(args=None):
    rclpy.init(args=args)

    merge_laser_node = MergeLaserNode()

    timer_period = 0.1  # seconds
    timer = merge_laser_node.create_timer(
        timer_period, merge_laser_node.merge_and_publish)

    rclpy.spin(merge_laser_node)

    merge_laser_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
