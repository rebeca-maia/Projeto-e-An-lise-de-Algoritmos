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
public class Main {
     public static void main(String[] args) {
        // TODO code application logic here
        /*
        int[] v = {10, 8, 5, 9, 20, 25, 40, 2, 4, 1};
        
        Merge m = new Merge(v);
        
        //System.out.println("\nDepois de Ordenar: ");
        //for (int j = 0; j < v.length; j++) {
          //  System.out.println(v[j]+","); 
        //}
        
       HeapSort h = new HeapSort(v);
              
        System.out.println("\nDepois de Ordenar: ");
        for (int i = 0; i < v.length; i++) {
            System.out.print(","+v[i]);
        }
        */
        int l[]={2,5,3,0,2,3,0,3};
		int k[]=new int[l.length];
		new CountingSort().CountSort(l, k, 5);
		for(int i=0;i<k.length;i++){
			System.out.print(" "+k[i]+" ,");
		}

     }
}
