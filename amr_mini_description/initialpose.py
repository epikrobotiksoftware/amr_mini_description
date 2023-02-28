import rclpy
from geometry_msgs.msg import PoseWithCovarianceStamped


def publish_initial_pose():
    rclpy.init()
    node = rclpy.create_node('initial_pose_publisher')
    publisher = node.create_publisher(
        PoseWithCovarianceStamped, '/initialpose', 10)

    msg = PoseWithCovarianceStamped()
    msg.header.frame_id = 'map'
    msg.pose.pose.position.x = 0.0
    msg.pose.pose.position.y = 0.0
    msg.pose.pose.position.z = 0.0
    msg.pose.pose.orientation.x = 0.0
    msg.pose.pose.orientation.y = 0.0
    msg.pose.pose.orientation.z = 0.0
    msg.pose.pose.orientation.w = 1.0
    msg.pose.covariance[0] = 0.25
    msg.pose.covariance[7] = 0.25
    msg.pose.covariance[35] = 0.06853891945200942

    while rclpy.ok():
        publisher.publish(msg)
        node.get_logger().info('Publishing initial pose')
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    publish_initial_pose()
