#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import time


class RecoveryGlobalPlanPublisher(Node):
    def __init__(self):
        super().__init__('received_global_plan_publisher')
        self.publisher_ = self.create_publisher(
            PoseStamped, 'goal_pose', 10)

        self.publishers_ = self.create_timer(
            0.5, self.publish_received_global_plan)

    def publish_received_global_plan(self):
        pose_msg = PoseStamped()

        pose_msg.header.stamp = self.get_clock().now().to_msg()
        pose_msg.header.frame_id = 'map'
        pose_msg.pose.position.x = -21.2076
        pose_msg.pose.position.y = -12.8942
        pose_msg.pose.position.z = 0.0
        pose_msg.pose.orientation.x = 0.0
        pose_msg.pose.orientation.y = 0.0
        pose_msg.pose.orientation.z = -0.0018
        pose_msg.pose.orientation.w = 1.0

        # Publish the message
        time.sleep(10)
        self.publisher_.publish(pose_msg)
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    received_global_plan_publisher = RecoveryGlobalPlanPublisher()

    rclpy.spin(received_global_plan_publisher)

    received_global_plan_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
