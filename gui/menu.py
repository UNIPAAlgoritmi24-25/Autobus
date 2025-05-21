
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
                "nome": "Grafi",
                "btn_text": "Visualizza",
                "btn_action": 8
            },
            {
                "nome": "Alberi",
                "btn_text": "Visualizza",
                "btn_action": 9
            },
            {
                "nome": "Heap",
                "btn_text": "Visualizza",
                "btn_action": 10
            }
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
insertion = []
marge = []
quik = []

Compara = [
{"tipo": 1, "testo": "Comparazione tra algortmi"},
{"tipo": 0, "testo": "Questa pagina ti permette di compare degli algortmi di ordinamento"},
{"tipo": 1, "testo": "Come funziona?"},
{"tipo": 0, "testo": "Generiamo un dataset contenente vari array di diverse grandezze e facciamo risolvere ad ogni algortmo lo stesso dataset prendendo i temppi di ogni eseguzione fatto cio generiamo un grafico"},
{"tipo": 1, "testo": "Come leggo il grafico"},
{"tipo": 0, "testo": "Se vogliamo ottenere i dati di una precisa eseguzione es: Trovare il tempo in secondi che ha impiegato un algortmo a risolvere una tagila Basterà cercare la linea del algortmo e leggere il valore y associato alla taglia che volevamo verificare"},
]

