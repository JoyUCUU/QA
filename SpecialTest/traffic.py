#/usr/bin/python
#encoding:utf-8

import csv
#adb命令
import os
import string
import time

#控制类
class Controller(object):
    def __init__(self,count):
        #定义测试的次数
        self.counter = count
        #定义收集数据的数组
        self.alldata = [("timestamp","traffic")]


    #单次测试过程
    def testprocess(self):
        #执行获取进程的命令
        result = os.popen("adb shell ps | grep com.qiyi.video")
        receive = 0
        receive1 = 0
        transmit = 0
        transmit1 = 0

        #获取进程的ID
        pidstr = str(result.readlines()[0])
        print (pidstr)
        pid = pidstr.split(" ")[4]
        print (pid)

        #获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/"+pid+"/net/dev")
        for line in traffic:
            strline = str(line.split())
            print(strline)
            if "eth0" in strline:
                #将所有的空行换成#
                strline = "#".join(strline.split())
                print ("newdata/n"+strline)
                #按#号拆分，获取收到和发出的流量
                receive = strline.split("#")[1]
                transmit = strline.split("#")[9]
            elif "eth1" in strline:
                #将所有空行换成#
                #strline = "#".join(strline.split())
                print("看一下呗"+strline)
                #按#号拆分，获取收到和发出的流量
                receive2 = strline[1:3]
                print("receive2:" + receive2)
                transmit2 = strline[60:66]
                print("transmit2:" + transmit2)

        #计算所有流量的之和
        alltraffic = round(float(receive)) + float(transmit) + float(receive2) + float(transmit2)
        #按kb计算流量值
        alltraffic = alltraffic/1024
        #获取当前时间
        currenttime = self.getCurrentTime()
        #将获取到的数据存到数组中
        self.alldata.append((currenttime,alltraffic))

    #多次测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter = 1
            #每5秒钟采集一次数据
            time.sleep(5)

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = open("traffic.csv","w")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(2)
    controller.run()
    controller.SaveDataToCSV()