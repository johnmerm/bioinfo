package bioinfo.w9;

import java.io.FileWriter;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

import org.apache.commons.io.IOUtils;

import com.google.common.base.Function;
import com.google.common.base.Joiner;
import com.google.common.base.Predicate;
import com.google.common.collect.Iterables;
import com.google.common.collect.Ordering;

public class Trie {
	private Integer id;
	private String label;
	private Trie parent;
	private List<Trie> children;
	
	private Trie() {
		// TODO Auto-generated constructor stub
	}
	private Trie(Integer id, String label, Trie parent, List<Trie> children) {
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
	
	
	
	Trie appendText(String text) { //returns the leaf corresponding to the text
		Trie pos = this;
		for (char c:text.toCharArray()) {
			String label = String.valueOf(c);
			Trie newPos = pos.getChild(label); 
			if (newPos == null) {
				newPos = pos.appendChild(label); 
			}
			pos = newPos;
		}
		return pos;
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
			
			if (children.size()==1) {
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
	public Trie lcr() {
		List<Trie> allLeafs = allLeafs();
		Set<Trie> branches = new HashSet<Trie>();
		for (Trie leaf:allLeafs) {
			Trie l = leaf;
			while (l.parent.children.size()<2) {
				l = l.parent;
			}
			branches.add(l.parent);
		}
		Ordering<Trie> bydepth = Ordering.from(new Comparator<Trie>() {
			public int compare(Trie o1, Trie o2) {
				String p1 = o1.path(false);
				String p2 = o2.path(false);
				
				String s1 = (p1!=null?p1:"")+(o1.label!=null?o1.label:"");
				String s2 = (p2!=null?p2:"")+(o2.label!=null?o2.label:"");
				return s1.length()-s2.length();
			}
		});
		
		
		return bydepth.max(branches);
	}
	@Override
	public String toString() {
		String path = path(true);
		String s = path!=null?path:"";
		s = s + (label!=null?label:"");
		//s = s+ (id!=null?"@"+id:"");
		return s;
	}

	public static Trie suffixTrie(String text) {
		//text = text+"$";
		Trie root = new Trie();
		for (int i = text.length();i>=0;i--) {
			String suffix = text.substring(i);
			Trie leaf = root.appendText(suffix);
			leaf.id = i;
		}
		return root;
	}
	
	
	
	public static void main(String[] args) throws Exception{
		
		InputStream f = SuffixArray.class.getResourceAsStream("dataset_94_8.txt");
		final String text = IOUtils.toString(f).trim();
		
		//final String text = "ATATCGTTTTATCGTT";
		//final String text = "ATAAATG";
		
		long time = System.currentTimeMillis();
		Trie suffixTrie =suffixTrie(text);
		suffixTrie.compress();
		
		Trie lcr= suffixTrie.lcr();
		System.out.println(lcr.path(false)+lcr.label);
		System.out.println("after "+(System.currentTimeMillis()-time)+" ms");
		
		/*suffixTrie.compress();
		
		FileWriter fw = new FileWriter("src/main/java/bioinfo/w9/out.txt");
		
		
		for (Trie t:suffixTrie.allNodes()) {
			if (t.label!=null) {
				fw.write(t.label+"\n");
			}
		}
		
		fw.close();
*/	}
}
