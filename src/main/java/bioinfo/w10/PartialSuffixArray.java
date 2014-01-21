package bioinfo.w10;

import java.util.ArrayList;
import java.util.List;

import bioinfo.w9.SuffixArray;

public class PartialSuffixArray extends SuffixArray{
	public List<int[]> getPartialSuffixArray(String text,int k){
		List<int[]> parray = new ArrayList<int[]>();
		calculateSuffixArray(text);
		for (int i=0;i<suffixArray.size();i++) {
			int s = suffixArray.get(i);
			if (s % k == 0) {
				parray.add(new int[] {i,s});
			}
		}
		return parray;
	}
	

}
