#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped


class InitialPosePublisher(Node):
    def __init__(self):
        super().__init__('initial_pose_publisher')
        self.publisher_ = self.create_publisher(
            PoseWithCovarianceStamped, 'initialpose', 10)

        self.publishers_ = self.create_timer(0.5, self.publish_initial_pose)

    def publish_initial_pose(self):
        # Create a PoseWithCovarianceStamped message
        pose_msg = PoseWithCovarianceStamped()

        # Set the header
        pose_msg.header.stamp = self.get_clock().now().to_msg()
        pose_msg.header.frame_id = 'map'

        # Set the initial pose
        pose_msg.pose.pose.position.x = 0.0
        pose_msg.pose.pose.position.y = 0.0
        pose_msg.pose.pose.position.z = 0.0
        pose_msg.pose.pose.orientation.x = 0.0
        pose_msg.pose.pose.orientation.y = 0.0
        pose_msg.pose.pose.orientation.z = 0.0
        pose_msg.pose.pose.orientation.w = 1.0
        pose_msg.pose.covariance[0] = 0.25
        pose_msg.pose.covariance[7] = 0.25
        pose_msg.pose.covariance[35] = 0.06853891945200942

        # Publish the message
        self.publisher_.publish(pose_msg)
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    initial_pose_publisher = InitialPosePublisher()

    rclpy.spin(initial_pose_publisher)

    initial_pose_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
