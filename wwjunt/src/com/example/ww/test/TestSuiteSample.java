package com.example.ww.test;

import junit.framework.TestSuite;
import junit.framework.Test;

public class TestSuiteSample extends TestSuite {
  public static Test suit() {
	  TestSuite testasuit = new TestSuite("Test");
	  testasuit.addTestSuite(MainActivityTest.class);
	  testasuit.addTest(TestSuite.createTest(MainActivityTest1.class, "Add测试用例"));
	  testasuit.addTest(TestSuite.createTest(MainActivityTest1.class, "Addtest2"));
	  testasuit.addTest(TestSuite.createTest(MainActivityTest1.class, "Addtest"));
	  
	return testasuit;
	
}
}
