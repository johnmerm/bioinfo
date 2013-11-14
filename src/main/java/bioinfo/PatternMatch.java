package bioinfo;

import java.io.FileInputStream;

import org.apache.commons.io.IOUtils;

public class PatternMatch {
	public static void main(String[] args) throws Exception{
		String file = IOUtils.toString(new FileInputStream("C:\\Users\\grmsjac6.GLOBAL-AD\\AppData\\Local\\Temp\\dataset_3_5.txt"));
		String lines[] = file.split("\n");
		
		String input=lines[1].trim();
		String pattern = lines[0].trim();
		int i=0;
		while (i!=-1) {
			i = input.indexOf(pattern, i+1);
			System.out.print(i+" ");
		}
			
	}
}
