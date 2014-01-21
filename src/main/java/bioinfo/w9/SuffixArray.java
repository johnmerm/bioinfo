package bioinfo.w9;

import java.io.FileWriter;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;
import java.util.SortedSet;
import java.util.TreeSet;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Function;
import com.google.common.base.Joiner;
import com.google.common.base.Predicate;
import com.google.common.collect.Collections2;
import com.google.common.collect.Iterables;
import com.google.common.collect.Lists;
import com.google.common.collect.Ordering;

public class SuffixArray {
	protected String text;
	protected List<Integer> suffixArray;
	protected List<Integer> lcp;
	
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
	
	String getSuffix(int s) {
		return text.substring(suffixArray.get(s));
	}
	void noop(){}
	public Trie toTrie(){
		Trie root = new Trie();
		try {
			Trie previous = root.appendChild(getSuffix(0));
			previous.id = 0;
			
			for (int i=1;i<text.length();i++) {
				int lcp_before = lcp.get(i-1);
				int lcp_now = lcp.get(i);
				if (lcp_before == lcp_now) {
					//previous and this share parent
					Trie parent = previous.parent;
					previous = parent.appendChild(getSuffix(i).substring(lcp_now));
				
				}else if (lcp_before<lcp_now) {
					//Must break previous in prefix and suffix and link this to suffix
					String previousString = previous.label;
					String prefix = previousString.substring(0,lcp_now-lcp_before);
					String suffix = previousString.substring(lcp_now-lcp_before);
					Trie parent = previous;
					parent.label = prefix;
					parent.appendChild(suffix);
					String thisText = getSuffix(i).substring(lcp_now);
					previous = parent.appendChild(thisText);
				
				}else {
					//lcp_before > lcp_now. Must climb upwards to find a common parent
					int diff = lcp_before-lcp_now;
					Trie parent = previous;
					
					while (diff>0) {
						parent = parent.parent;
						diff -= parent.label.length();
						
					}
					if (diff<0) {
						String parentLabel = parent.label;
						String parentPrefix = parentLabel.substring(0,-diff);
						String parentSuffix = parentLabel.substring(-diff);
						
						parent.label = parentPrefix;
						List<Trie> paChildren = parent.children;
						parent.children = null;
						Trie paThis = parent.appendChild(parentSuffix);
						paThis.children = paChildren;
						for (Trie t:paChildren) {
							t.parent = paThis;
						}
						 
					}else {
						parent = parent.parent;
					}
					previous = parent.appendChild(getSuffix(i).substring(lcp_now));
				}
			}
		}catch (Exception e) {
			e.printStackTrace();
		}
		
		
		return root;
	}
	
	public static void main_lsrp(String[] args) throws Exception{
		SuffixArray array = new SuffixArray();
		
		
		InputStream f = SuffixArray.class.getResourceAsStream("dataset_95_5.txt");
		
		String[] texts = IOUtils.toString(f).split("\n");
		String text = texts[0]+"$"+texts[1]+"#";
		
		array.calculateSuffixArray(text);
		array.calculateLCP();
				
		for (int i=0;i<text.length();i++) {
			int sarry = array.suffixArray.get(i);
			int lcp = array.lcp.get(i);
			String stext = text.substring(array.suffixArray.get(i));
			StringBuilder treetext = new StringBuilder(stext);
			for (int j=0;j<lcp;j++) {
				treetext.setCharAt(j, '.');
			}
			System.out.println(sarry+"\t"+lcp+"\t"+treetext);
		}
		
		String lcr = array.lcr();
		
		Trie trie = array.toTrie();
		
		for (Trie t:trie.allNodes()) {
			System.out.println(t);
		}
		
		
	}
	
	public static void main_trie(String[] args) throws Exception{
		SuffixArray array = new SuffixArray();
		
		InputStream f = SuffixArray.class.getResourceAsStream("dataset_96_6.txt");
		String[] texts = IOUtils.toString(f).split("\n");
		
		
		array.text = texts[0].trim();
		array.suffixArray = Lists.newArrayList(Iterables.transform(Arrays.asList(texts[1].split(", ")), new Function<String, Integer>() {
			public Integer apply(String input) {
				return Integer.parseInt(input.trim());
			}
		}));
		
		array.lcp = Lists.newArrayList(Iterables.transform(Arrays.asList(texts[2].split(", ")), new Function<String, Integer>() {
			public Integer apply(String input) {
				return Integer.parseInt(input.trim());
			}
		}));
		
		
		
		
		Trie trie = array.toTrie();
		
		for (Trie t:trie.allNodes()) {
			System.out.println(t.label);
		}
	}
	
	public static void main(String[] args) throws Exception{
		InputStream f = SuffixArray.class.getResourceAsStream("dataset_95_6.txt");
		
		String[] texts = IOUtils.toString(f).split("\n");
		
		final String text1=texts[0];
		final String text2=texts[1];
		
		//final String text1="CCAAGCTGCTAGAGG";
		//final String text2="CATGCTGGGCTGGCT";
		
		String text = text1+"$"+text2+"#";
		
		final SuffixArray array = new SuffixArray();
		array.calculateSuffixArray(text);
		array.calculateLCP();
/*		
		for (int i=0;i<text.length();i++) {
			int sarry = array.suffixArray.get(i);
			int lcp = array.lcp.get(i);
			String stext = text.substring(array.suffixArray.get(i));
			StringBuilder treetext = new StringBuilder(stext);
			for (int j=0;j<lcp;j++) {
				treetext.setCharAt(j, '.');
			}
			System.out.println(sarry+"\t"+lcp+"\t"+stext);
		}
*/		

		List<int[]> ranges = new ArrayList<int[]>();
		int range_start = 0;
		int range_end = 0;
		int lcp_old = array.lcp.get(0);
		for (int i=1;i<array.lcp.size();i++){
			int lcp = array.lcp.get(i);
			if (lcp == lcp_old){
				range_end++;
			}else{
				ranges.add(new int[]{lcp_old,range_start,range_end});
				range_start=i;
				range_end = i;
				lcp_old = lcp;
			}
		}
		
//		System.out.println("Ranges");
//		for (int[] range:ranges){
//			System.out.println(range[0]+" "+range[1]+" "+range[2]);
//		}
		
		Collection<int[]> filteredRanges = Collections2.filter(ranges, new Predicate<int[]>() {
			public boolean apply(int[] arg) {
				if (arg[0] == 0 || arg[1]==arg[2]){
					return false;
				}else{
					int start = arg[1]-1;
					int end = arg[2];
					boolean valid = true;
					for (int i=start;i<=end;i++){
						valid &= array.getSuffix(i).contains("$");
					}
					return valid;
				}
			}
		});
		
		
		List<int[]> minranges = Ordering.from(new Comparator<int[]>() {
			public int compare(int[] o1, int[] o2) {
				return o1[0]-o2[0];
			}
		}).leastOf(filteredRanges, 1);
		
		System.out.println("Filtered Ranges");
		for (int[] range:minranges){
			System.out.println(range[0]+" "+range[1]+" "+range[2]);
			for (int i=range[1]-1;i<=range[2];i++){
				System.out.println(array.getSuffix(i).substring(0,range[0]+1));
			}
		}
		
		
	}
}
