package bioinfo.w2;

import java.util.Arrays;
import java.util.List;

import com.google.common.base.Function;
import com.google.common.collect.Lists;

public class CyclopeptideSequence {

	public static void main(String[] args) {
		String input = "677 265 852 218 443 724 57 97 305 508 580 275 243 346 71 795 708 296 362 0 852 362 402 999 137 779 667 605 87 115 967 933 668 910 465 403 362 561 580 805 530 393 128 380 103 483 218 923 611 160 827 144 433 490 128 637 942 168 315 291 394 459 562 234 1013 690 823 540 676 587 983 955 973 836 845 765 627 247 509 265 1070 942 926 774 225 708 147 805 755 490 708 902";
		List<Integer> integers = Lists.transform(Arrays.asList(input.split(" ")), new Function<String,Integer>(){
			public Integer apply(String arg0) {
				return Integer.parseInt(arg0);
			}	
		});
		
		for (int i=0;i<integers.size();i++){
			for (int j=i+1;j<integers.size();j++){
				int t = integers.get(integers.size()-i-1) - integers.get(integers.size()-j-1);
				System.out.print(t+" ");
				
				
			}
			
		}
		
	}
}
