package bioinfo.w2;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.io.IOUtils;

import com.google.common.collect.HashMultimap;
import com.google.common.collect.Multimap;

public class ProteinTranslation {
	static Map<String, String> map = new HashMap<String, String>();
	static Multimap<String, String> invMap = HashMultimap.create();
	static {
		InputStream is = ProteinTranslation.class.getResourceAsStream("RNA_codon_table_1.txt");
		
		try {
			for (String l:IOUtils.readLines(is)){
				String t[] = l.trim().split(" ");
				if (t.length==2){
					map.put(t[0], t[1]);
					invMap.put(t[1], t[0]);
				}else{
					map.put(t[0], "");
					invMap.put("", t[0]);
				}
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void main(String[] args) throws IOException {
		
		InputStream task = new FileInputStream("/home/giannis/Downloads/dataset_18_3.txt");//ProteinTranslation.class.getResourceAsStream("protein_translate_data.txt");
		List<String> lines=  IOUtils.readLines(task);
		String rna = lines.get(0);
		//String out = lines.get(3);
		
		StringBuilder protein = new StringBuilder();
		for (int i=0;i<=rna.length()-3;i+=3){
			String codon = rna.substring(i, i+3);
			String amino = map.get(codon);
			protein.append(amino);
		}
		System.out.println(protein.toString());
		//System.out.println(out);
		//System.out.println(protein.toString().equals(out));
		task.close();
	}
}
