package bioinfo.w2;
import static bioinfo.w2.ProteinTranslation.map;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Function;
import com.google.common.base.Joiner;
import com.google.common.base.Strings;
import com.google.common.collect.Iterables;

public class PreoteinTranslationReverse {
	static String reverse(String input){
		StringBuilder reverse = new StringBuilder();
		for (char c:input.toCharArray()) {
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

	public static void main(String[] args) throws FileNotFoundException, IOException {
		List<String> lines = IOUtils.readLines(new FileInputStream("/home/giannis/Downloads/dataset_18_6.txt"));
		String dna = lines.get(0);
		String ppt = lines.get(1);
		List<String> encodings = new ArrayList<String>();
		boolean reverse = false;
		for (String dd:new String[]{dna,reverse(dna)}){
			String rna = dd.replaceAll("T", "U");
			
			for (int i=0;i<=rna.length()-3;i++){
				String codon = rna.substring(i,i+3);
				
				
				if (map.get(codon)!=null && map.get(codon).equals(ppt.substring(0,1))){
					int k=1;
					for (int j=i+3;j<=rna.length()-3;j+=3){
						String codon2 = rna.substring(j,j+3);
						if (map.get(codon2).equals(ppt.substring(k, k+1))){
							k++;
							if (k == ppt.length()){
								String rnaToken = rna.substring(i,j+3);
								String dnaToken = rnaToken.replaceAll("U", "T");
								encodings.add(reverse?reverse(dnaToken):dnaToken);
								i = j+2;
								break;
							}
						}else{
							break;
						}
					}
				}
			}
			reverse = ! reverse;
		}
		
		System.out.println(Joiner.on("\n").join(encodings));
	}
}
