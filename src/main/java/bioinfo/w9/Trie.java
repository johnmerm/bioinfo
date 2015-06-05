package bioinfo.w9;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import org.apache.commons.io.IOUtils;

import com.google.common.collect.Ordering;

public class Trie {
	
	enum Color{
		RED,BLUE,PURPLE
	}
	
	Integer id;
	String label;
	Trie parent;
	List<Trie> children;
	
	Color color;
	
	Trie() {
		// TODO Auto-generated constructor stub
	}
	Trie(Integer id, String label, Trie parent, List<Trie> children) {
		super();
		this.id = id;
		this.label = label;
		this.parent = parent;
		this.children = children;
	}
	
	
	Trie getChild(String label){
		if (children !=null) {
			for (Trie child:children) {
				if (label.equals(child.label)){
					return child;
				}
			}
		}
		return null;
	}
	
	Trie appendChild(String label) {
		Trie child = new Trie(null, label, this, null);
		if (children == null) {
			children = new ArrayList<Trie>();
		}
		this.children.add(child);
		return child;
	}
	
	
	
	Trie appendText(String text,Color color) { //returns the leaf corresponding to the text
		Trie pos = this;
		for (char c:text.toCharArray()) {
			String label = String.valueOf(c);
			Trie newPos = pos.getChild(label); 
			
			if (newPos == null) {
				newPos = pos.appendChild(label); 
				newPos.color = color;
			}else if (newPos.color !=color){
				newPos.color = Color.PURPLE;
			}
			pos = newPos;
		}
		return pos;
	}
	
	
	public void merge(String text,Color color){
		if (this.color == null){
			this.color = color;
		}else if (this.color !=color){
			this.color = Color.PURPLE;
		}
		for (int i = text.length();i>=0;i--) {
			String suffix = text.substring(i);
			Trie leaf = appendText(suffix,color);
			leaf.id = i;
		}
	}
	int depth() {
		int i=0;
		Trie pos = this;
		while (pos.parent !=null) {
			i+=1;
			pos = pos.parent;
		}
		
		return i;
	}
	String path(boolean visualize) {
		String s = "";
		if (this.parent == null) {
			return null;
		}
		Trie pos = this.parent;
		while (pos.label !=null) {
			if (visualize) {
				s = "("+pos.label+")"+s;
			}else {
				s = pos.label+s;
			}
			pos = pos.parent;
		}
		
		return s;
	}
	
	
	
	public List<Trie> allNodes(){
		List<Trie> allNodes = new ArrayList<Trie>();
		allNodes.add(this);
		if (children !=null) {
			for (Trie ch:children) {
				allNodes.addAll(ch.allNodes());
			}
		}
		return allNodes;
	}
	
	public List<Trie> allLeafs(){
		List<Trie> allNodes = new ArrayList<Trie>();
		
		if (children !=null) {
			for (Trie ch:children) {
				allNodes.addAll(ch.allLeafs());
			}
		}else {
			allNodes.add(this);
		}
		return allNodes;
	}
	
	public void compress() {
		if (children !=null) {
			for (Trie child:children) {
				child.compress();
			}
			
			if (children.size()==1 && color == children.get(0).color) {
				Trie child = children.get(0);
				if (label ==null) {
					label = child.label;
				}else {
					label = label+child.label;
				}
				id = child.id;
				children = child.children;
				if (children!=null) {
					for (Trie c:children) {
						c.parent = this;
					}
				}
			}
		}
		
	}
	
	
	public Set<Trie> branches(){
		List<Trie> allLeafs = allLeafs();
		
		Set<Trie> branches = new HashSet<Trie>();
		for (Trie leaf:allLeafs) {
			Trie l = leaf;
			while (l.parent.children.size()<2) {
				l = l.parent;
			}
			branches.add(l.parent);
		}
		return branches;
	}
	public Trie lcr() {
		
		
		Ordering<Trie> bydepth = Ordering.from(new Comparator<Trie>() {
			public int compare(Trie o1, Trie o2) {
				String p1 = o1.path(false);
				String p2 = o2.path(false);
				
				String s1 = (p1!=null?p1:"")+(o1.label!=null?o1.label:"");
				String s2 = (p2!=null?p2:"")+(o2.label!=null?o2.label:"");
				return s1.length()-s2.length();
			}
		});
		
		
		return bydepth.max(branches());
	}
	@Override
	public String toString() {
		String path = path(true);
		String s = path!=null?path:"";
		s = s + (label!=null?label:"");
		s = s+ "["+color+"]";
		//s = s+ (id!=null?"@"+id:"");
		return s;
	}

