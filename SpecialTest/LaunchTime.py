#/usr/bin/python
#encoding:utf-8
import csv
import os

#app类
import time


class App(object):
    def __init__(self):
        self.content = ''
        self.startTime = 0
    #启动App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.qiyi.video/.WelcomeActivity'
        self.content = os.popen(cmd)
    #停止App
    def StopApp(self):
        cmd = 'adb shell am force-stop com.qiyi.video'
        os.popen(cmd)
    #获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if 'ThisTime' in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime


#控制过程


class Controller(object):

    def __init__(self,count):
        self.app = App()
        #执行次数的
        self.counter = count
        self.alldata = [{"timestamp","elapsedtime"}]
    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(5)
        elapsedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime,elapsedtime))
    #多次执行的测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return  currentTime

    #def collectAllData(self):
    #数据的存储
    def SavaDataToCSV(self):
        csvfile = open('startTime.csv' , 'w')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if  __name__ == "__main__":
    controller = Controller(5)
    controller.run()
    controller.SavaDataToCSV()

