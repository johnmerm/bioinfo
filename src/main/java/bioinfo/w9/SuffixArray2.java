package bioinfo.w9;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import org.apache.commons.io.IOUtils;

public class SuffixArray2{
	
	private String text;
	private Integer[] suffixArray;
	

	public SuffixArray2(String text) {
		super();
		this.text = text;
		
		
		List<Integer> suffixSet = IntStream.range(0, text.length()).mapToObj(Integer::valueOf).sorted((o1,o2)->{
			String s1 = text.substring(o1)+text.substring(0,o1);
			String s2 = text.substring(o2)+text.substring(0,o2);
			return s1.compareTo(s2);
		}).collect(Collectors.toList());
		suffixArray = suffixSet.toArray(new Integer[text.length()]);
	}
	
	public String firstCol(){
		return Arrays.stream(suffixArray).map(text::charAt).map(String::valueOf).collect(Collectors.joining());
	}
	
	private String lastCol;
	public String lastCol(){
		if (lastCol == null){
			lastCol = Arrays.stream(suffixArray)
					.map(i->(i+text.length()-1)%text.length())
					.map(text::charAt).map(String::valueOf).collect(Collectors.joining()); 
		}
		return lastCol;
	}
	
	public String burrowWheelerTransform(){
		String lastCol = lastCol();
		
		StringBuilder builder = new StringBuilder();
		char prev = lastCol.charAt(0);
		int count = 1;
		for (char c:lastCol.substring(1).toCharArray()){
			if (c == prev){
				count ++;
			}else{
				if (count >1){
					builder.append(count);
				}
				builder.append(prev);
				prev = c;
				count = 1;
			}
		}
		
		if (count >1){
			builder.append(count);
		}
		builder.append(prev);
		
		return builder.toString();
	}
	
	static class idx implements Comparable<idx>{
		char s;
		int i;
		
		idx(char s, int i) {
			super();
			this.s = s;
			this.i = i;
		}
		@Override
		public String toString() {
			return s+"("+i+")";
		}
		
		
		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + i;
			result = prime * result + s;
			return result;
		}
		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			idx other = (idx) obj;
			if (i != other.i)
				return false;
			if (s != other.s)
				return false;
			return true;
		}
		public static List<idx> withIdx(String string){
			
			Map<Character,Integer> mi = new HashMap<Character, Integer>();
			List<idx> indices = new ArrayList<idx>();
			
			for (char c:string.toCharArray()){
				int ci = mi.getOrDefault(c, 1);
				indices.add(new idx(c,ci));
				mi.put(c,ci+1);
			}
			return indices;
			
		}
		@Override
		public int compareTo(idx o) {
			if (s == o.s){
				return i-o.i;
			}else{
				return s- o.s;
			}
		}
	}
	
	public static String invert(String lastCol){
		List<idx> lastIdx = idx.withIdx(lastCol);
		String firstCol = lastCol.chars().mapToObj(i->String.valueOf((char)i)).sorted().collect(Collectors.joining());
		
		List<idx> firstIdx = idx.withIdx(firstCol);
		
		
		final idx endidx = new idx('$',1); 
		idx idx = new idx('$',1);
		
		List<idx> reconst = new ArrayList<idx>();
		do{
			int pos = lastIdx.indexOf(idx);
			idx = firstIdx.get(pos);
			reconst.add(idx);
		}while(!idx.equals(endidx));
		
		return reconst.stream().map(i->String.valueOf(i.s)).collect(Collectors.joining());
		
		
	}
	
	public static void main(String[] args) throws IOException {
		
		List<String> lines = IOUtils.readLines(SuffixArray.class.getResourceAsStream("dataset_304_6.txt"));
		String text = lines.get(0).trim()+"$";
		String[] patterns = lines.get(1).trim().split(" ");
		int d = Integer.parseInt(lines.get(2).trim());
		
//		String text = "ACATGCTACTTT$";
//		String[] patterns = "ATT GCC GCTA TATT".split(" ");
//		int d = 1;
		
		List<Integer> ints = indexDiff(text, patterns, d);
		FileWriter outFile = new FileWriter("out.txt");
				
		
		
		String out = ints.stream().map(String::valueOf).collect(Collectors.joining(" "));
		
		
		IOUtils.write(out, outFile);
		
		outFile.flush();
		outFile.close();
				
	}
	
	
	public static List<idx> nextCol(List<idx> last,List<idx> first,List<idx> current){
		return current.stream().map(idx->last.get(first.indexOf(idx))).collect(Collectors.toList());
	}
	
	
	public static Map<idx,idx> transitions(List<idx> last,List<idx> first){
		return last.stream().collect(Collectors.toMap(idx->idx, idx->last.get(first.indexOf(idx))));
	}
	
	
	
	public static List<Integer> indexDiff(String text,String[] patterns,int d){
		
		
		SuffixArray2 sa = new SuffixArray2(text);
		
	
		List<idx> lastIdx = idx.withIdx(sa.lastCol());
		List<idx> firstIdx = idx.withIdx(sa.firstCol());
		
		Map<idx,idx> transitions = transitions(lastIdx, firstIdx);
		
		
		return Arrays.stream(patterns).parallel().flatMap(pattern -> {
		
		
			Map<Integer,idx> test = IntStream.range(0, lastIdx.size()).boxed().collect(Collectors.toMap(i->i, i->lastIdx.get(i)));
			
			Map<Integer,Integer> posToDist = new LinkedHashMap<>();
			
			
			for (int i=pattern.length()-1;i>=0;i--){
				char c = pattern.charAt(i);
				IntStream.range(0, test.size()).forEach(ii->{
					int currDist = posToDist.getOrDefault(ii, 0);
					if (currDist<=d){
						if (test.get(ii).s!=c){
							currDist++;
						}
						posToDist.put(ii, currDist);
						test.put(ii, transitions.get(test.get(ii)));
					}else{
	//					test.remove(ii);
	//					posToDist.remove(ii);
					}
					
				});
			}
			List<Integer> poses = posToDist.entrySet().stream().filter(e->e.getValue()<=d).map(e->e.getKey()).collect(Collectors.toList());
			List<idx> indices = poses.stream().map(i->test.get(i)).collect(Collectors.toList());
			
			return (Stream<Integer>)indices.stream().map(idx->sa.suffixArray[firstIdx.indexOf(idx)]+1);
			
		}).sorted().collect(Collectors.toList());
		
		
		
	}
	
	
}
