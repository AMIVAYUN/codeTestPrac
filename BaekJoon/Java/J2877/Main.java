package J2877;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	static StringTokenizer token;

	public static void main(String[] args) throws IOException {

		int n = Integer.parseInt(bf.readLine());
		int turn = 1;
		int div = 2;

		while (n > div) {
			n -= div;
			turn++;
			div *= 2;
		}

		char[] nums = new char[turn];

		Arrays.fill(nums, '4');

		String b = Integer.toBinaryString(n - 1);

		String base = "";

		for (int idx = 0; idx < turn - b.length(); idx++) {
			base += "0";
		}

		char[] bb = (base + b).toCharArray();
		for (int idx = 0; idx < bb.length; idx++) {
			char c = bb[idx];
			if (c == '1') {
				nums[idx] = '7';
			}
		}

//			if (n != 1) {
//				int bias = 1;
//
//				int div2 = 2;
//
//				int pos = turn - bias;
//				while (n > div2) {
//					nums[pos] = '7';
//					n -= div2;
//					pos--;
//					div2 *= 2;
//
//				}
//				bias++;
//
//			}

		String s = "";
		for (char c : nums)
			s += c;
		System.out.println(s);
	}
//int n = Integer.parseInt( bf.readLine() );

}
