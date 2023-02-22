#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSDurabilityPolicy, QoSReliabilityPolicy
from rclpy.qos import QoSProfile
from sensor_msgs.msg import LaserScan
from rclpy.executors import MultiThreadedExecutor

flt = 'amr_mini_description/front_lidar_amr_mini_laser'
blt = 'amr_mini_description/back_lidar_amr_mini_laser'


class ReadingLaser(Node):

    def __init__(self, topic):
        super().__init__('reading_laser')
        self.laser_data = None

        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT
        qos_profile.durability = QoSDurabilityPolicy.VOLATILE

        self.subscription = self.create_subscription(
            LaserScan,
            topic,
            self.listener_callback,
            qos_profile,
        )

        self.merged_pub = self.create_publisher(LaserScan, 'scan', 10)

    def listener_callback(self, msg):
        # self.get_logger().info('I heard : Range[0] "%f" Ranges[100]: "%f"' % (
        #     msg.ranges[0], msg.ranges[100]))
        self.laser_data = msg
        self.merged_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    reading_laser_flt = ReadingLaser(flt)
    reading_laser_blt = ReadingLaser(blt)
    executor = MultiThreadedExecutor()
    executor.add_node(reading_laser_flt)
    executor.add_node(reading_laser_blt)
    executor.spin()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
