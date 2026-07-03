Project Management

Introduzione al Project Management

Marco A. Boschetti

Università di Bologna

Introduzione al Project Management

Sommario
● Premessa
● Il mito del garage
● Cambiamento e The Tar Pit
● Complessità
● The Mythical Man-Month
● Joys and Woes of the Craft
● The Surgical Team
● Conceptual Integrity
● The Second-System Effect
● Communication: Passing the Word
● What Documentation Is Required?
● La rivoluzione Agile

2

Premessa

● In questa introduzione utilizziamo alcune idee proposte da Brooks, che
non devono essere considerate come verità assolute, ma costituiscono
una interessante base di discussione.

● Fred Brooks è stato un noto “computer scientist” e “software engineer”
responsabile dei progetti per lo sviluppo della famiglia di computer IBM
System/360 e del sistema operativo IBM OS/360.

● La notorietà di Brooks è dovuta al suo libro “The Mythical Man-Month”
pubblicato nel lontano 1975 e agli articoli che lo hanno accompagnato,
che hanno generato un vivace dibattito che dura ancora oggi.

● Uno degli argomenti proposti da Brooks è riassunto nella seguente frase

nota come Legge di Brooks:

“adding people to a late software project just makes it later”

3

Premessa

● Molti principi enunciati da Brooks sono ancora oggi condivisibili, mentre

altri sono ancora molto dibattuti o considerati obsoleti.

● Altri autori hanno proposto principi diversi e, qualche volta, contrastanti

con quelli enunciati da Brooks.

● Gli approcci agile sembrano essere in contrasto con molti dei principi
enunciati da Brooks. Durante il corso scopriremo come stanno le cose.

● Questa introduzione ha l’obiettivo di proporre alcuni importanti temi di

base che ci accompagneranno per tutto il corso.

● Anche voi potete partecipare alla discussione con vostre considerazioni,

domande, proposte, etc.

4

Il Mito del Garage

https://www.businessinsider.com

5

Il Mito del Garage

Alcune aziende di successo hanno avuto inizio in un garage dove un gruppo
di giovani intraprendenti ha sviluppato soluzioni in grado di competere con
quelle prodotte da aziende strutturate con team più numerosi e organizzati.

https://www.gettyimages.it/immagine/steve-jobs-garage

6

Il Mito del Garage

● Anche Brooks negli anni ‘70 osservava come spesso si leggeva di piccoli

gruppi di programmatori che in un qualche garage scrivevano software in
grado di competere con software prodotti da aziende con team molto più
numerosi e organizzati (esattamente come accade anche oggi).

● Brooks si chiedeva: “why, then, do we not replace large teams - no matter

how well-run - with two and a half men coding away in garages?”

● La risposta, che lo stesso Books forniva, era piuttosto semplice: “the small
systems don’t really compare with the products that require large teams”.

● I software scritti in un garage non hanno richiesto un’approfondita analisi
dei requisiti e dell’architettura, un insieme di test sufficiente, un piano di
manutenzione, una documentazione dettagliata, etc.

7

Il Mito del Garage: Apple Computers

La leggenda vuole che Steve Jobs e Steve
Wozniak svilupparono il loro primo PC in
un garage.

Recentemente Wozniak ha confessato che
la maggior parte del lavoro lo ha svolto nel
suo “cubicolo” presso HP, che però non ha
creduto nel suo progetto.

Però l’essenza non cambia: Wozniak e Jobs
hanno sviluppato il loro primo PC.

Certo che il risultato, seppur funzionante,
era tutto tranne che un “prodotto”.

Cosa gli mancava per essere un prodotto?

8

Il Mito del Garage: Apple Computers

9

Il Mito del Garage: Google

Larry Page e Sergey Brin scrissero la prima versione Google quando erano
entrambi studenti di dottorato alla Stanford University nel loro garage.

10

Il Mito del Garage: Google

L’idea di Google non era originale, anzi sul mercato erano presenti già molti
“web searcher” e “directory”.

                                                 Come ha fatto Google a conquistare il mercato?

11

Il Mito del Garage: Google

I fattori di successo di Google si possono riassumere come segue:

● Funzionava meglio degli altri. L’algoritmo “PageRank” usato da Google

consentiva di ottenere migliori risultati rispetto ai concorrenti.

● Modello di business innovativo. Valorizzazione del dato raccolto invece di
limitarsi a vendere pubblicità o posizionamenti migliori nei risultati delle
ricerche.

● Facilità di utilizzo. L’interfaccia di Google era essenziale e focalizzata sul

servizio che erogava.

● Un progetto chiaro focalizzato sul “FARE” (execution).

Nota: alcuni autori sottolineano come il progetto sia ancora più importante
dell’idea, che può anche evolvere e cambiare. Per questo, sempre più spesso
si parla di “Execution over idea”.

12

Il Mito del Garage: Facebook

Come è nata l’idea di Facebook? Non in un garage, ma in un campus!

Tutto iniziò nel 2003, quando Mark Zuckerberg creò un’applicazione online
chiamata “Facemash”, che consentiva di confrontare delle foto di compagni
di università per determinare “chi era più hotter”.

13

Il Mito del Garage: Facebook

14

Il Mito del Garage: Facebook

● Facebook è un ottimo esempio di un’ottima idea e un’ottima execution:

o Facebook aveva una soluzione che interessava molto il pubblico.

o L’infrastruttura funzionava, scalava e offriva un’ottima UX.

● Cosa mancava? Mancava il Modello di Business.

● Per lungo tempo Facebook non ha saputo come produrre “utili” dalla sua

soluzione.

