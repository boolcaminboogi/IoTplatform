#include "ros/ros.h"
#include "my_practice/time_msg.h"

void msgCallback(const my_practice::time_msg::ConstPtr &msg) // const 상수
{
  ROS_INFO("receive msg = %d", msg->stamp.sec);
  ROS_INFO("receive msg = %d", msg->stamp.nsec);
  ROS_INFO("receive msg = %d", msg->data);
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "sub");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("pub_topic", 100, msgCallback);
  ros::spin(); //어떤 값이 들어오기 전까지 대기 (다시 위로 올라감)
  return 0;
}
