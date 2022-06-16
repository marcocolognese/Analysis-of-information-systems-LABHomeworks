
# Homework di Laboratorio di Analisi dei Sistemi

## Esercizi

### Esercizio 1
Implementare dei test di unità adeguati a verificare la correttezza delle procedure viste a lezione per il calcolo del codice fiscale, in modo tale da ottenere una copertura dei sorgenti quanto più vicina al 100%. Motivare adeguatamente l’eventuale mancato raggiungimento del 100% di copertura.
    
### Esercizio 2
Implementare in Python una procedura non ricorsiva per il calcolo dell’IRPEF. Implementare quindi dei test di unità adeguati a verificare la correttezza della procedura implementata, in modo tale da ottenere una copertura dei sorgenti quanto più vicina al 100%. Motivare adeguatamente l’eventuale mancato raggiungimento del 100% di copertura.

### Esercizio 3
Implementare in Python una procedura per il calcolo della Pasqua.
Implementare quindi dei test di unità adeguati a verificare la correttezza della procedura implementata, in modo tale da ottenere una copertura dei sorgenti quanto più vicina al 100%. Motivare adeguatamente l’eventuale mancato raggiungimento del 100% di copertura.

### Esercizio 4
Utilizzando gli strumenti di analisi dinamica introdotti nel corso del laboratorio, verificare la possibilità di monitorare i fork di processo ed analizzare lo scambio di messaggi tra processo padre e figlio. \
Verificare la possibilità di furto di dati sensibili, quali credenziali di accesso, ad esempio effettuando tale attività sul processo sshd.

### Esercizio 5.A (semplificato)
Implementare una procedura che tenta di scrivere in un file posto in una directory per cui non è concessa autorizzazione di scrittura o accesso (e.g. /var). \
Utilizzando gli strumenti di analisi dinamica introdotti nel corso del laboratorio, verificare la possibilità di monitorare tali tentativi di scrittura e gestirli generando un log.

### Esercizio 5.B (complesso)
Implementare in C una procedura che accede ad aree di memoria scelte in modo casuale. \
Utilizzando gli strumenti di analisi dinamica introdotti nel corso del laboratorio, verificare la possibilità di monitorare i tentativi di accesso ad aree di memoria non allocate al processo e gestirli generando un log.