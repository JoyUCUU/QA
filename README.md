# QA
appium启动所需的包名和Activity名获取的方法

1、将待测apk放到在一定的路径

2、改变当前目录有aapt，我的在/Users/joyliu/Documents/app/android-sdk-macosx/build-tools/25.0.2

3、aapt dump badging /Users/joyliu/Desktop/Finance_tiancai_Test_v4.0.3.apk  
	 	
   即可得到当前包名和launchactivity 
   
   launchable-activity: name='com.itiancai.finance.container.view.activity.SplashActivity_'
	
   package: name='com.itiancai.finance.test'

4、使用uiaumator viewer时，有时不能定位xpath，或者像我这种懒人不想一点儿一点儿扣路径的，可以用lazy-uiautomator viewer
    下载uiautomatorviewer.jar 替换掉原来的
    下载路径：https://github.com/JoyUCUU/QA/blob/master/resource/uiautomatorviewer.jar  
    
