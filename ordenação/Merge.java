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
public class Merge {

    /**
     * @param args the command line arguments
     */
   
    public Merge( int[] v) {
        int[] aux = new int[v.length];
        sort(v, aux , 0 , v.length-1);
    }
    
    private void sort(int[] v, int[] aux, int inicio, int fim){
        if (inicio < fim) {
            int meio = (fim+inicio)/2;
            sort(v, aux, inicio, meio);
            sort(v, aux, meio+1, fim);
            merge(v, aux, inicio,meio, fim);
        }
    }

    private void merge(int[] v, int[] aux, int inicio, int meio, int fim) {
        int soma;
        //issorted
        for (int k = inicio; k <= fim; k++) {
            aux[k] = v[k];
        }
        int i = inicio;
        int j = meio+1;
        for (int k = inicio; k <= fim; k++) {
            if (i>meio) {
                v[k] = aux[j++];
            }else if (j>fim) {
                v[k] = aux[i++];
            }else if (aux[j] < aux[i]) {
                v[k] = aux[j++];
            }else{
                v[k] = aux[i++];
            }
        }
        int u=inicio;
        int t=fim;
        
        for( int k=inicio;k<=fim-1;k++){
            soma=v[u]+v[t];
            if (soma>10){t--;}
            else if(soma<10){u++;}
            else{System.out.println(v[u]+" "+v[t]);}
        }
       
    }
   
    
}
