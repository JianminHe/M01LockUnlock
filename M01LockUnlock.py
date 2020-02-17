# -*- encoding=utf8 -*-
__author__ = "jianmin"

from airtest.core.api import *

from airtest.core.android.minitouch import *

from airtest.core.android.android import Android

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

# # 锁屏情况下，唤醒屏幕，输入密码

# keyevent("POWER")
test1=Android()
w=test1.display_info['physical_width']
h=test1.display_info['physical_height']

wake()


swipe([w/2,h*0.9],[w/2,h*0.3])

# sleep(3.0)
if poco(text="输入密码").exists():
    touch(Template(r"tpl1581920576254.png", record_pos=(-0.231, 0.135), resolution=(1080, 1920)))
    touch(Template(r"tpl1581920576254.png", record_pos=(-0.231, 0.135), resolution=(1080, 1920)))
    touch(Template(r"tpl1581920576254.png", record_pos=(-0.231, 0.135), resolution=(1080, 1920)))
    touch(Template(r"tpl1581920576254.png", record_pos=(-0.231, 0.135), resolution=(1080, 1920)))

start_app('com.chehejia.oc.m01')


for j in range(100):
    poco(text="车锁").click()
    if  poco(text="请输入安全密码").exists():
        for i in range(6):
            touch(Template(r"tpl1581925219098.png", record_pos=(-0.213, 0.373), resolution=(1080, 1920)))
    sleep(10.0)




