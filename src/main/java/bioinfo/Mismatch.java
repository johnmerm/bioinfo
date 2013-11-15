package bioinfo;

import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.io.IOUtils;

import bioinfo.FrequentWords.KMer;

import com.google.common.base.Function;
import com.google.common.collect.Lists;

public class Mismatch {
	
	static Function<String[], Integer> difference = new Function<String[], Integer>() {
		public Integer apply(String[] input) {
			assert input.length ==2;
			assert input[0].length() == input[1].length();
			int diff = 0;
			for (int i=0;i<input[0].length();i++) {
				char c0 = input[0].charAt(i);
				char c1 = input[1].charAt(i);
				if (c0 != c1) {
					diff ++ ;
				}
			}
			return diff;
		}
	};
	
	
	static int difference(KMer a1,KMer a2) {
		return difference.apply(new String[] {a1.getkMer(),a2.getkMer()});
	}
	
	
	static int difference(String a1,String a2) {
		return difference.apply(new String[] {a1,a2});
	}
	public static void main(String[] args) throws Exception, IOException {
		
		
		
		boolean sample = false;
		
		String text = IOUtils.toString(new FileInputStream("C:\\Users\\grmsjac6.GLOBAL-AD\\Downloads\\dataset_8_3.txt"));
		String lines[] = text.trim().split("\n");
		String kmerOrig = lines[sample?1:0].trim();
		String input = lines[sample?2:1].trim();
		int d = Integer.parseInt(lines[sample?3:2].trim());
		List<Integer> outPos = null;
		if (sample) {
			String output = lines[5].trim();
			outPos = Lists.transform(Arrays.asList(output.trim().split(" ")), new Function<String,Integer>(){
				public Integer apply(String input) {
					return Integer.parseInt(input);
				}
			});
		}
		/*
		
		
		String kmerOrig ="ATTCTGGA";
		String input = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT";
		int d = 3;
		
		*/
		List<Integer> pos = new ArrayList<Integer>();
		
		for (int i=0;i<=input.length()-kmerOrig.length();i++) {
			String kmerCompare = input.substring(i,i+kmerOrig.length());
			int diff = difference.apply(new String[] {kmerCompare,kmerOrig});
			if (diff<=d) {
				pos.add(i);
			}
			if (diff == 0) {
				//i+=kmerOrig.length();
			}
		}
		if (sample) {
			//assert(outPos.size() == pos.size());
			List<Integer> comp = new ArrayList<Integer>(outPos);
			comp.removeAll(pos);
			//assert(outPos.size() == 0);
		}
		
		FileWriter out = new FileWriter("out");
		for (int p:pos) {
			out.append(String.valueOf(p)).append(" ");
		}
		out.close();
	}
}
