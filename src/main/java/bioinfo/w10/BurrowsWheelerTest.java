package bioinfo.w10;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.io.InputStream;

import org.apache.commons.io.IOUtils;
import org.junit.Test;

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

}
