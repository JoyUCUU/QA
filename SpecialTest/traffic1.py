#/usr/bin/python
#encoding:utf-8

import  csv
import  os
import  string
import  time

class Controller(object):
    def __init__(self,count):
        #定义测试的次数
        self.count = count
        #定义收集数据的数组
        self.alldata = [("timestamp","traffic")]

    #单次检测过程
    def testprocess(self):
        #执行获取进程的命令
        result = os.popen("adb shell ps | grep com.qiyi.video")
        #获取进程ID
        pid = result.readlines()[0].split(" ")[5]

        #获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/" + pid + "/net/dev")
        for line in traffic:
            if "eth0" in line:
                #将所有空行换成#
                line = "#".join(line.split())
                #按#号拆分，获取收到和发出的流量
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
            elif "eth1" in line:
                #将所有空行换成#
                line = "#".join(line.split())
                #按#号拆分，获取收到和发出的流量

    #多次检测过程控制
    def run(self):

    #获取当前时间戳
    def getCurrentTime(self):

    #数据的存储
    def SavaDataToCSV(self):

if __name__ == "__main__":