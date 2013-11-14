package bioinfo;

import java.awt.Color;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.io.IOUtils;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import org.jfree.ui.ApplicationFrame;

import com.google.common.base.Function;
import com.google.common.base.Functions;
import com.google.common.base.Joiner;
import com.google.common.collect.Iterables;
import com.google.common.collect.Lists;
import com.google.common.collect.Multimap;
import com.google.common.collect.Multimaps;
import com.google.common.collect.SortedSetMultimap;
import com.google.common.collect.TreeMultimap;

public class Scew {
	public static void main(String[] args) throws Exception{
		
		String input = IOUtils.toString(new FileInputStream("C:\\Users\\grmsjac6.GLOBAL-AD\\AppData\\Local\\Temp\\dataset_7_6.txt"));;
		List<Integer> scew = new ArrayList<Integer>();
		scew.add(0);
		int scewNow=0;
		for (char c:input.toCharArray()) {
			switch (c) {
			case 'C':
				scew.add(--scewNow);
				break;
			case 'G':
				scew.add(++scewNow);
				break;
			default:
				scew.add(scewNow);
				break;
			}
		}
		
		Function<List<Integer>,List<Integer>> findMinima = new Function<List<Integer>, List<Integer>>() {
			public List<Integer> apply(List<Integer> input) {
				TreeMultimap<Integer, Integer> mm = TreeMultimap.create();
				for (int i=0;i<input.size();i++) {
					mm.put(input.get(i), i);
				}
				
				return Lists.newArrayList(mm.get(mm.keySet().first()));
			}
		};
		
		System.out.println(findMinima.apply(scew));
		
		String title = "scew";
		ApplicationFrame frame = new ApplicationFrame(title);
		
		XYSeriesCollection collection = new XYSeriesCollection();
		
		XYSeries xySeries = new XYSeries("scew");
		
		for (int i=0;i<scew.size();i++) {
			xySeries.add(i, scew.get(i));
		}
		
		collection.addSeries(xySeries);
		
		
		String xAxisLabel = "inc";
		String yAxisLabel = "scew";
		JFreeChart chart = ChartFactory.createXYLineChart(title, xAxisLabel, yAxisLabel, collection, PlotOrientation.VERTICAL, true, false, true);
		chart.setBackgroundPaint(Color.white);
		
		ChartPanel chartPanel = new ChartPanel(chart);
		frame.setContentPane(chartPanel);
		frame.pack();
		frame.setVisible(true);
		
	}
}
