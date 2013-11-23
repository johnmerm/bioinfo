package bioinfo.w2;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.SortedSet;
import java.util.TreeSet;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Joiner;
import com.google.common.collect.Ordering;
import com.google.common.primitives.Chars;

public class TheoreticalSpectrum {
	static Map<String,Integer> map = new HashMap<String,Integer>();
	static{
		InputStream is = ProteinTranslation.class.getResourceAsStream("integer_mass_table.txt");
		
		try {
			for (String l:IOUtils.readLines(is)){
				String t[] = l.trim().split(" ");
				map.put(t[0], Integer.parseInt(t[1]));
				
				
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	static int mass(String tok){
		int r = 0;
		for (char c:tok.toCharArray()){
			r += map.get(""+c);
		}
		return r;
	}
	public static void main(String[] args) {
		Map<String,Integer> out = new HashMap<String,Integer>();
		out.put("",0);
		String input = "HCGQQFYELKYDNLA";
		String dInput = input+input;
		int k=0;
		for (int i=0;i<input.length();i++){
			for (int j=1;j<=input.length();j++){
				String tok = dInput.substring(i,(i+j) );
				String otok = new String(Chars.toArray(Ordering.natural().sortedCopy(Chars.asList(tok.toCharArray()))));
				out.put(""+(++k),mass(tok));
			}
		}
		System.out.println(Joiner.on(" ").join(Ordering.natural().sortedCopy(out.values())));
		
	}
	
	
}
