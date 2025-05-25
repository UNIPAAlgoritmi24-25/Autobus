
#from gui.frames.sort import quik



scelte = [
    {
        "nome": "Ordinamento",
        "possibili": [
            {
                "nome": "Counting Sort",
                "btn_text" : "Prova",
                "btn_action": 0
            },
            {
                "nome": "Merge Sort",
                "btn_text" : "Prova",
                "btn_action": 1
            },
            {
                "nome": "Bubblesort",
                "btn_text" : "Prova",
                "btn_action": 2
            },

            {
                "nome": "Insertionsort",
                "btn_text" : "Prova",
                "btn_action": 3
            },

            {
                "nome": "Quicksort",
                "btn_text" : "Prova",
                "btn_action": 4
            }
        ]
    },
    {
        "nome": "Strutture Dati Lineari",
        "possibili": [
            {
                "nome": "Pila",
                "btn_text": "Vai",
                "btn_action": 6
            },
            {
                "nome":"Coda",
                "btn_text": "Vai",
                "btn_action": 7
            },
            {
                "nome": "Liste",
                "btn_text": "Vai",
                "btn_action": 8
            }
        ]
    },
    {
        "nome": "Strutture Dati non Lineari",
        "possibili": [
            {
                "nome": "Alberi",
                "btn_text": "Visualizza",
                "btn_action": 8
            },{
                "nome": "Grafi",
                "btn_text": "Visualizza",
                "btn_action": 9
            },
        ]
    }
]

tipi = [
    {
        "nome":"Grafo",
        "desc": "Lorem impulsum doe sit amet e Il file deve essere composto da tre campi che possono essere specificati secondo le norme di comportamento del programma ",
        "btn_action": 11
    },
    {
        "nome": "Matrice",
        "desc": "Lorem impulsum doe sit amet e Il file deve essere composto da tre campi che possono essere specificati secondo le norme di comportamento del programma ",
        "btn_action": 11
    },
    {
        "nome": "Array",
        "desc": "Lorem impulsum doe sit amet e Il file deve essere composto da tre campi che possono essere specificati secondo le norme di comportamento del programma ",
        "btn_action": 11
    },
    {
        "nome": "Pila",
        "desc": "Lorem impulsum doe sit amet e Il file deve essere composto da tre campi che possono essere specificati secondo le norme di comportamento del programma ",
        "btn_action": 11
    },
    {
        "nome": "Coda",
        "desc": "Lorem impulsum doe sit amet e Il file deve essere composto da tre campi che possono essere specificati secondo le norme di comportamento del programma ",
        "btn_action": 11
    },
    {
        "nome": "Albero",
        "desc": "Lorem impulsum doe sit amet e Il file deve essere composto da tre campi che possono essere specificati secondo le norme di comportamento del programma ",
        "btn_action": 11
    },
    {
        "nome": "Lista Concatenata",
        "desc": "Lorem impulsum doe sit amet e Il file deve essere composto da tre campi che possono essere specificati secondo le norme di comportamento del programma ",
        "btn_action": 11
    },
]
counting = [
    {"tipo":1, "testo":"Il Counting Sort "},
    {"tipo":0, "testo":"Il Counting Sort è un algoritmo di ordinamento non comparativo che utilizza un array ausiliario per contare il numero di occorrenze di ciascun elemento."},
    {"tipo":1, "testo":""},
    {"tipo":1, "testo":"Come funziona il test?"},
    {"tipo":0, "testo":"Il programma crea un dataset contenenti dei numeri ordinati in maniera casuale Questi numeri vengono forniti all Algortmo che li ordinera."},
    {"tipo":0, "testo": "Alla fine del'esequzione vedrai i risultati in una tabella sulla destra."},
    {"tipo":1, "testo":""},
    {"tipo":0, "testo":"La sua complessita e di O(n+k) Ma potrebbe degenerare consulta la documentazione per approfondire"},
]

