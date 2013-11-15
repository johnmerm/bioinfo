package bioinfo;

import java.io.FileInputStream;
import java.io.IOException;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

import javax.net.ssl.SSLException;
import javax.net.ssl.SSLSession;
import javax.net.ssl.SSLSocket;

import org.apache.commons.io.IOUtils;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.conn.ssl.X509HostnameVerifier;
import org.apache.http.impl.client.HttpClientBuilder;

import bioinfo.FrequentWords.KMer;

import com.google.common.base.Function;
import com.google.common.base.Functions;
import com.google.common.base.Joiner;
import com.google.common.base.Predicate;
import com.google.common.collect.Iterables;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import com.google.common.collect.Ordering;
import com.google.common.collect.Sets;

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
		
		Set<String> retVariants = new HashSet<String>(variants);
		
		
		
		if (d>1){
			for (String variant:variants){
				retVariants.addAll(getKmerVariants(variant, k, d-1));
			}
		}
		
		
		
		
		
		return retVariants;
	}
	public static void main(String[] args) throws Exception {
		
		
		HttpClient client  = HttpClientBuilder.create().setHostnameVerifier(new X509HostnameVerifier() {
			
			public boolean verify(String arg0, SSLSession arg1) {
				return true;
			}
			
			public void verify(String host, String[] cns, String[] subjectAlts)
					throws SSLException {
			}
			
			public void verify(String host, X509Certificate cert) throws SSLException {
				// TODO Auto-generated method stub
				
			}
			
			public void verify(String host, SSLSocket ssl) throws IOException {
				// TODO Auto-generated method stub
				
			}
		}).build();
		
		boolean sample = false;
		HttpUriRequest request = new HttpGet("https://beta.stepic.org/media/attachments/lessons/9/frequent_words_mismatch_complement.txt");
		String inputString;
		if (sample){
			HttpResponse response =client.execute(request);
			inputString = IOUtils.toString(response.getEntity().getContent());
		}else{
			inputString = IOUtils.toString(new FileInputStream("/home/giannis/Downloads/dataset_8_5(1).txt"));
		}
		String[] lines = inputString.trim().split("\n");
		
		final String input = lines[sample?1:0];
		String tokens[] = lines[sample?2:1].trim().split(" ");
		final int k = Integer.parseInt(tokens[0]);
		final int d = Integer.parseInt(tokens[1]);
		
		/*
		final String input = "ACGTTGCATGTCGCATGATGCATGAGAGCT";
		final int k = 4;
		final int d =1;
		*/
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
				return input > 1;
			}
		});
		Map<String,Integer> patternCount = new HashMap<String, Integer>();
		SortedSet<KMer> allKmers = FrequentWords.findKmers(input, k);
		
		for (String pattern:kMap.keySet() ){
			patternCount.put(pattern, 0);
			for (KMer km:allKmers){
				if (Mismatch.difference(km.getkMer(), pattern)<=d){
					patternCount.put(pattern, patternCount.get(pattern)+1);
					if (Mismatch.difference(km.getkMer(), KMer.reverse(pattern))<=d){
						patternCount.put(pattern, patternCount.get(pattern)+1);
					}
				}
				
				
			}
		}
		
		final Integer maxP = Collections.max(patternCount.values());
		
		
		Ordering<String> order = Ordering.natural().onResultOf(Functions.forMap(patternCount));
		
		Set<String> result = Maps.filterValues(patternCount, new Predicate<Integer>() {
			public boolean apply(Integer arg0) {
				return arg0 == maxP;
			}
		}).keySet();
		
		List<String> reverseResult = Lists.newArrayList(Iterables.transform(result, new Function<String,String>(){
			public String apply(String arg0) {
				return KMer.reverse(arg0);
			}
		}));
		
		System.out.println(Joiner.on(' ').join( Iterables.concat(result,reverseResult)));
	}
	
}
