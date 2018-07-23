# QA
appium启动所需的包名和Activity名获取的方法

1、将待测apk放到在一定的路径

2、改变当前目录有aapt，我的在/Users/joyliu/Documents/app/android-sdk-macosx/build-tools/25.0.2

3、aapt dump badging /Users/joyliu/Desktop/Finance_tiancai_Test_v4.0.3.apk  
	 	
   即可得到当前包名和launchactivity 
   
   launchable-activity: name='com.itiancai.finance.container.view.activity.SplashActivity_'
	
   package: name='com.itiancai.finance.test'
