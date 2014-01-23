package bioinfo.w10;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import bioinfo.w9.SuffixArray;

import com.google.common.base.Joiner;
import com.google.common.base.Strings;
import com.google.common.collect.Collections2;
import com.google.common.collect.Iterables;
import com.google.common.collect.Lists;
import com.google.common.collect.Ordering;

public class BWMultiMatch {
	private static final  char[] alphabet = {'A','G','C','T','$'};
	private String text;
	private String bwt;
	
	private Map<Character, List<Integer>> counts = new HashMap<Character, List<Integer>>();
	private Map<Character, List<Integer>> checkpoints = new HashMap<Character, List<Integer>>();
	private Map<Character,Integer> firstOccurence = new HashMap<Character, Integer>();
	public BWMultiMatch(String text,boolean isBWT,int check) {
		if (!isBWT) {
			BurrowsWheeler bw = new BurrowsWheeler(text);
			bwt = bw.getBwt();
		}else {
			bwt = text;
		}
		
		List<Character> firstColumn = Ordering.natural().sortedCopy(Lists.charactersOf(bwt));
		
		for (char c:alphabet) {
			counts.put(c, new ArrayList<Integer>(Arrays.asList(0)));
			checkpoints.put(c, new ArrayList<Integer>(Arrays.asList(0)));
			firstOccurence.put(c, firstColumn.indexOf(c));
		}
		
		
		
		
		
		for (int i=1;i<=bwt.length();i++) {
			char s = bwt.charAt(i-1);
			
			
			for (char c:alphabet) {
				List<Integer> l = counts.get(c);
				l.add(c == s?l.get(i-1)+1:l.get(i-1));
				if (i%check == 0) {
					checkpoints.get(c).add(l.get(i));
				}
			}
		}
	}
	
	public int[] matchPatternInternal(String pattern) {
		int top = 0,bottom = bwt.length()-1;
		String p = pattern;
		while (top<=bottom) {
			if (p.length()>0) {
				char s = p.charAt(p.length()-1);
				p = p.substring(0,p.length()-1);
				if (counts.get(s).get(top)<counts.get(s).get(bottom+1)) {
					top = firstOccurence.get(s)+counts.get(s).get(top);
					bottom = firstOccurence.get(s)+counts.get(s).get(bottom+1)-1;
				}else {
					return new int[0];
				}
			}else {
				return new int[] {top,bottom};
			}
		}
		return new int[0];
	}
	public int matchPattern(String pattern) {
		int[] i = matchPatternInternal(pattern);
		if (i.length == 0) {
			return 0;
		}else {
			return i[1]-i[0]+1;
		}
	}
	
	public static List<Integer> matchPositions(String text,String patterns[]) {
		SuffixArray array = new SuffixArray();
		array.calculateSuffixArray(text);
		BWMultiMatch bm = new BWMultiMatch(text, false, 1);
		
		List<Integer> ret = new ArrayList<Integer>();
		for (String pattern:patterns) {
			int range[] = bm.matchPatternInternal(pattern);
			if (range.length == 0) {
				continue;
			}else {
				
				for (int i = range[0];i<=range[1];i++) {
					ret.add(array.getSuffixPosition(i));
				}
				
			}
		}
		return ret;
		
	}
}
