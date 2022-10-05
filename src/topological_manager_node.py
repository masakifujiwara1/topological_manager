#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int8MultiArray


class topological_node:
    def __init__(self):
        rospy.init_node('topological_node', anonymous=True)
        self.aisle_class_sub = rospy.Subscriber(
            "/detect_class", Int8MultiArray, self.callback_class, queue_size=1)
        self.cmd_dir_pub = rospy.Publisher(
            "cmd_dir_topological", Int8MultiArray, queue_size=1)
        self.node_no = 1
        self.count = 0
        self.cmd_dir = Int8MultiArray()
        self.cmd_dir.data = (0, 100, 0)
        self.detect_flag = False
        self.initialize()

    def initialize(self):
        pass

    def callback_class(self, data):
        self.detect_class_data = data.data
        self.detect_flag = True
        print("detect aisle")
        self.count += 1

    def plan(self, node_no=1):
        if node_no == 1:
            if self.count == 1:
                self.cmd_dir.data = (0, 100, 0)
            if self.count == 2:
                self.cmd_dir.data = (0, 100, 0)
            if self.count == 3:
                self.cmd_dir.data = (0, 0, 100)
            if self.count == 4:
                self.cmd_dir.data = (0, 0, 100)
            if self.count == 5:
                self.cmd_dir.data = (0, 0, 100)
            if self.count == 6:
                self.cmd_dir.data = (100, 0, 0)
            if self.count == 7:
                print("stop point")
        else:
            pass
        self.detect_flag = False

    def loop(self):
        if self.detect_flag:
            self.plan(self.node_no)

        self.cmd_dir_pub.publish(self.cmd_dir)
        # print("topological")


if __name__ == '__main__':
    rg = topological_node()
    DURATION = 0.25
    r = rospy.Rate(1 / DURATION)
    while not rospy.is_shutdown():
        rg.loop()
        r.sleep()
