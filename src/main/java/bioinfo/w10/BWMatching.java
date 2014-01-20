package bioinfo.w10;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import com.google.common.collect.Ordering;

public class BWMatching{

	protected List<IndexString> lastColumn;
	protected List<IndexString> firstColumn;
	
	protected Map<Character,Map<Integer,Integer>> lastColumnIndex = new TreeMap<Character, Map<Integer,Integer>>();
	protected Map<Character,Map<Integer,Integer>> firstColumnIndex = new TreeMap<Character, Map<Integer,Integer>>();
	
	protected List<Integer> lastToFirst;
	
	public BWMatching(String bwText) {
		
		final Map<Character,Integer> map = new HashMap<Character,Integer>();
		lastColumn =  Lists.newArrayList(Lists.transform(Lists.charactersOf(bwText),new Function<Character,IndexString>(){
			public IndexString apply(Character c) {
				if (map.containsKey(c)){
					int i = map.get(c);
					i = i+1;
					map.put(c, i);
					return new IndexString(c,i);
				}else{
					map.put(c, 1);
					return new IndexString(c,1);
				}
			}
		}));
		
		firstColumn = Ordering.natural().sortedCopy(lastColumn);
		
		for (int i=0;i<lastColumn.size();i++) {
			IndexString li = lastColumn.get(i);
			if (!lastColumnIndex.containsKey(li.getS())) {
				lastColumnIndex.put(li.getS(), new TreeMap<Integer, Integer>());
			}
			lastColumnIndex.get(li.getS()).put(li.getI(), i);
			
			IndexString fi = firstColumn.get(i);
			if (!firstColumnIndex.containsKey(fi.getS())) {
				firstColumnIndex.put(fi.getS(), new TreeMap<Integer, Integer>());
			}
			firstColumnIndex.get(fi.getS()).put(fi.getI(), i);
		}
		
		lastToFirst = new ArrayList<Integer>();
		for (int i=0;i<lastColumn.size();i++) {
			IndexString li = lastColumn.get(i);
			int f_pos = firstColumnIndex.get(li.getS()).get(li.getI());
			lastToFirst.add(f_pos);
		}
		
		
	}
	
	
	public int matchPattern(String pattern) {
		class TopBottomPredicate implements Predicate<Integer>{
			private int top,bottom;

			public TopBottomPredicate(int top, int bottom) {
				super();
				this.top = top;
				this.bottom = bottom;
			}
			
			public boolean apply(Integer input) {
				return input >= top && input <=bottom;
			}
			
			
		}
		
		String p = pattern;
		int top = 0;
		int bottom = lastColumn.size()-1;
		while (top<=bottom) {
			if (p.length()>0) {
				char s = p.charAt(p.length()-1);
				p = p.substring(0,p.length()-1);
				Map unfiltered = lastColumnIndex.get(s);
				if (unfiltered != null) {
					Map<Integer,Integer> filtered = Maps.filterValues(lastColumnIndex.get(s), new TopBottomPredicate(top, bottom));
					if (filtered.size() == 0) {
						return 0;
					}else {
						top = lastToFirst.get(Ordering.natural().min(filtered.values()));
						bottom = lastToFirst.get(Ordering.natural().max(filtered.values()));
					}
				}else {
					return 0;
				}
			}else {
				return bottom-top+1;
			}
		}
		return 0;
		
	}
}
