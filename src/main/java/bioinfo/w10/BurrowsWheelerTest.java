package bioinfo.w10;

import static org.junit.Assert.*;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

import com.google.common.base.Function;
import com.google.common.base.Joiner;
import com.google.common.collect.Lists;

public class BurrowsWheelerTest {

	@Test
	public void testBurrowsWheeler() {
		String text= "GCGTGCCTGGTCA$";
		BurrowsWheeler b = new BurrowsWheeler(text);
		
		String bString = b.getBwt();
		assertEquals(bString, "ACTGGCT$TGCGGC");
	}
	
	@Test
	public void testBurrowsWheelerAssignment() throws IOException{
		InputStream f = BurrowsWheeler.class.getResourceAsStream("dataset_97_4.txt");
		String text = IOUtils.toString(f).trim();
		String bString = new BurrowsWheeler(text).getBwt();
		System.out.println(bString);
	}
	
	@Test
	public void testInverse(){
		String text="TTCCTAACG$A";
		String s  = BurrowsWheeler.invert(text);
		assertEquals(s, "TACATCACGT$");
	}
	
	@Test
	public void testInverseAssignment() throws Exception{
		InputStream f = BurrowsWheeler.class.getResourceAsStream("dataset_99_10.txt");
		String text = IOUtils.toString(f).trim();
		String s  = BurrowsWheeler.invert(text);
		System.out.println(s);
		
	}
	
	@Test
	public void testMatching() {
		String bwText = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC";
		
		final BWMatching bwMatching = new BWMatching(bwText);
		
		String patternString = "CCT CAC GAG CAG ATC";
		String[] patterns = patternString.split(" ");
		List<Integer> m= Lists.transform(Arrays.asList(patterns), new Function<String, Integer>() {
			public Integer apply(String input) {
				int r = bwMatching.matchPattern(input);
				return r;
			}
		});
		List<Integer> tgt = Arrays.asList(2,1,1,0,1);
		assertArrayEquals(m.toArray(), tgt.toArray());
		
		
	}
	
	@Test
	public void testMatchingAssignment() throws IOException {
		InputStream f = BurrowsWheeler.class.getResourceAsStream("dataset_101_6.txt");
		String lines[] = IOUtils.toString(f).split("\n");
		
		
		String bwText = lines[0].trim();
		
		final BWMatching bwMatching = new BWMatching(bwText);
		
		String patternString = lines[1].trim();
		
		String[] patterns = patternString.split(" ");
		List<Integer> m= Lists.transform(Arrays.asList(patterns), new Function<String, Integer>() {
			public Integer apply(String input) {
				int r = bwMatching.matchPattern(input);
				return r;
			}
		});
		IOUtils.write(Joiner.on(" ").join(m), new FileOutputStream("out.txt"));
		//System.out.println(Joiner.on(" ").join(m));
	}
	

}
