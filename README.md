# Validazione e confronto tra semplificazione automatica e semplificazione manuale di testi in italiano istituzionale ai fini dell'efficacia comunicativa
Giuliana Fiorentino, Marco Russodivito, Vittorio Ganfi and Rocco Oliveto


## Abstract
L'articolo presenta i risultati di due studi sperimentali messi a punto per la validazione umana della qualità di testi generati con modelli di IA del tipo GPT. In particolare, i testi da validare sono le versioni semplificate di diverse tipologie di documenti di tipo amministrativo scritte in italiano istituzionale. Per la semplificazione sono stati utilizzati alcuni modelli di IA basati su LLM, e i risultati della semplificazione sono stati misurati ricorrendo agli indici di leggibilità. Una volta accertato che i testi generati automaticamente presentano indici più elevati nella scala della leggibilità, si è deciso di far validare i testi in due esperimenti. Il primo ha coinvolto alcuni giuristi che hanno verificato che il valore giuridico dei testi semplificati fosse salvaguardato. Il secondo ha coinvolto tre categorie di lettori-destinatari (cittadini comuni con diversi livelli di istruzione, stranieri non madrelingua italiani, dipendenti delle pubbliche amministrazioni) per misurare se con i testi semplificati migliora la comprensione da parte dell’utente. I risultati dimostrano che mentre per quanto riguarda la salvaguardia del valore giuridico dei testi la semplificazione non sembra introdurre modifiche che danneggiano particolarmente questo fattore, invece per quanto riguarda l'eventuale incremento della comprensione nei testi semplificati non soltanto questo risultato non viene raggiunto, ma addirittura in qualche caso si osserva che i testi semplificati risultano meno comprensibili dei corrispondenti originali. Questo parametro induce a rivedere la nozione stessa di comprensione e di mettere in discussione gli indici di leggibilità così come concepiti finora ma questo potrà essere oggetto di future ricerche.


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