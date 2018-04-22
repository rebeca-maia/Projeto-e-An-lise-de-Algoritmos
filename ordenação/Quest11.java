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
public class Quest11 {
     /*Altere o algoritmo HeapSort para trabalhar com Heaps minimos, ao inves de Heaps maximos.
Argumente porque e melhor trabalhar com Heaps maximos ao inves de Heaps minimos.*/
    
    private int minHeapfy(int A[],int i){
        int n=A.length;
        int l=A[2*i];
        int r=A[2*i+1];
        int menor=i;
        int aux;
        if ((l<=n) && (A[l]<A[i])){
            menor=l;
        }
        if((r<=n)&&(A[r]<A[i])){
            menor=r;
        }
        if(menor!=i){
            aux=A[menor];
            A[menor]=A[i];
            A[i]=aux;
            minHeapfy(A,menor);
        }
        return menor;
    }
    
    private void BuildMinHeap(int[]A){
        int n=A.length;
        for(int i=n/2;i>=1;i--){
            minHeapfy(A,i);
        }
    }
    
    public void heapSort(int[]A){
        int aux;
        BuildMinHeap(A);
        for(int i=A.length;i>=1;i--){
            aux=A[i];
            A[i]=A[1];
            A[1]=aux;
            minHeapfy(A,1);
        }
    }
    
    public void exibir(int[]A){
        for(int i=0;i<=A.length;i++){
            System.out.println(" "+A[i]);
        }
    }
}
