# Validazione e confronto tra semplificazione automatica e semplificazione manuale di testi in italiano istituzionale ai fini dell'efficacia comunicativa
Giuliana Fiorentino, Marco Russodivito, Vittorio Ganfi and Rocco Oliveto

## Abstract
In questo contributo gli autori sviluppano una ulteriore fase di un progetto che va avanti da circa un anno e mezzo. Obiettivo finale del progetto è costruire - con un modello di intelligenza artificiale ispirato a chat GPT - un ATS (denominato SEMPLIT, applicativo risultante dal progetto PRIN VerbAcxSS) addestrato su un corpus di testi raccolto all'interno del progetto (denominato ItaIst), per semplificare testi di italiano istituzionale al fine di mettere a disposizione della Pubblica Amministrazione e degli utenti finali, i cittadini, uno strumento di lavoro facile da usare (in open access).

Gli autori – dopo aver semplificato automaticamente l'intero corpus ItaIst, valutando il risultato rispetto al testo di origine – hanno aperto una seconda fase di lavoro in cui è stata semplificata manualmente una porzione del corpus ItaIst. Questa seconda fase di lavoro ha permesso a) di confrontare e valutare quantitativamente il modo di semplificare del modello di intelligenza artificiale con la semplificazione manuale utilizzando diverse formule di semplificazione come Gulpease Index, Flesch Reading Ease; Flesch Kincaid Grade, Automated Readability oltre che considerando l'incremento del Vocabolario di Base (sui parametri e criteri da usare nella semplificazione di testi giuridici si vedano anche Brunato, Venturi 2014; Dell'Orletta et alii 2011); b) di studiare le diverse regole di semplificazione applicate spontaneamente dal software confrontandole con quelle applicate da due studiosi; c) di valutare che anche nella semplificazione manuale si possono applicare regole di semplificazione in modo non omogeneo (differenze tra i due revisori umani); d) di raggruppare e descrivere regole di semplificazione anche diverse da quelle normalmente suggerite dalla manualistica italiana corrente (Cortelazzo et alii 199; Cortelazzo, 2021). A questo proposito gli obiettivi che ci proponiamo sono i) valutare il diverso peso che parametri quantitativi (ad esempio lunghezza delle frasi o delle parole) e parametri qualitativi (ad esempio il soggetto esplicito preferibilmente animato) hanno nel raggiungere l'efficacia comunicativa ed inoltre ii) integrare maggiormente il ricorso a parametri qualitativi nel nostro applicativo (SEMPL-IT).

Presenteremo dunque i risultati di una terza fase del lavoro che consiste in test di valutazione da somministrare a due campioni di utenti di madrelingua italiana. Infatti a partire da 4 insiemi di testi paralleli che sono: 1. testi amministrativi originali; 2. testi semplificati dal modello di intelligenza artificiale; 3. testi semplificati manualmente da un revisore 4. testi semplificati manualmente da un secondo revisore; si sono costruiti due test. Il primo consiste nel far valutare a un campione di utenti la qualità della semplificazione (campione di esperti, linguisti, studenti universitari); il secondo consiste nel valutare il diverso impatto dei 4 testi paralleli mediante domande di comprensione che consentiranno di verificare l'efficacia dei metodi di semplificazione utilizzati nelle 3 tipologie di testi.

L'articolo discuterà criticamente i risultati dei due test.

## Setup
Create a virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

## Replication Package Content
* `juridical_review`: folder that contains data and code of the juridical-review experiment.
  * `before_meeting_reviewer1.csv`, `before_meeting_reviewer2.csv` and `before_meeting_reviewer3.csv`: juridical-review data before conflict solver meeting.
  * `before_meeting_analysis.ipynb`: jupyter notebook used to analyze juridical-review data before conflict solver meeting.
  * `before_meeting_report.py`: script to create `before_meeting_report.pdf`.
  * `before_meeting_report.pdf`: human-readable report in `.pdf` format.
  * `after_meeting.csv`: juridical-review data after conflict solver meeting.
  * `after_meeting_analysis.ipynb`: jupyter notebook used to analyze the juridical-review data after conflict solver meeting.
  * `after_meeting_report.py`: script to create `after_meeting_report.pdf`.
  * `after_meeting_report.pdf`: human-readable report in `.pdf` format.
* `compension_survey_pilot_study`: folder that contains data and code of the compension-survey pilot study.
  * `raw_data`: folder that contains the compension-survey pilot study raw data in `.csv` format.
  * `post_survey.xlsx`: post-survey structured interview report.
  * `analysis.ipynb`: jupyter notebook used to analyze the compension-survey results.
  * `visualize.ipynb`: jupyter notebook used to visualize all the events produced by the participants.
* `compension_survey`: folder that contains data and code of the compension-survey experiment.
  * `docs`: folder that contains documents and question of the compension-survey.
  * `raw_data`: folder that contains the compension-survey raw data in `.csv` format.
  * `final_data`: folder that contains the compension-survey processed data in `.csv` and `.xlsx` formats.
  * `0_docs_analysis.ipynb`: jupyter notebook used to evaluate the documents of the compension-survey. It employs [italian-ats-evaluator](https://github.com/RedHitMark/italian-ats-evaluator).
  * `1_data_processor.ipynb`: jupyter notebook used to process the files in `raw_data` folder.
  * `2_demographics_analysis.ipynb`: jupyter notebook used to analyze demographics info of the participants.
  * `3_explorative_analysis.ipynb`: jupyter notebook used to analyze the compension-survey results.
  * `4_statistical_analysis.ipynb`: jupyter notebook used to perform statistical analyis on the compension-survey results.
  * `5_visualize_participant.ipynb`: jupyter notebook used to visualize all the events produced by a single participant.

## Acknowledgements
This contribution is a result of the research conducted within the framework of the PRIN 2020 (Progetti di Rilevante Interesse Nazionale) "VerbACxSS: on analytic verbs, complexity, synthetic verbs, and simplification. For accessibility" (Prot. 2020BJKB9M), funded by the Italian Ministero dell'Università e della Ricerca.