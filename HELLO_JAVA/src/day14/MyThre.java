package day14;

// 쌤
public class MyThre {
	public static void showNum() {
		new Thread(new Runnable() {
			public void run() {
				for (int i = 1; i <= 100000; i++) {
					System.out.print(i);
					if(i%100==0) {
						System.out.println();
					}
				}
			}
		}).start();
	}
	
	public static void showAscii() {
		new Thread(new Runnable() {
			public void run() {
				for (int i = 1; i <= 100000; i++) {
					System.out.print((char)i);
					if(i%100==0) {
						System.out.println();
					}
				}
			}
		}).start();
	}
	
	public static void main(String[] args) {
		showNum();
		showAscii();
	}
}


// 나
//public class MyThre {
//	public static void showNum() {
//		TestThread testThread = new TestThread();
//		testThread.start();
//	}
//	
//	public static void main(String[] args) {
//		showNum();
//	}
//}
//
//class TestThread extends Thread {
//	@Override
//	public void run() {
//		for (int i = 0; i <= 100000; i++) {
//			System.out.println(i);
//		}
//	}
//}

