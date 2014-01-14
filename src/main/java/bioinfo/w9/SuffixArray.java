package bioinfo.w9;

import java.io.InputStream;
import java.util.SortedSet;
import java.util.TreeSet;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Joiner;

public class SuffixArray {

	static class Element implements Comparable<Element>{
		int i;
		String suffix;
		
		public int compareTo(Element o) {
			return suffix.compareTo(o.suffix);
		}

		public Element(int i, String suffix) {
			super();
			this.i = i;
			this.suffix = suffix;
		}
		
		@Override
		public String toString() {
			
			return String.valueOf(i);
		}
		
	}
	
	public static void main(String[] args) throws Exception{
		InputStream f = SuffixArray.class.getResourceAsStream("dataset_96_3.txt");
		String text = IOUtils.toString(f);
		
//		String text = "AACGATAGCGGTAGA$";
		SortedSet<Element> suffixArray = new TreeSet<SuffixArray.Element>();
		for (int i=0;i<text.length();i++){
			suffixArray.add(new Element(i, text.substring(i)));
		}
		
		
		System.out.print(Joiner.on(", ").join(suffixArray));
		
		
		
		
	}
}
