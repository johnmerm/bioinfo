package bioinfo;

import java.io.FileInputStream;
import java.util.Set;
import java.util.SortedMap;

import org.apache.commons.io.IOUtils;

import bioinfo.FrequentWords.KMer;

import com.google.common.base.Function;
import com.google.common.base.Functions;
import com.google.common.base.Predicate;
import com.google.common.collect.Ordering;
import com.google.common.collect.Sets;

public class ClumpFinder {

	
	
	public static void main(String[] args) throws Exception{
		
		
		
		String file = IOUtils.toString(new FileInputStream("C:\\Users\\grmsjac6.GLOBAL-AD\\AppData\\Local\\Temp\\dataset_4_4.txt"));
		String lines[] = file.split("\n");
		
		//String input = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA";
		
		String input = lines[0].trim();
		String toks[] = lines[1].trim().split(" ");
		final int k=Integer.parseInt(toks[0]);
		final int L=Integer.parseInt(toks[1]);
		final int t=Integer.parseInt(toks[2]);
		
		
		Set<KMer> kMers = FrequentWords.findKmers(input, k);
		
		final Function<KMer, Integer> clump = new Function<FrequentWords.KMer, Integer>() {
			public Integer apply(KMer input) {
				Integer[] indices = input.indices().toArray(new Integer[input.occurences()]);
				int maxT = 1;
				for (int i=0;i<indices.length;i++) {
					int maxJ=1;
					for (int j=i+1;j<indices.length;j++) {
						if (indices[j]-indices[i]<=L-k) {
							maxJ++;
						}
					}
					maxT = Math.max(maxT, maxJ);
				}
				return maxT;
			}
		};
		
		Set<KMer> target = Sets.filter(kMers, new Predicate<KMer>() {
			public boolean apply(KMer input) {
				return clump.apply(input) >=t;
			}
		});
		
		for (KMer kmer:target)
			System.out.print(kmer.getkMer()+" ");		 
		
		
		
		
		
		
	}
}
