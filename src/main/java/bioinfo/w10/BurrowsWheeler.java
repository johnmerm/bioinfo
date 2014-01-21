package bioinfo.w10;

import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.SortedSet;
import java.util.TreeSet;

import com.google.common.base.Function;
import com.google.common.collect.Lists;
import com.google.common.collect.Ordering;

public class BurrowsWheeler {

	protected final String text;
	protected final String bwt;
	
	public BurrowsWheeler(final String text){
		this.text = text;
		SortedSet<Integer> m_set = new TreeSet<Integer>(new Comparator<Integer>() {
			public int compare(Integer o1, Integer o2) {
				String s1 = text.substring(o1)+text.substring(0,o1);
				String s2 = text.substring(o2)+text.substring(0,o2);
				return s1.compareTo(s2);
			}
		});
		
		for (int i=0;i<text.length();i++){
			m_set.add(i);
		}
		
		Integer[] m = m_set.toArray(new Integer[m_set.size()]);
		StringBuilder b = new StringBuilder();
		for (int i=0;i<text.length();i++){
			int idx = m[i];
			char last = text.charAt(idx>0?idx-1:text.length()-1);
			b.append(last);
		}
		
		bwt = b.toString();
		
		
	}

	public String getText() {
		return text;
	}

	public String getBwt() {
		return bwt;
	}
	
	
	public static String invert(String bwtString){
		final Map<Character,Integer> map = new HashMap<Character,Integer>();
		List<IndexString> lastrow =  Lists.newArrayList(Lists.transform(Lists.charactersOf(bwtString),new Function<Character,IndexString>(){
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
		
		List<IndexString> firstRow = Ordering.natural().sortedCopy(lastrow);
		
		
		StringBuilder b = new StringBuilder();
		
		int idx = lastrow.indexOf(new IndexString('$', 1));
		IndexString fChar = firstRow.get(idx);
		while (fChar.getS()!='$'){
			b.append(fChar.getS());
			idx = lastrow.indexOf(fChar);
			fChar = firstRow.get(idx);
		}
		b.append('$');
		
		
		return b.toString();
	}
	
}
