package bioinfo.w10;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BWMultiMatch {
	private static final  char[] alphabet = {'A','G','C','T','$'};
	private Map<Character, List<Integer>> counts = new HashMap<Character, List<Integer>>();
	private Map<Character, List<Integer>> checkpoints = new HashMap<Character, List<Integer>>();
	private Map<Character,Integer> firstOccurence = new HashMap<Character, Integer>();
	public BWMultiMatch(String text,boolean isBWT,int check) {
		String bwt = null;
		if (!isBWT) {
			BurrowsWheeler bw = new BurrowsWheeler(text);
			bwt = bw.getBwt();
		}else {
			bwt = text;
		}
		
		for (char c:alphabet) {
			counts.put(c, new ArrayList<Integer>(Arrays.asList(0)));
			checkpoints.put(c, new ArrayList<Integer>(Arrays.asList(0)));
		}
		
		for (int i=1;i<=bwt.length();i++) {
			char s = bwt.charAt(i-1);
			if (!firstOccurence.containsKey(s)) {
				firstOccurence.put(s, i-1);
			}
			
			for (char c:alphabet) {
				List<Integer> l = counts.get(c);
				l.add(c == s?l.get(i-1)+1:l.get(i-1));
				if (i%check == 0) {
					checkpoints.get(c).add(l.get(i));
				}
			}
		}
	}
}
