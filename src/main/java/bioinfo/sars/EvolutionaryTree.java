package bioinfo.sars;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

import org.apache.commons.io.IOUtils;

public class EvolutionaryTree {

	private int[] distanceMatrix;
	private int n;
	
	
	
	public EvolutionaryTree( int n,int[] distanceMatrix) {
		this.n = n;
		this.distanceMatrix = distanceMatrix;
		
	}

	public int d(int i,int j){
		return distanceMatrix[i*n+j];
	}
	
	
	
	public static int[] fromLines(List<String> lines){
		return lines.stream().map(String::trim).flatMap(s->Arrays.stream(s.split(" "))).mapToInt(Integer::parseInt).toArray(); 
	}
	public static void main(String[] args) throws IOException {
		List<String> lines = IOUtils.readLines(EvolutionaryTree.class.getResourceAsStream("dataset_10329_11.txt"));
		int n = Integer.parseInt(lines.get(0).trim());
		int j = Integer.parseInt(lines.get(1).trim());
		
		/*
		int[] distanceMatrix = {
				0,	13,	21,	22,
				13,	0,	12,	13,
				21,	12,	0,	13,
				22,	13,	13,	0
		};
		*/
		
		int[] distanceMatrix = fromLines(lines.subList(2, lines.size()));
		
		EvolutionaryTree evo = new EvolutionaryTree(n, distanceMatrix);
		System.out.println(evo.leafLimb(j)[0]+","+evo.leafLimb(j)[1]+","+evo.leafLimb(j)[2]);
	}
	
	public static int[][] DM(int[] D){
		int n = (int) Math.sqrt(D.length);
		Object[] DM =  IntStream.range(0, n).mapToObj(i->{
			return IntStream.range(0, n).map(j->D[i*n+j]).toArray();
		}).toArray(int[][]::new);
		
		return (int[][])DM;
	}
	public static int[] limb(int n,int[] D,int j){
		return new EvolutionaryTree(n, D).leafLimb(j);
	}
	
	public int[] leafLimb(int j){
		int minD=Integer.MAX_VALUE,min_i=-1,min_k=-1;
		for (int i=0;i<n;i++){
			if (i == j){
				continue;
			}
			for (int k=0;k<n;k++){
				if (k==j){
					continue;
				}
				int D = (d(i,j)+d(j,k)-d(i,k))/2;
				if (D < minD){
					minD = D;
					min_i = i;
					min_k = k;
				}
			}
		}
		
		return new int[]{minD,min_i,min_k};
	}
}
