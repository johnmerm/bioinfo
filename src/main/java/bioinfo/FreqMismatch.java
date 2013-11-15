package bioinfo;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.concurrent.Callable;
import java.util.concurrent.CompletionService;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorCompletionService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

import bioinfo.FrequentWords.KMer;

import com.google.common.base.Function;
import com.google.common.base.Functions;
import com.google.common.base.Joiner;
import com.google.common.base.Predicate;
import com.google.common.collect.HashMultimap;
import com.google.common.collect.Maps;
import com.google.common.collect.Multimap;
import com.google.common.collect.Ordering;
import com.google.common.collect.TreeMultimap;
import com.google.common.util.concurrent.ListeningExecutorService;
import com.google.common.util.concurrent.MoreExecutors;

public class FreqMismatch {
	private static final char acids[]=new char[] {'A','G','C','T'};
	
	private static List<String> getKMers(String input,int k){
		List<String> allKmers = new ArrayList<String>();
		
		for (int i=0;i<=input.length()-k;i++) {
			String kmer = input.substring(i,i+k);
			allKmers.add(kmer);
		}
		
		return allKmers;
	}
	
	
	private static Set<String> getKmerVariants(String kmer,int k,int d){
		Set<String> variants = new HashSet<String>();
		
		for (int i=0;i<k;i++) {
			StringBuilder b = new StringBuilder(kmer);
			for (char c:acids) {
				b.setCharAt(i, c);
				variants.add(b.toString());
			}
		}
		
		return variants;
	}
	public static void main(String[] args) throws Exception {
		
		String inputString = "ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1";
		String tokens[] = inputString.trim().split(" ");
		final String input = tokens[0];
		final int k = Integer.parseInt(tokens[1]);
		final int d = Integer.parseInt(tokens[2]);
		
		Map<String,Integer> kmerCounts = new HashMap<String, Integer>();
		
		List<String> kmers = getKMers(input, k);
		for (String kmer:kmers) {
			Set<String> variants = getKmerVariants(kmer, k, d);
			for (String variant:variants) {
				if (kmerCounts.containsKey(variant)) {
					kmerCounts.put(variant,kmerCounts.get(variant)+1);
					
				}else {
					kmerCounts.put(variant,1);
				}
			}
		}
		
		
		final Integer max = Collections.max(kmerCounts.values());
		
		Map<String,Integer> kMap = Maps.filterValues(kmerCounts, new Predicate<Integer>() {
			public boolean apply(Integer input) {
				return input == max;
			}
		});
		
		Ordering<String> ordering = Ordering.natural().onResultOf(Functions.forMap(kMap));
		
		List<String> results = ordering.reverse().sortedCopy(kMap.keySet());
		
		for (String s:results) {
			System.out.println(s+" "+ kMap.get(s));
		}
		
		
	}
}
