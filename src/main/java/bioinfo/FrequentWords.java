package bioinfo;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import com.google.common.collect.Maps;

public class FrequentWords {

	static class KMer implements Comparable<KMer>{
		private String kMer;
		private List<Integer> foundAt = new ArrayList<Integer>();
		public KMer(String kMer) {
			super();
			this.kMer = kMer;
		}
		
		public KMer(String kMer,int firstIndex) {
			super();
			this.kMer = kMer;
			foundAt(firstIndex);
		}
		
		public void foundAt(int index) {
			foundAt.add(index);
		}
		
		public int occurences() {
			return foundAt.size();
		}
		@Override
		public String toString() {
			return kMer+"("+occurences()+")";
		}

		@Override
		public int hashCode() {
			return kMer.hashCode();
		}
		
		public Collection<Integer> indices(){
			return Collections.unmodifiableCollection(foundAt);
		}

		@Override
		public boolean equals(Object obj) {
			return obj!=null && obj instanceof KMer  && kMer.equals(((KMer) obj).kMer) ;
		}

		public String getkMer() {
			return kMer;
		}
		
		public int compareTo(KMer o) {
			if (occurences() - o.occurences() !=0) {
				return occurences() - o.occurences(); //revese sorting (larger first 
			}else {
				return kMer.compareTo(o.kMer); //NAtural ordering on name if occurences are the same;
			}
		}
		
		public String reverse() {
			StringBuilder reverse = new StringBuilder();
			for (char c:kMer.toCharArray()) {
				char complement;
				switch (c) {
				case 'A':
						complement = 'T';
						break;
					case 'T':
						complement = 'A';
						break;
					case 'G':
						complement = 'C';
						break;
					case 'C':
						complement = 'G';
						break;
					default:
						throw new IllegalArgumentException("Illegal acid "+c);
					}
					reverse.append(complement);
				}
			return reverse.reverse().toString();
		}
	}
	
	public static SortedSet<KMer> findKmers(String input,int k){
		Map<String,KMer> map = new HashMap<String, FrequentWords.KMer>();
		
		for (int i=0;i<input.length()-k;i++) {
			String km = input.substring(i,i+k);
			if (map.containsKey(km)) {
				KMer kmer = map.get(km);
				kmer.foundAt(i);
			}else {
				KMer kmer = new KMer(km, i);
				map.put(km, kmer);
			}
		}
		
		SortedSet<KMer> kmerSet = new TreeSet<KMer>();
		for (KMer kmer:map.values()) {
			kmerSet.add(kmer);
		}
		
		
		return kmerSet;
	}
	
	public static void main(String[] args) throws Exception{
		int k=13;
//		String input = IOUtils.toString(FrequentWords.class.getResourceAsStream("frequent_words_input"));
		String input = "TGCCTCCGGTGCGGTGAAGCCCGGGTGGGTCAAGCCCGTGCCTCAAGCCCGTGCCTCGGTGGGTCCGGTGTGCCTCAACAGAGGTGGGTCCGGTGAACAGAAACAGACGGTGAACAGAAACAGAAACAGAAACAGAGGTGGGTCAACAGATGCCTCGGTGGGTCAACAGATGCCTCGGTGGGTCTGCCTCCGGTGCGGTGCGGTGGGTGGGTCTGCCTCGGTGGGTCAAGCCCGAACAGAAAGCCCGCGGTGAAGCCCGTGCCTCCGGTGTGCCTCAAGCCCGAACAGAGGTGGGTCGGTGGGTCAACAGAAAGCCCGTGCCTCAACAGATGCCTCAAGCCCGAAGCCCGGGTGGGTCCGGTGCGGTGTGCCTCGGTGGGTCGGTGGGTCCGGTGAAGCCCGCGGTGAAGCCCGAAGCCCGAACAGACGGTGTGCCTCAAGCCCGCGGTGCGGTGAACAGATGCCTCAACAGATGCCTCCGGTGCGGTGAAGCCCGCGGTGAACAGAAAGCCCGTGCCTCAAGCCCGAAGCCCGCGGTGCGGTGCGGTGCGGTGAAGCCCGTGCCTCCGGTGTGCCTCAAGCCCGAACAGAGGTGGGTCCGGTGGGTGGGTCTGCCTCGGTGGGTCCGGTGAACAGACGGTGAACAGAAACAGACGGTGAACAGATGCCTCGGTGGGTCCGGTGAACAGAAACAGAAAGCCCGGGTGGGTCAACAGAAAGCCCGAAGCCCGCGGTGAACAGAAAGCCCGAACAGACGGTGAAGCCCGCGGTGTGCCTCAAGCCCGGGTGGGTCCGGTGAAGCCCG";
		String output = IOUtils.toString(FrequentWords.class.getResourceAsStream("frequent_words_output"));
		
		List<String> outputs = Arrays.asList(output.trim().split(" "));
		
		Set<KMer> kmers =findKmers(input, k);
		
		
		
		for (KMer fKmer:kmers) { 
			System.out.print(fKmer+" ");
		
		}
		
	}
}
