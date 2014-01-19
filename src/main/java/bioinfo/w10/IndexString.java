package bioinfo.w10;

public class IndexString implements Comparable<IndexString>{
	private char s;
	private int i;
	
	public IndexString(char s, int i) {
		super();
		this.s = s;
		this.i = i;
	}
	
	public int compareTo(IndexString o) {
		int c = s-o.s;
		if (c==0){
			return i-o.i;
		}else{
			return c;
		}
	};
	
	@Override
	public String toString() {
		return ""+s+":"+i;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + i;
		result = prime * result + s;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		IndexString other = (IndexString) obj;
		if (i != other.i)
			return false;
		if (s != other.s)
			return false;
		return true;
	}

	public char getS() {
		return s;
	}

	public int getI() {
		return i;
	}
	
	
	
	
}