package com.example.ww.test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.example.ww.MainActivity;

import android.test.AndroidTestCase;

@SuppressWarnings("deprecation")
public class MainActivityTest1 extends AndroidTestCase {
    MainActivity myapp = null;
	@Before
	protected void setUp() throws Exception {
		super.setUp();
		myapp  = new MainActivity();
	}

	@After
	protected void tearDown() throws Exception {
		super.tearDown();
		myapp = null;
	}

	@Test
	public void Add测试用例(){
		assertEquals(myapp.add(3, 2), 5);
		
	}
	public  void Addtest2() {
		assertEquals(myapp.add(3, 22), 26);
	}
	public  void Addtest() {
		assertEquals(myapp.add(3, 2), 5);
	}

}
