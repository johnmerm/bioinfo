package bioinfo.w9;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import org.apache.commons.io.IOUtils;


public class Checkpoints {

	
	public static void main(String[] args) throws IOException {
		
		List<String> data = IOUtils.readLines(SuffixArray.class.getResourceAsStream("dataset_303_4.txt"));
		String text = data.get(0);
		List<String> cp = data.subList(1, data.size());
		
		
//		String text = "AATCGGGTTCAATCGGGGT";
//		List<String> cp = Arrays.asList("ATCG","GGGT");
		
		List<Integer> cpi =	cp.stream().parallel().flatMap(c->{
			List<Integer> li = new ArrayList<>();
			int i = text.indexOf(c);
			while (i!=-1){
				li.add(i);
				i = text.indexOf(c,i+1);
			}
			return li.stream();
		}).sorted().collect(Collectors.toList());
		FileWriter w = new FileWriter("out.txt");
		cpi.forEach(i->{
			try {
				w.append(i+" ");
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		});
		
		w.close();
		
		
		
		
	}
}
