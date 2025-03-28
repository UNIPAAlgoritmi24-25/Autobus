# Uso ed esempi
# Dependency
## Matplotlib Plotting

## 1. Algoritmi di Ordinamento 
Gli algoritmi di ordinamento sono degli algoritmi che preso in ingresso una lista di oggetti siano essi numeri, stringhe, o istanze di una classe.
Restituiscono una lista dove ogni uno degli elementi segue la legge secondo la quale l'elemento precedente e minore di quello successivo
>a<sub>1</sub> < a<sub>2</sub> < a<sub>3</sub>

Per far in modo che il software funzioni correttamente anche nel ordinamento di un vettore di oggetti quindi è necessario definire i metodi 
`__lt__` e `__gt__` per poter usare gli operatori di confronto anche su istanze di classi
### 1.1 Counting Sort
- L'algoritmo in oggetto partendo dall'array che deve ordinare crea un nuovo array con l'obbiettivo di contare i valori presenti più volte.
Quindi se questo è l' array di partenza `[2, 3, 0, 2, 3, 2]` verrà creato l' array `[0, 0, 0, 0]` con 4 posizioni perché il valore più alto è 3 
(Deve esistere un indice 3)
- Viene popolato l' array contando le corrispondenze **es: il numero 2 è presente 2 volte la cella all'indice 2 subirà due incrementi**. 
  Ogni volta che facciamo un incremento quel valore viene eliminato dal vettore
  Quindi otterremo i due array `[]` e `[ 1, 0, 3, 2]`
- Ora ricostruiamo il valore originale avendo pero cura di mettere gli elementi in ordine per farlo scansioniamo l' array del conteggio e vediamo 
  che abbiamo 1 elemento con valore 0 lo sappiamo perché l'indicè representa il valore mentre il numero rapresenta il numero di valori
- Quindi inseriamo 1 elemento con valore 0 nell' array e decrementiamo di 1 l'elemento all'indice 0 nell' array di conteggio. Quindi il valore 
  attuale sara `[0]` per l' array di output e `[0, 0, 3, 2]` per l' array di conteggio dato che il valore che stiamo usando è arrivato a 0 ci 
  spostiamo più in là e riprendiamo l'esecuzione.
- fiche non troviamo nessun valore nell' array di conteggio in quel caso abbiamo terminato

L'algoritmo ha una complessità di O(n<sup>2</sup>) ma è importante sottolineare che questo algortmo va utilizato se da una analisi dei dati ci 
accorgiamo che i nostri dati sono doppioni in oltre è preferibile che il numero di elementi sia considerevole
### 1.2 Merge Sort 
### 1.3 Bubblesort  
### 1.4 Insertionsort
### 1.5 Quicksort  

# 2. Strutture Dati  
### 2.1 Liste  

### 2.2 Pile  

### 2.3 Code  

### 2.4 Funzionalità
- Massimo e minimo  
- Ricerca  
- Predecessore e successore  
- Input/Output (File o tastiera)  