	public static Trie suffixTrie(String text,Color color) {
		//text = text+"$";
		Trie root = new Trie();
		root.merge(text,color);
		return root;
	}
	
	
	public static String shortestNonSharedSubstring(String text1,String text2){
		
		
		
		Trie suffixTrie =suffixTrie(text1+"#",Color.RED);
		suffixTrie.merge(text2+"$",Color.BLUE);
		
		
		//suffixTrie.compress();
		List<String> red = suffixTrie.allNodes().stream().filter(n->n.color == Color.RED && n.children !=null).map(n->{
					return n.path(false)+n.label;

				}).sorted((o1,o2)->{
					return o1.length()-o2.length();
				}).collect(Collectors.toList());
		
		
		
		return red.get(0);
	}
	public static void testLCR() throws Exception{
		
		InputStream f = SuffixArray.class.getResourceAsStream("dataset_296_5.txt");
		final String text = IOUtils.toString(f).trim();
		
		//final String text = "AATTTCCGACTTGCATGACGAGTCAGCGTTCCATCTGATCGAGTCTCCGAAGAACAAATACCCCTACTCAGTTGTGAGCCCCTTTACCGTGAGGACAGGGTCCTTGATGTCGTCTCCTAATTTGCGTTGCGGCTCAACATGTTGTACATAGTGGGGCCAGCCCCAGGGATTTTGTAATTTCTACACTCCATATACGGGACAAGGGTGAGCATTTCCGGGCTTGGATAGGGGCTGCAAGAAAATATCTGGACGTAAGAACTTAATGCCATTCCTACATCCTCGATACCTCGTCTGTCAGAGCAATGAGCTGGTTAGAGGACAGTATTGGTCGGTCATCCTCAGATTGGGGACACATCCGTCTCTATGTGCGTTCCGTTGCCTTGTGCTGACCTTGTCGAACGTACCCCATCTTCGAGCCGCACGCTCGACCAGCTAGGTCCCAGCAGTGGCCTGATAGAAAAATTACCTACGGGCCTCCCAATCGTCCTCCCAGGGTGTCGAACTCTCAAAATTCCCGCATGGTCGTGCTTCCGTACGAATTATGCAAACTCCAGAACCCGGATCTATTCCACGCTCAACGAGTCCTTCACGCTTGGTAGAATTTCATGCTCGTCTTTTGTATCCGTGTAAGTAGGAGGCCGCTGTACGGGTATCCCAGCCTTCGCGCTCTGCTGCAGGGACGTTAACACTCCGAACTTTCCATATACGGGACAAGGGTGAGCATTTCCGGGCTTGGATAGGGGCTGCAAGAAAATATCTGGACGTAAGAAGCTCTGAGGGATCCTCACGGAGTTAGATTTATTTTCCATATACGGGACAAGGGTGAGCATTTCCGGGCTTGGATAGGGGCTGCAAGAAAATATCTGGACGTAAGAAGAGTGATGTTTGGAATGCCAACTTCCATGCACGCCAATTGAGCAATCAGGAGAATCGAGTGCTGTTGACCTAGACCTTGTCAGAAGTATGAATTAACCGCGCGTGTAGGTTTGTCGCTCGACCTGCAAGGGTGCACAATCTGGACTGTCGTCGGCGAACGCTTTCATACGCCTACAAACCGCGTTGCTGGTCGAATCGATCTCACCACCGGCCTTGCAGGATTCTAATTATTCTCTCTCGGTGAGACTGCCGGCGGTCCATGGGTCTGTGTTTCGCTTCAAGCAGTGATATACTGGCGTTTTGTGACACATGGCCACGCACGCCTCTCGTTACTCCCAAT$";
		
		long time = System.currentTimeMillis();
		Trie suffixTrie =suffixTrie(text,Color.RED);
		suffixTrie.compress();
		
		Trie lcr= suffixTrie.lcr();
		System.out.println(lcr.path(false)+lcr.label);
		System.out.println("after "+(System.currentTimeMillis()-time)+" ms");
		
		
	}
	public static void main(String[] args) throws IOException {
//		String text1 = "CCAAGCTGCTAGAGG";
//	    String text2 = "CATGCTGGGCTGGCT";
//	    List<String> data = IOUtils.readLines(Trie.class.getResourceAsStream("dataset_296_7.txt"));
//	    
//	    text1 = data.get(0).trim();
//	    text2 = data.get(1).trim();
//	    System.out.println(shortestNonSharedSubstring(text1, text2));
		
		
		String t = "GCCAGCTCTTTCAGTATCATGGAGCCCATGG$";
		Trie trie = suffixTrie(t, Color.RED);
		trie.compress();
		System.out.println(trie.branches().size());
	}
}
