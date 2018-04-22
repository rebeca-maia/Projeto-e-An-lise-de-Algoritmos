/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package firstpart;

/**
 *
 * @author Rebeca Maia <rebeca.maia@alu.ufc.br>
 */
public class CountingSort {
    private static int[] c;
	
	public void CountSort(int[] a, int[]b ,int k){
		c=new int[k+1];
		for(int i=0;i<=k;i++){
			c[i]=0;
		}
		for(int i=0;i<a.length;i++){
			c[a[i]]=c[a[i]]+1;
		}
		for(int i=1;i<=k;i++){
			c[i]=c[i]+c[i-1];
		}
		for(int i=a.length-1;i>=0;i--){
			b[c[a[i]]-1]=a[i];
			c[a[i]]=c[a[i]]-1;
		}
	}
}
