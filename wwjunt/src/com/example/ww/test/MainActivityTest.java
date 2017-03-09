package com.example.ww.test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.example.ww.MainActivity;

import android.test.AndroidTestCase;

@SuppressWarnings("deprecation")
public class MainActivityTest extends AndroidTestCase {
    MainActivity myapp = null;
  
	@Before
	protected void setUp() throws Exception {
		super.setUp();
		myapp = new MainActivity();
	}

	@After
	protected void tearDown() throws Exception {
		super.tearDown();
		myapp = null;
	}

	@Test
	public void testAdd() {
		assertNotNull("Content is null",mContext);
		assertEquals(myapp.add(3, 2), 5);
		assertEquals(myapp.add(1, 99), 100);
		assertEquals(myapp.add(1, 10000), 10001);
	}

}
