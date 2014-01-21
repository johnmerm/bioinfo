package bioinfo.w10;

import static org.junit.Assert.assertEquals;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.List;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

import com.google.common.base.Function;
import com.google.common.base.Joiner;
import com.google.common.collect.Iterables;

public class PartialSuffixArrayTest {

	@Test
	public void testGetPartialSuffixArray() {
		String text = "PANAMABANANAS$";
		int k = 5;
		PartialSuffixArray p = new PartialSuffixArray();
		List<int[]> pr = p.getPartialSuffixArray(text, k);
		String out = Joiner.on("\n").join(Iterables.transform(pr, new Function<int[],String>(){
			public String apply(int[] input) {
				return input[0]+","+input[1];
			}
		}));
		String test = "1,5\n11,10\n12,0";
		assertEquals(test, out);
	}
	
	
	@Test
	public void testGetPartialSuffixArrayAssignment() throws IOException {
		InputStream f = PartialSuffixArray.class.getResourceAsStream("dataset_102_3.txt");
		String lines[] = IOUtils.toString(f).split("\n");
		String text = lines[0].trim();
		int k = Integer.parseInt(lines[1].trim());
		
		PartialSuffixArray p = new PartialSuffixArray();
		List<int[]> pr = p.getPartialSuffixArray(text, k);
		String out = Joiner.on("\n").join(Iterables.transform(pr, new Function<int[],String>(){
			public String apply(int[] input) {
				return input[0]+","+input[1];
			}
		}));
		
		IOUtils.write(out, new FileOutputStream("out.txt"));
		
	}

}
