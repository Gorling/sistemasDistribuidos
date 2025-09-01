package ListasThread;

import java.util.List;
import java.util.Random;

/**
 *
 * @author Gabriel Machado
 */
public class PopulaLista extends Thread{
    private final List<Integer> listaIndividual;
    private final int tamanhoDaLista;

    public PopulaLista(List<Integer> listaIndividual, int tamanhoDaLista) {
        this.listaIndividual = listaIndividual;
        this.tamanhoDaLista = tamanhoDaLista;
    }

    @Override
    public void run() {
        Random random = new Random();
        
        for (int i = 0; i < tamanhoDaLista; i++) {
            int numeroAleatorio = random.nextInt(1000, 100001);
            listaIndividual.add(numeroAleatorio);
        }
    }
}
