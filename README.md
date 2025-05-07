# Uso ed esempi

## 0.  Dependency

### 0.1 Matplotlib Plotting

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
L'algoritmo di Bubble Sort è uno degli algoritmi di ordinamento meno efficienti. Come altri algoritmi di ordinamento, ricostruisce un array ordinato partendo da uno non ordinato tramite una serie di scambi.

Il procedimento consiste nell'utilizzare due cicli annidati: il primo punta a un elemento e il secondo punta all'elemento successivo. Se i due 
elementi sono già in ordine, il secondo indice avanza; altrimenti, i due elementi vengono scambiati. Questo processo si ripete fino a quando 
l'intero array risulta ordinato. 

L'algoritmo di Bubble Sort non presenta miglioramenti con array semi ordinati e la sua complessita e di O(n<sup>2</sup>) dato da i due cicli che 
scansionano l'array.

### 1.4 Insertionsort
### 1.5 Quicksort  

# 2. Strutture Dati  
### 2.1 Liste  

### 2.2 Pile  

### 2.3 Code  
 
### 2.4 Alberi
Gli **alberi** sono strutture dati non lineari. Proprio come le liste, ogni nodo contiene informazioni utili a identificare i propri figli, che a loro volta sono nodi. Tuttavia, a differenza delle liste, ogni nodo di un albero può avere più di un singolo successore. Il tipo di albero dipende infatti dal numero di successori che un nodo può avere. Se il numero di figli di ogni nodo è uguale o minore a due, si parla di **albero binario**; altrimenti, si parla semplicemente di **albero** o, se il numero di figli è definito, di **albero N-ario**.

La struttura dati è chiamata "albero" perché ricorda la forma di un albero capovolto. Seguendo questa analogia, il punto iniziale della struttura viene chiamato **radice**, mentre i nodi terminali sono detti **foglie**. Inoltre, vengono chiamate **rami** le connessioni tra i vari nodi, che nel codice sono rappresentate da variabili definite come puntatori ai nodi figli.

Gli alberi possiedono diverse proprietà che li descrivono:

- **Dimensione**: rappresenta il numero totale di nodi contenuti nell'albero.
- **Altezza**: rappresenta il percorso che conta più salti tra la radice e una foglia. Questo è un parametro che preferiamo mantenere basso, perché nelle operazioni che usano gli alberi come strutture dati, l'altezza rappresenta il caso peggiore in termini di complessità computazionale.
- **Livelli**: sono insiemi di nodi che si trovano alla stessa distanza dalla radice, cioè che hanno la stessa profondità (numero di salti dalla radice).

Esistono anche vari modi per chiamare un singolo nodo:
- **Padre**: un nodo che ha almeno un altro nodo sotto di lui.
- **Fratelli**: i nodi che hanno lo stesso nodo padre.
- **Figli**: i nodi che sono sottostanti a un nodo.

Inoltre, viene chiamato **sottoalbero** un albero costituito da un nodo e dai suoi figli.

#### 2.4.1 Alberi di ricerca
Gli **alberi di ricerca** sono particolari alberi nei quali i nodi sono disposti secondo un criterio specifico. Questo ordine facilita la ricerca di un determinato valore senza la necessità di percorrere tutto l'albero. Questo è particolarmente utile quando si utilizzano gli alberi per memorizzare informazioni che devono essere lette frequentemente o quando si lavora con grandi quantità di dati.

La differenza tra un albero non ordinato e un albero ordinato è che la complessità di ricerca scende da **O(n)** a **O(log n)**. Tuttavia, se l'albero non viene bilanciato, la complessità può crescere nuovamente fino a **O(n)**, formando un albero definito **degenerato**, in cui ogni nodo ha un solo figlio e l'albero si riduce a una lista.
 
## 3 Funzionalità

- Massimo e minimo  
- Ricerca  
- Predecessore e successore  
- Input/Output (File o tastiera)  