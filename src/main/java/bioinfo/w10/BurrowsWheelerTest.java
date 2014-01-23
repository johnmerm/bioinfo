package bioinfo.w10;

import static org.junit.Assert.*;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

import com.google.common.base.Function;
import com.google.common.base.Joiner;
import com.google.common.collect.Collections2;
import com.google.common.collect.Iterables;
import com.google.common.collect.Lists;
import com.google.common.collect.Ordering;

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
	
	
	@Test
	public void testBetterMatching() {
		String bwText = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC";
		
		final BWMultiMatch bwMatching = new BWMultiMatch(bwText,true,100);
		
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
	public void testMultiMatch() throws IOException {
		InputStream f = BurrowsWheeler.class.getResourceAsStream("dataset_103_4.txt");
		String lines[] = IOUtils.toString(f).split("\n");
		
		
		String text=lines[0].trim();
		
		String patterns[] =new String[lines.length-1];
		List<Integer> tgt = new ArrayList<Integer>();
		
		for (int i=1;i<lines.length;i++) {
			patterns[i-1] = lines[i].trim();
			
			String pattern = patterns[i-1];
			int p=text.indexOf(pattern);
			while (p>-1) {
				tgt.add(p);
				p = text.indexOf(pattern,p+1);
			}
			
		}
		tgt = Ordering.natural().sortedCopy(tgt);
		List<Integer> pos = BWMultiMatch.matchPositions(text, patterns);
		
		List<Integer> cmp1 = new ArrayList<Integer>(tgt);
		cmp1.removeAll(pos);
		
		List<Integer> cmp2 = new ArrayList<Integer>(pos);
		cmp2.removeAll(tgt);
		
		assertTrue(cmp1.size()==0 && cmp2.size()==0);
		
		IOUtils.write(Joiner.on(" ").join(pos), new FileOutputStream("out.txt"));
		
				
		
	}
	
	@Test
	public void cheatMultiMatch() throws IOException {
		InputStream f = BurrowsWheeler.class.getResourceAsStream("dataset_103_4.txt");
		String lines[] = IOUtils.toString(f).split("\n");
		
		
		String text=lines[0].trim();
		
		
		
		List<Integer> pos = new ArrayList<Integer>();
		
		for (int i=1;i<lines.length;i++) {
			String pattern = lines[i].trim();
			int p=text.indexOf(pattern);
			while (p>-1) {
				pos.add(p);
				p = text.indexOf(pattern,p+1);
			}
		}
		
		IOUtils.write(Joiner.on(" ").join(Ordering.natural().sortedCopy(pos)), new FileOutputStream("out.txt"));
		
		
		
	}

}