bubble = [
    {"tipo": 1, "testo": "Il Bubble Sort "},
    {"tipo": 0,
     "testo": "Il Bubble Sort è uno degli algoritmi di ordinamento piu semplici usa due cicli con due puntatori per confrontare i valori contenuti nell array."},
    {"tipo": 0,"testo": "La sua complessita e la più alta tra quelle che esaminiamo O(n^2)"},
    {"tipo": 1, "testo": "Come funziona il test?"},
    {"tipo": 0,
     "testo": "Il programma crea un dataset contenenti dei numeri ordinati in maniera casuale Questi numeri vengono forniti all Algortmo che li ordinera."},
    {"tipo": 0, "testo": "Alla fine del'esequzione vedrai i risultati in una tabella sulla destra."},

]
insertion = [
    {"tipo": 1, "testo": "Insertion Sort"},
    {"tipo": 0, "testo": "L'Insertion Sort è un algoritmo semplice che costruisce la lista ordinata un elemento alla volta, spostando ogni nuovo elemento nella posizione corretta."},
    {"tipo": 0, "testo": "Ha una complessità nel caso peggiore di O(n^2), ma è efficiente per piccole quantità di dati o array quasi ordinati."},
    {"tipo": 1, "testo": "Come viene testato?"},
    {"tipo": 0, "testo": "Il programma genera una serie di numeri disordinati che vengono ordinati usando l'Insertion Sort."},
    {"tipo": 0, "testo": "Al termine, i risultati saranno visibili nella tabella dei tempi di esecuzione."},
]

marge = [
    {"tipo": 1, "testo": "Merge Sort"},
    {"tipo": 0, "testo": "Il Merge Sort è un algoritmo divide-et-impera: divide l'array in due metà, le ordina ricorsivamente e le fonde."},
    {"tipo": 0, "testo": "Ha una complessità O(n log n) in tutti i casi, ed è stabile ma utilizza memoria extra."},
    {"tipo": 1, "testo": "In cosa consiste il test?"},
    {"tipo": 0, "testo": "Il sistema crea un dataset disordinato che viene ordinato utilizzando il Merge Sort."},
    {"tipo": 0, "testo": "I risultati finali verranno mostrati in una tabella comparativa con gli altri algoritmi."},
]

quik = [
    {"tipo": 1, "testo": "Quick Sort"},
    {"tipo": 0, "testo": "Il Quick Sort è un algoritmo molto efficiente che sceglie un elemento pivot e partiziona l'array attorno ad esso."},
    {"tipo": 0, "testo": "Nel caso medio ha complessità O(n log n), ma nel caso peggiore può arrivare a O(n^2). Tuttavia, è spesso il più veloce in pratica."},
    {"tipo": 1, "testo": "Come viene eseguito il test?"},
    {"tipo": 0, "testo": "Il test genera un array di numeri casuali che vengono ordinati tramite Quick Sort."},
    {"tipo": 0, "testo": "Alla fine vedrai i tempi di esecuzione nella tabella comparativa."},
]


Compara = [
{"tipo": 1, "testo": "Comparazione tra algortmi"},
{"tipo": 0, "testo": "Questa pagina ti permette di compare degli algortmi di ordinamento"},
{"tipo": 1, "testo": "Come funziona?"},
{"tipo": 0, "testo": "Generiamo un dataset contenente vari array di diverse grandezze e facciamo risolvere ad ogni algortmo lo stesso dataset prendendo i temppi di ogni eseguzione fatto cio generiamo un grafico"},
{"tipo": 1, "testo": "Come leggo il grafico"},
{"tipo": 0, "testo": "Se vogliamo ottenere i dati di una precisa eseguzione es: Trovare il tempo in secondi che ha impiegato un algortmo a risolvere una tagila Basterà cercare la linea del algortmo e leggere il valore y associato alla taglia che volevamo verificare"},
]