● Non basta l’idea e la capacità di tradurla in una soluzione concreta, ma è
necessario definire il modello che consentirà alla soluzione di produrre
utili per i “finanziatori”, che sono indispensabili per portare il prodotto
sul mercato.

● Qual è il modello di business di Facebook?

15

Il Mito del Garage: Facebook

● Nel 2020 il modello di business di Facebook era focalizzato per il 98.3%
sulla pubblicità. E’ un problema? Il modello potrebbe essere migliorato?

16

Il Mito del Garage: Facebook

● Cosa sta cambiando? Bisogna preoccuparsi?

17

Il Mito del Garage: Facebook

● Cosa sta cambiando? Bisogna preoccuparsi?

18

Il Mito del Garage: Facebook

● Cosa sta cambiando? Bisogna preoccuparsi?

19

Il Mito del Garage: Facebook

● Cosa sta cambiando? Bisogna preoccuparsi?

20

Dal Garage al Mercato

● In un garage possono nascere buone idee e prototipi interessanti, ma non

prodotti.

● Le soluzioni sviluppate in un garage non hanno richiesto un’approfondita
analisi dei requisiti e dell’architettura, un insieme di test sufficiente, una
documentazione dettagliata, un piano di manutenzione, etc.

● Per portare sul mercato un prodotto è necessario fare un piano.

● Se siamo una start-up e cerchiamo finanziatori la prima cosa da scrivere è

un business plan con un modello di business convincente.

● Gli elementi fondamentali possono essere sintetizzati in due keywords:

Goal

Progetto

21

Goal e Progetto

● Come vedremo elementi fondamentali saranno il goal, che definirà cosa
deve essere fatto, e il progetto che consentirà di raggiungere il risultato
atteso.

● La definizione del goal è parte integrante del progetto.

● Il progetto richiede un’attenta gestione per garantire il rispetto del goal,
far fronte ai cambiamenti e alla complessità, impiegare “bene” le risorse
disponibili (tra cui il tempo e il denaro), organizzare e dirigere il team, le
comunicazioni, la documentazione, etc...

● Scopriremo durante il corso che definire degli approcci e delle buone

pratiche di riferimento può essere di grande aiuto.

● Più avanti formalizzeremo la definizione di progetto e quella di gestione
di progetto. Per il momento cercheremo di evidenziare alcuni aspetti
rilevanti indentificati già da Brooks e daremo una prima definizione del
mondo agile.

22

Cambiamento

● Brooks implicitamente intende dire che per fare un progetto è necessario
svolgere un’approfondita analisi dei requisiti e dell’architettura, produrre
una documentazione dettagliata, etc.

● Per Brooks il risultato dell’analisi è un progetto a cui bisogna attenersi
rigidamente. Ovviamente questa visione di Brooks può risultare anche
piuttosto limitata e datata. Comunque lo stesso autore sostiene che “the
only constancy is change itself” e aggiunge la raccomandazione “plan the
system for change”.

● Oggi alcuni approcci progettuali (e.g., agile) non impongono un’analisi
dettagliata e vincolante, ma assumono a priori che i requisiti possono
essere modificati in corso d’opera.

● Per esempio, quando si usano approcci agile si deve considerare un

aspetto fondamentale: i requisiti possono cambiare e il progetto deve
essere sufficientemente flessibile per accogliere i cambiamenti.

23

Cambiamento

● Il cambiamento può riguardare la soluzione che si sta sviluppano (e.g.,

modifica dell’idea iniziale, cambio di tecnologia, etc.) oppure le risorse a
disposizione (e.g., taglio del budget, ritardi nell’implementazione che
riducono il tempo a disposizione, etc.).

● Il cambiamento deve essere gestito e un “buon piano” può aiutarci ad

affrontarlo nel “modo migliore”.

● Come vedremo, il cambiamento può essere dovuto a molteplici fattori

interni o esterni rispetto al progetto.

● Sarà importante prevedere i possibili cambiamenti (dove possibile) ed

essere pronti a gestire il cambiamento nel modo corretto.

● Il cambiamento è fonte di stress per il personale coinvolto nel progetto e

lo stress può produrre ulteriori problemi.

24

Cambiamento

Figura: La Brea Tar Pits dipinta da Charles R. Knight.

● La “tar pit” è una palude/lago di bitume. Brooks usa la seguente metafora:

“Software like a tar pit: The more you fight it, the deeper you sink!”

25

Cambiamento

26

Cambiamento

27

Complessità

● Progetti molto complessi non possono essere suddivisi in tanti tasks

“indipendenti” che possono essere eseguiti senza comunicazioni tra gli
sviluppatori e senza stabilire un insieme di complesse interrelazioni tra i
tasks e gli sviluppatori.

● La complessità non riguarda la difficoltà di implementazione di alcune
parti del sistema software, ma le interrelazioni tra i diversi tasks e gli
sviluppatori.

● La progettazione per quanto accurata e approfondita non rimuove la

complessità, ma consente di gestire la complessità.

● Un programma è un insieme di istruzioni che implementa una o più
funzionalità. Scrivere un programma non equivale a realizzare un
prodotto.

● Solitamente un team di 2–3 programmatori in un garage produce un

programma.

28

Complessità

● Un prodotto è qualcosa di più di un programma:

o deve essere adeguatamente testato (la probabilità di incorrere in

un malfunzionamento deve essere la più bassa possibile);
o può essere utilizzato in diversi ambienti e con molti set di dati;
o può essere eseguito, testato e modificato da chiunque;
o la documentazione deve essere dettagliata e completa.

● Brooks stima che mediamente il costo per realizzare un prodotto è tre

volte il costo per realizzare un programma.

