package bioinfo.w9;

import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

import org.junit.Test;

public class SuffixArrayTest {

	@Test
	public void testMultipleApproximatePatternMatching(){
		String text = "PANAMABANANAS"+"$";
		List<String> tokens=  Arrays.asList("DNA","GCC","GCTA","TATT");
		
		SuffixArray array = new SuffixArray();
		array.calculateSuffixArray(text);
		
		final int distance=1;
		Map<Integer,Integer> distances = new LinkedHashMap<Integer, Integer>();
		Map<Integer,Character> last = array.suffixArray.stream().collect(Collectors.toMap(i->i,i->array.text.charAt((array.text.length()+i)%array.text.length()),(u,v) -> { throw new IllegalStateException(String.format("Duplicate key %s", u)); },LinkedHashMap::new));
		AtomicInteger ii = new AtomicInteger(0);
		
		while (ii.incrementAndGet()<array.text.length()){
			
			Character referenceChar = tokens.get(0).charAt(tokens.get(0).length()-ii.get()); 
			last = array.suffixArray.stream().collect(Collectors.toMap(i->i,i->array.text.charAt((array.text.length()+i-ii.get())%array.text.length()),(u,v) -> { throw new IllegalStateException(String.format("Duplicate key %s", u)); },LinkedHashMap::new));
			
			
			
			
		}
		
		
	}
}
