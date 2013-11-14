package bioinfo;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Function;

public class ReverseComplement {
	public static void main(String[] args) throws Exception{
		String input = IOUtils.toString(new FileInputStream("C:\\Users\\grmsjac6.GLOBAL-AD\\Downloads\\dataset_3_2(3).txt ")).trim();
		
		Function<String,String> reverseComplement = new Function<String,String>() {
			public String apply(String input) {
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
		};
		String ret = reverseComplement.apply(input);
		FileWriter writer  = new FileWriter("reversecomplement");
		writer.write(ret);
		writer.close();
		
	}
}