● Non è importante determinare se la stima di Brooks sia corretta o

meno. E’ importante il principio: “realizzare un prodotto è molto più
oneroso rispetto a scrivere un programma”.

29

Complessità

● Un sistema software è un insieme di prodotti che interagiscono tra loro
per supportare dei processi complessi. Un sistema deve soddisfare i
seguenti requisiti:

o la modalità di integrazione dei componenti deve essere definita

con precisione;

o input e output devono rispettare dei tracciati ben precisi, che
definiscono le interfacce di comunicazione tra i componenti;

o deve essere testata l’integrazione tra i diversi componenti;
o alcune risorse disponibili sono limitate.

● Brooks stima che mediamente il costo per realizzare un sistema è tre
volte il costo per realizzare un prodotto e, quindi, nove volte il costo
richiesto per realizzare un programma.

● Anche qui non è importante il “numero” fornito da Brooks, ma è

importante notare che c’è un fattore moltiplicativo non trascurabile.

30

Complessità

● Brooks distingue tra accidental complexity e essential complexity.

● La accidental complexity riguarda gli aspetti tecnici relativi alle tecnologie
impiegate (e.g., linguaggi di programmazione, librerie, strumenti di test e
building, etc.). Può essere ridotta, anche in modo sensibile, migliorando
le tecnologie a disposizione, come di fatto sta avvenendo.

● La essential complexity riguarda il problema che bisogna risolvere per
realizzare il sistema. La complessità del problema è costituita dalle sue
diverse componenti che devono essere integrate. Questa complessità è
difficile da ridurre.

● Il famoso claim di Brooks è che non esiste un “silver bullet” per ridurre in
modo sensibile la complessità essenziale, in particolare aggiunge che:
“there is no single development, in either technology or management
technique, which by itself promises even one order of magnitude
improvement within a decade in productivity, in reliability, in simplicity.”

31

The Mythical Man-Month

● La domanda fondamentale che si pone Brooks è la seguente:

“Why does software fail?”

● I motivi principali possono essere ricercati nei seguenti fattori:

o Mancato rispetto degli obiettivi (integrità concettuale violata);
o Difficoltà nella stima corretta dei tempi (e.g., troppo spesso lo

sviluppatore sottostima volutamente il tempo per compiacere il
management);

o Troppo ottimismo (i.e., lo sviluppatore non pensa mai che le cose

potrebbero andare male);

o La convinzione che l’impegno da solo assicuri l’avanzamento del

progetto (Effort ≠Progress);

o Mancato monitoraggio dello stato di avanzamento rispetto a quanto

preventivato;

o Ritardi dovuti all’aggiunta di nuovo personale al progetto.

32

The Mythical Man-Month

● Dorothy Sayers nel suo libro “The Mind of the Maker” suddivide il

processo creativo in tre fasi: l’idea, l’implementazione e l’interazione.

● Brooks fornisce un’efficace sintesi di questa decomposizione del

processo creativo:
“A book, then, or a computer, or a program comes into existence first
as an ideal construct, built outside time and space, but complete in the
mind of the authors. It is realized in time and space, by pen, ink, and
paper, or by wire, silicon, and ferrite.
The creation is complete when someone reads the book, uses the
computer, or runs the program, thereby interacting with the mind of
the maker.”

● Brooks sottolinea una triste realtà: gli sviluppatori sono ottimisti!

Pensano che tutto debba andare sempre bene. Purtroppo, eventuali
errori e inconsistenze presenti nell’idea iniziale emergono solo durante
l’implementazione e l’interazione degli utenti con la soluzione.

33

The Mythical Man-Month

● Tutti i task hanno una probabilità non nulla di fallire o subire ritardi.

● La probabilità che tutto vada bene è prossima allo zero!

● I costi dipendono strettamente dalle risorse impiegate (compreso il
tempo/uomo del personale coinvolto nel progetto), ma la velocità di
avanzamento di un progetto non dipende strettamente dalla quantità
di risorse allocate.

● Il semplice uso del “man month” (mese-uomo) come misura delle

risorse disponibili è sbagliato e pericoloso.

● La Legge di Masson dice che “esiste un tempo minimo di sviluppo che
non può essere ridotto ulteriormente, anche aumentando le risorse
disponibili”.

Esempio: Un progetto che richiede 100 mesi/uomo non dura 1 mese
se si impiegano 100 sviluppatori.

34

The Mythical Man-Month

Esempio:

Consideriamo l’esempio di un pit-stop per il cambio gomme in un gran
premio di Formula 1.

35

The Mythical Man-Month

Valutiamo le seguenti ipotesi, assumendo che siano sempre disponibili due
meccanici che si occupano esclusivamente del sollevamento dell’auto:

● Se il team impiegasse un solo meccanico per il cambio delle 4 gomme

impiegherebbe un tempo T.

● Se i meccanici impiegati per il cambio gomme fossero 2 si potrebbe

sperare di dimezzare il tempo T.

● Se i meccanici fossero 3, quanto tempo impiegherebbero?

● Se invece fossero 4?

● Se fossero 8?

● Se fossero 50?

● Come si può notare la funzione non è affatto lineare!

36

The Mythical Man-Month

● Si noti che ogni meccanico ha assegnato un ruolo ben preciso.

37

The Mythical Man-Month

)
i
s
e
m

(
o
p
m
e
T

25

20

15

10

5

0

1

2

3

4

5

6

7

8

9

10

N. Sviluppatori

Figura:  Tempo vs Numero di Lavoratori, nel caso di task

perfettamente partizionabili.

38

The Mythical Man-Month

)
i
s
e
m

