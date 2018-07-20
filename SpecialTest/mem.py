#/usr/bin/python
#encoding:utf-8

import  csv
import  os
import  time

#控制类
class Controller(object):
    def __init__(self):
        self.alldata = [("i","vss","rss")]

    #分析数据
    def analyzedata(self):
        content = self.readfile()
        i = 0
        for line in content:
            print("just line" + line)
            if "com.idainizhuang.dnz.test" in line:
                line = "#".join(line.split())
                print("line+#" + line)
                vss = line.split("#")[5].strip("K")
                print("vss" + vss)
                rss = line.split("#")[6].strip("K")
                print("rss" + rss)
                #将获取到的数据存储到数组中
                self.alldata.append((i,vss,rss))
                i = i + 1

    #数据的存储
    def SavaDataToCSV(self):
        csvfile = open("meminfo.csv",'w')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

    #读取数据文件
    def readfile(self):
        mfile = open("meminfo.txt")

        content = mfile.readlines()
        mfile.close()

        return  content

if __name__ == "__main__":
    controller = Controller()
    controller.analyzedata()
    controller.SavaDataToCSV()
