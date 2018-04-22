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
public class HeapSort {
    
    public HeapSort(int v[]) {
        construirMaxHeap(v);
        int n = v.length;
        
        for (int i = v.length-1; i > 0; i--) {
            swap(v,i,0);
            maxHeapify(v,0, --n);
        }
    }
    
    private void construirMaxHeap(int[] v) {
        for (int i = v.length / 2 ; i >= 0; i--)
            maxHeapify(v, i, v.length);

    }
    
    private void maxHeapify(int[] v,int pos, int tamanhovetor){
        int max = pos +1, direita = max +1;
        if(max < tamanhovetor){
            if(direita < tamanhovetor && v[max] < v[direita])
                max = direita;
            if(v[max] > v[pos]){
                swap(v,max,pos);
                maxHeapify(v, max, tamanhovetor);
            }
        }
    }
    
    private void swap(int[] v, int j, int aposJ) {
        int aux = v[j];
        v[j] = v[aposJ];
        v[aposJ] = aux;
    }
}
