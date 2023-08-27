#include "ros/ros.h“  //ROS 기본 헤더파일

#include "my_practice/time_msg.h" //패키지이름 / 메세지파일.h
            
int main(int argc, char **argv) // c++ 의 기본 함수형태
{
  ros::init(argc, argv, "pub"); //노드명 초기화
  ros::NodeHandle nh; // ROS시스템과 통신을 위한 노드핸들 선언

  ros::Publisher pub = nh.advertise<my_practice::time_msg>("pub_topic", 100);
  //퍼블리셔 선언, 패키지 ()의 메시지파일()을 이용
  //퍼블리시어()을 작성
  //토픽명은 ()이며 퍼블리시어큐 사이즈를 ()개로 설정한다.
  // publisher이기 때문에 advertise 만듬

  ros::Rate loop_rate(2); //루프 주기를 2Hz로 설정 (1초에 2번)

  my_practice::time_msg msg; //내가 만든 메시지 파일 형식으로 ()라는 메세지선언

  int count = 0;

  while (ros::ok()) // ros 가 활성화되면
  {
    msg.stamp = ros::Time::now(); //현재 시간을 msg 하위 stamp메세지에 담음
    msg.data = count; // count 변수 값을 msg 하위 data 메세지에 담는다.
    ROS_INFO("send msg = %d", msg.stamp.sec);
    ROS_INFO("send msg = %d", msg.stamp.nsec);
    ROS_INFO("send msg = %d", msg.data);

    pub.publish(msg);
    loop_rate.sleep();
    ++count;
  }
  return 0;
}