(
o
p
m
e
T

25

20

15

10

5

0

1

2

3

4

5

6

7

8

9

10

N. Sviluppatori

Figura:  Tempo vs Numero di Lavoratori, nel caso di task

non partizionabili.

39

The Mythical Man-Month

)
i
s
e
m

(
o
p
m
e
T

25

20

15

10

5

0

1

2

3

4

5

6

7

8

9

10

N. Sviluppatori

Figura:  Tempo vs Numero di Lavoratori, nel caso di task
partizionabili che però richiedono comunicazioni.

40

The Mythical Man-Month

)
i
s
e
m

(
o
p
m
e
T

25

20

15

10

5

0

1

2

3

4

5

6

7

8

9

10

N. Sviluppatori

Figura:  Tempo vs Numero di Lavoratori, nel caso di task con

complesse interrelazioni.

41

The Mythical Man-Month

● I costi per il test di ciò che è stato implementato sono sempre sottostimati.

● Brooks suggerisce che il tempo complessivo di sviluppo è mediamente così

partizionato:

1/3 progettazione e pianificazione;

1/6 implementazione (scrittura del codice);

1/4 test dei componenti (early system test);

1/4 test del sistema quando i componenti sono integrati.

● Svolgere i test significa anche scrivere del codice esclusivamente per
questo scopo. Il costo per scrivere la parte di codice per testare una
funzionalità può superare il costo per produrre il codice necessario per
implementare la funzionalità stessa.

42

The Mythical Man-Month

“Question: How does a large software project get to be one year late?

Answer: One day at a time!”

● Spesso le stime dei tempi sono sbagliate per mancanza di coraggio
(gutless estimating) da parte degli sviluppatori, che non riescono a
contrastare le richieste del management che impone tempi di
realizzazione più stretti e irrealistici.

● I ritardi che si riscontrano nella fase finale dei test sono più difficili da
recuperare, perché tendono a deprimere e mandare nel panico gli
sviluppatori.

● Sviluppatori depressi, nel panico e sotto pressione sono sicuramente

meno produttivi sia in termini di qualità che di quantità.

● Come ci si comporta quando viene riscontrato un ritardo? Come si

modifica il progetto?

43

The Mythical Man-Month

Figura:  Schedulazione originale in cui sono state fissate le

milestone A, B, C e D.

44

The Mythical Man-Month

Figura:  A fronte di un ritardo di un mese sulla milestone A,
ci si limita a posporre le milestone B, C e D.

45

The Mythical Man-Month

Figura:  A fronte di un ritardo di un mese sulla milestone A, si
prevede lo stesso “ritardo” per le milestone B, C e D.

46

The Mythical Man-Month

Figura:  A fronte di un ritardo di un mese sulla milestone A, si

aggiungono 2 sviluppatori per le milestone B, C e D
(devono essere previsti dei tempi di training).

47

Joys and Woes of the Craft

● Le “gioie” del realizzare un software possono essere le seguenti:

o la gioia di creare qualcosa;

o la soddisfazione di fare applicazioni che altre persone useranno;

o il fascino di risolvere rompicapi complessi;

o trovare uno stimolo continuo per la propria curiosità e desiderio

di imparare;

o lavorare con un “mezzo” molto flessibile;

o etc…

48

Joys and Woes of the Craft

● I “dolori” del realizzare un software possono essere i seguenti:

o bisogna essere molto precisi;

o spesso non c’è controllo di ciò che deve essere prodotto (si dipende

dalle specifiche);

o spesso si deve dipendere da altri programmi e/o programmatori;

o il debug (spesso scovare e correggere bugs è difficile e frustrante);

o quando si termina un progetto solitamente il prodotto è già

obsoleto;

o etc…

49

Joys and Woes of the Craft

● Nella gestione di un progetto è necessario tener conto sia degli aspetti

positivi (gioie) che di quelli negativi (dolori).

● Per motivare lo staff si può far leva sugli aspetti positivi. Come?

● La flessibilità del mezzo come incide sull’organizzazione del progetto?

Quali sono gli aspetti positivi?

● Quali insidie nascondono gli aspetti negativi? Quali sono i problemi che
potrebbero emergere durante un progetto? Come si possono eliminare
o gestite le possibili insidie?

● Questi aspetti (positivi e negativi) sono fondamentali nella gestione dei

progetti e ricorreranno spesso durante il corso.

50

Il Team

● Per la riuscita di progetto uno degli elementi fondamentali è il Team.

● La corretta composizione del Team è un prerequisito fondamentale per

una corretta ed efficiente gestione del Team stesso.

● La composizione del team è fortemente influenzata dall’ambito del

progetto e dalle metodologie che si intende utilizzare.

● Prenderemo in considerazione due proposte molto alternative:

o Un team molto “tradizionale”, che prevede numerose figure

molto specializzate.

o Un team molto “agile”, dove sono definite poche figure e in cui

tutti devono saper fare tutto.

● Queste due proposte sono solo due esempi, che ci permettono di
individuare i ruoli principali che devono coprire i componenti di un
team.

51

The Surgical Team

● Per quanto riguarda l’organizzazione del lavoro per un generico progetto
di sviluppo di software, Harlan Mills suggerì un approccio che nella sua
“essenza” è adottato ancora oggi.

● Mills suggerì di affidare i tasks di un progetto a dei team di dimensioni

“limitate” organizzati come un “surgical team”.

● Secondo Mills il team doveva prevedere le seguenti figure:

o chirurgo;
o copilota;
o amministratore;
o editor;
o segretaria;
o program clerk;
o toolsmith;
o tester;
o language lawyer.

52

The Surgical Team

● Chirurgo: dirige il team. Prende tutte le decisioni sull’architettura e sulle
specifiche sia funzionali che relative alle performance, codifica le parti
più impegnative, testa il codice e scrive la documentazione.

● Copilota: è l’alter-ego del chirurgo ed è in grado di fare tutto quello che
fa il chirurgo, ma ha meno esperienza. Il chirurgo condivide con lui tutte
le scelte progettuali, ma il suo parere può essere ignorato.

● Amministratore: il chirurgo ha pieni poteri e controlla anche gli aspetti
amministrativi del suo team, ma ha bisogno di un amministratore come
esecutore delle sue direttive. L’amministratore è in genere condiviso da
più team.

● Editor: anche la documentazione è responsabilità del chirurgo, ma
l’editor provvede a correggerla, organizzarla, aggiornarla a fronte di
modifiche, etc.

53

The Surgical Team

● Toolsmith: si occupa di realizzare, installare, manutenere tutti gli

strumenti e le risorse necessarie agli sviluppatori.

● Tester: si occupa di preparare ed eseguire i test per i diversi casi d’uso,
cercando di individuare insiemi di dati rappresentativi delle diverse
situazioni in cui si troverà a operare il software. Tra i dati raccolti per i
test vi sono anche quelli corrispondenti a casi reali che hanno causato
malfunzionamenti.

● Program Clerk: è un impiegato che supporta l’amministratore e l’editor,

ma ha anche conoscenze e responsabilità tecniche.

● Segretario: supporta in particolare l’amministratore e l’editor e non

deve avere conoscenze tecniche.

● Language Lawyer: si occupa di definire come usare il linguaggio di

programmazione impiegato per l’implementazione di particolari parti
di codice (agli albori dell’informatica era fondamentale).

54

The Surgical Team

● Oggigiorno, e soprattutto nelle aziende medio-piccole, alcuni ruoli sono

interpretati dalla stessa persona.

● L’evoluzione tecnologica e metodologica ha trasformato alcuni ruoli, in

alcuni casi depotenziandoli e in altri potenziandoli.

● Nei diversi approcci progettuali proposti in letteratura sono considerate

anche altre tipologie di organizzazione del team.

● Negli ultimi anni la tendenza e quella di avere dei team “orizzontali” in
cui gli sviluppatori gestiscono direttamente molte delle mansioni del
surgical team.

● Indipendentemente dall’organizzazione adottata, la proposta di Mills ha
il pregio di evidenziare le mansioni che dovrebbero essere coperte
all’interno di un team.

55

The Scrum Team

● Un approccio alla gestione dei progetti sempre più utilizzato negli ultimi

anni è la metodologia Scrum.

● Il termine Scrum, che nel rugby indica la mischia, descrive un approccio
in cui le persone (i.e., il team) sono concentrate sullo stesso obiettivo: il
successo del progetto.

Fonte: www.guidagalatticaperagilisti.com

56

The Scrum Team

● Scrum è un “framework” di project management proposto negli anni
novanta da Ken Schwaber e Jeff Sutherland per lo sviluppo iterativo e
incrementale di prodotti software.

● Nel rugby lo sprint è quel tratto di corsa che si fa per portare avanti il
pallone. In Scrum, “il portatore di palla corre in avanti seguito dai suoi
compagni che lo sostengono: spirito di gruppo, comunicazione, empatia
sono tutte caratteristiche importanti”.

● Quindi in Scrum il lavoro viene suddiviso in iterazioni (gli sprint), che

hanno una durata ben precisa e predeterminata.

● La metodologia Scrum prevedere solo tre ruoli per il personale che

costituisce lo Scrum Team:

o Product Owner;
o Scrum Master;
o Team di sviluppo (Dev Team).

57

The Scrum Team

● Product Owner: ha la responsabilità del prodotto, conosce l’utente e i
suoi bisogni. Il Product Owner (PO) è responsabile del “cosa” sarà
contenuto all’interno del prodotto, ma non del “come” questo verrà
realizzato, che è di competenza del team di sviluppo.

● Scrum Master: il suo ruolo non è quello del “capo” del  team, come il
termine “master” potrebbe far pensare, ma è un coach al servizio del
team, che aiuta la sua crescita, agevola la comunicazione, fa in modo
che si rispettino le indicazioni, etc...

● Team di Sviluppo: è composto da persone che dovrebbero avere tutte

le competenze per sviluppare la soluzione (i.e., le user story inserite nel
loro backlog). Per questo motivo dovrebbero sempre avere la massima
autonomia sulle scelte tecniche, in particolare sul come implementare
le funzionalità.

58

Dimensioni ideali di un Team

● Il tema del dimensionamento del team di sviluppo è molto dibattuto,
ma c’è accordo su un punto: team troppo numerosi sono di difficile
gestione, perché richiedono un alto overhead per le comunicazioni.

● Jeff Bezos’ Two-Pizza Team Rule: secondo Bezos un team deve avere
un numero di componenti che possono essere sfamati da due pizze.

● Quante persone si possono accontentare di due pizze?

● L’idea di Bezos è ormai condivisa da una vasta platea di professionisti

che quantifica le dimensioni ideali in circa 4-8 sviluppatori.

● Quindi, indipendentemente dalle dimensioni dell’azienda e dal numero
di sviluppatori coinvolti in un progetto, i team non devono superare un
certo numero di componenti.

● Sulla composizione c’è la possibilità di puntare a team generalisti (e.g.,
full-stack) o specialisti (che coprono uno specifico dominio) o un mix.

59

Conceptual Integrity

● Il rispetto della conceptual integrity è molto importante, ma al tempo

stesso è difficile definire in cosa consiste.

● Per produrre un sistema efficace, efficiente e user-friendly è necessario
che sia rispettata la sua integrità concettuale, ossia è necessario che le
funzionalità e la loro implementazione risponda solo e solamente ai
requisiti definiti in fase di progettazione.

● Il sistema deve permettere di fare tutto ciò per il quale è stato progettato

(efficacia) e lo deve fare nel modo migliore (efficienza).

● Nessuna funzionalità non prevista nel progetto deve essere implementata
e nell’implementazione ogni funzionalità deve prevedere solo ciò che è
necessario.

● Il motivo è piuttosto semplice: se un sistema è troppo complicato da
usare, allora molte delle sue funzionalità non saranno usate perché
nessun utente ha il tempo e la pazienza di impararle a usare.

60

Conceptual Integrity

● Per mantenere l’integrità concettuale del sistema è necessario separare

l’architettura dall’implementazione.

● Uno o più architetti decidono cosa deve essere presente nel sistema e

cosa invece no. Gli architetti devono tenere in considerazione le esigenze
dell’utente finale.

● L’architetto o il team di architetti devono definire cosa il sistema dovrà

essere, dopodiché devono assicurarsi che la loro visione sia condivisa dal
resto del team.

● Se gli architetti definiscono cosa il sistema dovrà essere, il come dovrà
essere implementato lo dovrà definire il team che si prenderà carico
dell’implementazione del sistema.

● Delegare al team l’implementazione, permette una gestione più efficiente
evitando di sovraccaricare di lavoro l’architetto che può diventare un
“collo di bottiglia”.

61

Conceptual Integrity

● Agli sviluppatori deve essere lasciata la “gioia” di dare libero sfogo alla
propria creatività, a patto che sia rispettata l’integrità concettuale di
quanto progettato dagli architetti. Books riassume questo concetto così:
“Architecture is what happens, and implementation is how it happens”.

● In questo contesto Brooks parla di aristocracy e democracy.

● I pericoli per gli architetti:

o Le specifiche degli architetti potrebbero essere troppo “ricche” e non

considerare in modo adeguato i costi di implementazione.

o Gli architetti si prendono tutto il divertimento lasciando pochi margini
alla creatività degli sviluppatori. Se gli architetti rispettano i confini tra
“what” e “how” l’implementazione può essere divertente.

o Gli sviluppatori devono essere coinvolti quando le specifiche sono

pronte o addirittura quando vengono definite.

62

The Second-System Effect

● Il primo sistema che si progetta/implementa solitamente prevede solo
le funzionalità richieste dall’utente e ha un’implementazione “pulita”.

● Appena il primo sistema è completato ci si accorge che può essere

“migliorato” modificando l’implementazione di alcune funzionalità o
aggiungendone di nuove. Queste nuove idee vengono riservate per il
prossimo progetto.

● Per queste ragioni il secondo sistema viene progettato/implementato
aggiungendo “tutto” ciò che si ritiene di aver dimenticato nel primo
progetto. Però, passare da un “better design” a un “over design” è molto
facile.

● L’over design ha un impatto negativo anche sui costi, perché non valuta

correttamente il rapporto costi/benefici.

● Brooks si raccomanda che il management punti su personale con

almeno due progetti/sistemi alle spalle (cosa ne pensate?).

63

Communication: Passing the Word

Come si comunica?

● Informally: telefono, pausa caffè, instant message, pub, etc...

● Meetings: riunioni sia a cadenza regolare che al bisogno, dove i team
informano gli “altri” (propri colleghi, altri team, manager, etc.) sullo
stato di avanzamento, su eventuali criticità riscontrate, su proposte
progettuali o implementative, etc.

● Workbook: contenitore in cui sono riportate formalmente tutte le
informazioni riguardanti un progetto. Anni fa erano dei documenti
stampati su carta, oggi sono sempre più spesso fruibili via web
utilizzando intranet aziendali, soluzioni cloud, etc.

64

What Documentation Is Required?

“For several years I diligently lectured my software engineering class on
the necessity and propriety of good documentation, exhorting them even
more fervently and eloquently. It didn’t work.
I assumed they had learned how to document properly and were failing
for lack of zeal. Then I tried showing them how the job is done. This has
been much more successful.”

● Documentare il proprio lavoro è fondamentale per:

o indicare il funzionamento di un programma, un componente, etc.;
o ricordarsi a distanza di tempo cosa si è fatto;
o condividere il proprio lavoro con i colleghi;
o definire formalmente le interfacce tra componenti, etc.;
o tenere traccia dei problemi e delle soluzioni (e.g., bugs, etc.);
o stabilire i test case, definire il loro utilizzo, etc.;
o etc...

65

The Manual

● Le specifiche scritte dell’architetto potrebbero essere fornite sotto forma

di manuale.

● Nel manuale dovrebbero essere riportate in dettaglio tutte le specifiche

dell’interfaccia (ossia tutto ciò che l’utente vede).

● Il manuale è “anche” uno strumento per la progettazione, che spesso è

sottovalutato.

● Il manuale può essere modificato dai feedback degli utenti finali e del

team di implementazione.

● Nei capitolati dei progetti sarebbe buona norma riportare il manuale, che
costituisce un insieme di specifiche molto dettagliato e molto efficace
nella fase di test e validazione da parte del cliente.

● Al giorno d’oggi che fine hanno fatto i manuali?

66

The Manual

67

To Use A Program

“Most documentation fails in giving too little overview.
The trees are described, the bark and leaves are commented,
but there is no map of the forest.”

● Ogni utente necessita di una descrizione in “prosa” del software, che sia

sintetica ma esaustiva (compito non facile).

● Questa documentazione dovrebbe essere già disponibile prima che il

software sia implementato.

● Brooks individua i seguenti quesiti a cui bisogna dare una risposta:

o Purpose: Qual è la funzione principale del software?

o Environment: Su quale macchina, configurazione e sistema operativo

girerà il software?

o Domain and Range: Quale dominio dell’input è valido? Quale output

si ritiene ammissibile?

68

To Use A Program

o Function Realized and Algorithm Used: Precisamente cosa permette

di fare il software e come?

o Input-Output Formats: Qual è il formato e il mezzo per effettuare

l’input e output? In questo caso la descrizione deve essere completa
e precisa.

o Operating Instruction: Come si usa? Quali sono le eccezioni e come

si gestiscono?

o Options: Quali scelte può effettuare l’utente? Come queste scelte

devono essere specificate?

o Running Time: Quanto tempo impiega il software per eseguire una
funzionalità su un input di una certa dimensione e su una macchina
con una specifica configurazione?

69

To Use A Program

o Accuracy and Checking: Quanto è precisa la soluzione fornita dal
software? Sono state implementate delle funzionalità per il
controllo dell’accuratezza e della correttezza della soluzione?

70

To Modify a Program

● Come possiamo consentire modifiche e/o correzioni in futuro?

● Come possiamo riutilizzare il lavoro fatto in passato?

● Come possiamo consentire anche ad altri di intervenire sul codice?

71

To Modify a Program

● Per consentire modifiche o correzioni è necessario avere tutti i dettagli

dell’implementazione.

● Chi modifica il codice ha bisogno di avere una chiara e precisa descrizione

della struttura interna dei diversi componenti.

● Per descrivere i diversi componenti con sufficiente dettaglio si possono

individuare i seguenti elementi/strumenti:
o Rappresentazione grafica della struttura di ciascun componente (i.e., flow

charts, etc.).

o Strutture dati utilizzate e definizione degli input e output.
o Completa descrizione degli algoritmi utilizzati nell’implementazione, con

eventuali riferimenti bibliografici, etc.

o Descrizione delle tecnologie utilizzate e dettagli sulle modalità di utilizzo.
o Discussione dei possibili miglioramenti che si possono apportare, dei difetti e

limiti dell’implementazione corrente, etc.

72

Self-Documenting Programs

● Martin Fowler sostiene che il codice stesso può essere considerato la

documentazione principale di un sistema software, ma ci ricorda anche
che non deve essere l’unica documentazione disponibile.

● In effetti un modo molto efficace ed efficiente per documentare il codice

è inserire la documentazione nel codice stesso.

● Per documentare il codice si possono usare i commenti, i nomi delle

variabili, l’indentazione, etc.

● Un vantaggio evidente consiste nel fatto che la documentazione è

“immediatamente” disponibile ed è aggiornata e allineata con il codice
(a patto che lo sviluppatore faccia il proprio dovere aggiornando con
costanza i commenti, etc.).

● Usando delle particolari regole sintattiche nella scrittura dei commenti è
possibile consentire anche la produzione automatica di documentazione,
utilizzando dei software ad hoc (e.g., Doc++, Doxygen, etc.).

73

Self-Documenting Programs

Esempio

…
float O[ND,NG];
float P[ND];
float S[ND];

F1(ND,NG,O);
F2(ND,P)

for (i=0; i<ND; i++)
{

S[i] = 0.0;
for (j=0; j<NG; j++)
{

if (O[i,j]>8)

S[i] += (8 + 1.2 * (O[i,j]-8)) * P[i];

else

S[i] += O[i,j] * P[i];

}

}
…

74

Self-Documenting Programs

Esempio

…
float OreLavorate[NumeroDipendenti,NumeroGiorni];
float PagaOraria[NumeroDipendenti];
float Stipendio[NumeroDipendenti];

LeggiOreLavorate(NumeroDipendenti,NumeroGiorni,OreLavorate);
LeggiPagaOraria(NumeroDipendenti,PagaOraria)

for (i=0; i<NumeroDipendenti; i++)
{

Stipendio[i] = 0.0;
for (j=0; j<NumeroGiorni; j++)
{

if (OreLavorate[i,j]>8) // Straordinario pagato 20% in piu’

Stipendio[i] += (8 + 1.2 * (OreLavorate[i,j]-8)) * PagaOraria[i];

else

Stipendio[i] += OreLavorate[i,j] * PagaOraria[i];

}

}
…

75

Self-Documenting Programs

Esempio: Doxygen

/*! A test class */
class Test
{

public:

/** An enum type.
* The documentation block cannot be put after the enum!
*/
enum EnumType
{

int EVal1, /**< enum value 1 */
int EVal2  /**< enum value 2 */

};

void member(); //!< a member function.

protected:

int value; /*!< an integer value */

};

76

Self-Documenting Programs

Esempio: Doxygen

77

Self-Documenting Programs

Esempio: Doxygen

78

Documents for a Software Project

● Molti progetti di sviluppo software iniziano con numerose riunioni per

definire la struttura, poi si inizia subito a scrivere il codice.

● Anche per progetti di piccole dimensioni sarebbe opportuno produrre

della documentazione.

● Per gestire un progetto software è necessario quanto meno produrre la

seguente documentazione:

o What: objective. Questo documento definisce i bisogni che devono
essere soddisfatti, gli obiettivi, i desiderata, i vincoli e le priorità.

o What: product specifications. La prima versione del documento può
essere solamente una proposta sintetica, ma deve “evolvere” in un
documento completo costituito dal manuale (ciò che vede l’utente)
e una descrizione dettagliata dell’implementazione (a uso interno).

79

Documents for a Software Project

o When: schedule. Descrizione dell’organizzazione di tutte le attività di
progetto (i.e., GANTT, etc.). Può prevedere l’uso di strumenti software
specifici (e.g., Microsoft Project, etc.).

o How much: budget. Questa documentazione è tra le più importanti
per la gestione dei progetti. Il budget può influenzare anche le scelte
tecniche.

o Where: space allocation. Solitamente nella produzione del software
non è un tema fondamentale, però non deve essere sottovalutato e
deve essere considerato.

o Who: organization chart. Documentare l’organizzazione delle risorse
coinvolte nel progetto è fondamentale sia per attribuire i compiti e le
responsabilità sia per stabilire la rete delle comunicazioni (e quindi la
rete delle responsabilità).

80

Documents for a Software Project

● L’organizzazione delle risorse umane e l’assegnazione delle mansioni ha
una forte interrelazione con l’architettura che si deve implementare.
Perciò la documentazione riguardante l’organizzazione deve avere una
corrispondenza biunivoca con la documentazione tecnica.

81

Why Have Formal Documents?

1. Mettere per iscritto le decisioni è fondamentale.

● Solo quando si scrive ci si accorge di eventuali inconsistenze e del gap tra

l’idea e l’implementazione.

● Nello scrivere è necessario prendere numerose “mini-decisioni”, che nella

fase di ideazione non era stato necessario prendere.

2. La documentazione serve per comunicare le decisioni agli altri.

● Se qualche aspetto del progetto non è riportato nella documentazione non

ci si può sorprendere se qualche membro del team lo ignora.

● Se il progetto non è ben documentato è facile che l’integrità concettuale sia

violata e che il prodotto finale non rispetti alcuni requisiti.

● Il compito fondamentale per il management è riuscire a far andare tutti nella
stessa direzione. Quindi il suo compito fondamentale non è solo prendere
decisioni, ma anche comunicare e la documentazione aiuta.

82

Why Have Formal Documents?

3.

La documentazione è un database e una checklist fondamentale per il
progetto.

● La documentazione deve essere continuamente aggiornata e registrare

l’evoluzione del progetto.

● Quando aggiornano la documentazione il management e gli sviluppatori

capiscono dove sono e quali cambiamenti di rotta sono stati eventualmente
apportati.

“The task of the manager is to develop a plan and then to realize it. But
only the written plan is precise and communicable. Such a plan consists
of documents on what, when, how much, where, and who. This small
set of critical documents encapsulates much of the manager’s work. If
their comprehensive and critical nature is recognized in the beginning,
the manager can approach them as a friendly tools rather than
annoying busywork.”

83

La rivoluzione Agile

● Ciò che abbiamo detto finora è in linea con un approccio tradizionale al

project management.

● Negli ultimi anni nell’ambito dello sviluppo software si stanno imponendo
numerosi approcci che sembrano “violare” molti dei principi del project
management tradizionale.

● Uno dei movimenti di maggior successo è quello Agile.

● Le idee ispiratrici del movimento Agile sono riassunte nel noto Manifesto

for Agile Software Development (agilemanifesto.org).

● Il Manifesto è stato redatto nel febbraio del 2001, quando 17 sviluppatori
software si incontrarono allo Snowbird Resort nello Utah per discutere di
metodi di sviluppo “leggeri”.

● A quanto pare non avevano le stesse idee, ma trovarono un accordo su

quattro punti.

84

Manifesto for Agile Software Development

We are uncovering better ways of developing

software by doing it and helping others do it.

Through this work we have come to value:

Individuals and interactions over processes and tools

Working software over comprehensive documentation

Customer collaboration over contract negotiation

Responding to change over following a plan

That is, while there is value in the items on

the right, we value the items on the left more.

85

Twelve Principles of Agile Software

1. Our highest priority is to satisfy the customer through early and

continuous delivery of valuable software.

2. Welcome changing requirements, even late in development.

Agile processes harness change for the customer's competitive
advantage.

3. Deliver working software frequently, from a couple of weeks to a
couple of months, with a preference to the shorter timescale.

4. Business people and developers must work together daily

throughout the project.

5. Build projects around motivated individuals. Give them the

environment and support they need, and trust them to get the
job done.

86

Twelve Principles of Agile Software

6.

The most efficient and effective method of conveying information
to and within a development team is face-to-face conversation.

7. Working software is the primary measure of progress.

8. Agile processes promote sustainable development.

The sponsors, developers, and users should be able to maintain a
constant pace indefinitely.

9. Continuous attention to technical excellence and good design

enhances agility.

10. Simplicity (the art of maximizing the amount of work not done) is

essential.

11. The best architectures, requirements, and designs emerge from

self-organizing teams.

87

Twelve Principles of Agile Software

12. At regular intervals, the team reflects on how to become more
effective, then tunes and adjusts its behavior accordingly.

Un’importante precisazione (agilemanifesto.org):

● The Agile movement is not anti-methodology, in fact, many of us want to

restore credibility to the word methodology.

● We want to restore a balance. We embrace modeling, but not in order to

file some diagram in a dusty corporate repository.

● We embrace documentation, but not hundreds of pages of never-

maintained and rarely-used tomes.

● We plan, but recognize the limits of planning in a turbulent environment.

88

Marco A. Boschetti
C.d.S. Ingegneria e Scienze Informatiche
marco.boschetti@unibo.it

https://www.unibo.it/sitoweb/marco.boschetti
http://isi-personale.csr.unibo.it/marco.boschetti

