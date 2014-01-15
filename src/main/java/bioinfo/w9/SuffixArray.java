package bioinfo.w9;

import java.io.FileWriter;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.SortedSet;
import java.util.TreeSet;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Joiner;
import com.google.common.collect.Ordering;

public class SuffixArray {
	private String text;
	private List<Integer> suffixArray;
	private List<Integer> lcp;
	
	public void calculateSuffixArray(final String text) {
		this.text = text;
		SortedSet<Integer >suffixArray = new TreeSet<Integer>(new Comparator<Integer>() {
			public int compare(Integer o1, Integer o2) {
				return text.substring(o1).compareTo(text.substring(o2));
			}
		});
		
		for (int i=0;i<text.length();i++){
			suffixArray.add(i);
		}
		
		this.suffixArray = new ArrayList<Integer>(suffixArray);
	}
	
	public void calculateLCP() {
		lcp = new ArrayList<Integer>();
		lcp.add(0);
		
		for (int i=1;i<text.length();i++) {
			String s_before = text.substring(suffixArray.get(i-1));
			String s_this = text.substring(suffixArray.get(i));
			
			for (int k=0;k<Math.min(s_before.length(), s_this.length());k++) {
				if (s_before.charAt(k) != s_this.charAt(k)) {
					lcp.add(k);
					break;
				}
			}
		}
	}
	
	
	public String lcr(){
		int max = Ordering.natural().max(lcp);
		int idx = lcp.indexOf(max);
		int s_idx = suffixArray.get(idx);
		return text.substring(s_idx,s_idx+max);
	}
	
	
	public List<List<Integer>> breakdown(){
		List<List<Integer>> br = new ArrayList<List<Integer>>();
		br.add(new ArrayList<Integer>());
		
		for (int i=1;i<text.length();i++){
			
		}
		return br;
	}
	
	public static void main(String[] args) throws Exception{
		SuffixArray array = new SuffixArray();
		
		
		InputStream f = SuffixArray.class.getResourceAsStream("dataset_95_5.txt");
		//final String text = IOUtils.toString(f).trim()+"$";
		
		//final String text = "AACGATAGCGGTAGA$";
		//final String text = "ATATCGTTTTATCGTT$";
		
		//final String text="TCGGTAGATTGCGCCCACTC$AGGGGCTCGCAGTGTAAGAA#";
		
		String[] texts = IOUtils.toString(f).split("\n");
		String text = texts[0]+"$"+texts[1]+"#";
		
		array.calculateSuffixArray(text);
		array.calculateLCP();
				
//		for (int i=0;i<text.length();i++) {
//			System.out.println(array.suffixArray.get(i)+"\t"+array.lcp.get(i)+"\t"+text.substring(array.suffixArray.get(i)));
//		}
		
		String lcr = array.lcr();
		System.out.println(lcr);
		
		
	}
	
	
}
