package ListasThread;

import java.util.ArrayList;
import java.util.List;

public class Principal {
   
    public static void main(String[] args) throws InterruptedException {
        final int totalDeListas = 100;
        final int numerosPorLista = 100;
        final int totalDeNumeros = totalDeListas * numerosPorLista;
        
        List<List<Integer>> listaDeListas = criarListas(totalDeListas);
        List<Thread> threadsAtivas = popularListasEmParalelo(listaDeListas, numerosPorLista);
        aguardarThreads(threadsAtivas);
      
        double Total = calcularTotal(listaDeListas);
        double mediaFinal = ((Total)/(totalDeNumeros));
        
        System.out.println("Total: " + Total);
        System.out.println("Media Final: " + mediaFinal);
    }
    
    private static List<List<Integer>> criarListas (int quantidadeDeListas){
        List<List<Integer>> listaDeListas = new ArrayList<>();
        
        for (int i = 0; i < quantidadeDeListas; i++) {
            listaDeListas.add(new ArrayList<>());
        }
        
        return listaDeListas;
    }
    
    private static List<Thread> popularListasEmParalelo (List<List<Integer>> listaDeListas, int numerosPorLista){
        List<Thread> threadsAtivas = new ArrayList<>();
        
        for (List<Integer> listaIndividual : listaDeListas) {
            Thread novaThread = new PopulaLista(listaIndividual, numerosPorLista);
            threadsAtivas.add(novaThread);
            novaThread.start();
        }
        
        return threadsAtivas;
    }
    
    private static void aguardarThreads (List<Thread> listaDeThreads) throws InterruptedException{
        for (Thread threadAtiva : listaDeThreads) {
            threadAtiva.join();
        }
    }
    
    private static double calcularTotal (List<List<Integer>> listaDeListas) {
        double Total = 0;
        
        for (List<Integer> listaIndividual : listaDeListas) {
            for (int numero : listaIndividual){
                Total += numero;
            }
        }
        
        return Total;
    }
    
    private static void exibirConteudoDasListas (List<List<Integer>> listaDeListas) {
        for (List<Integer> listaIndividual : listaDeListas) {
            System.out.println(listaIndividual);
        }
    }
}
