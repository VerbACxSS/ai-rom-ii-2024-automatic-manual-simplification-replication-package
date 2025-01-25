from xhtml2pdf import pisa
import pandas as pd


def class_for_check(r1, r2, r3):
    if r1 == r2 == r3:
        return 'a'
    return 'a-to-check'


def html_template(paragraphs):
    html = """
    <html>
    <head>
        <title>PDF</title>
        <style>
            @page {
                size: a4 landscape;
                margin-left: 0.35cm;
                margin-right: 0.35cm;
                margin-top: 0.25cm;
                margin-bottom: 0.25cm;
            }
            .page-content {
                width: 29cm;
                height: 21cm;
            }
            h1 {
                width: 29cm;
                height: 0.5cm;
                line-height: 1;
                font-size: 12px;
                text-align: center;
            }
            
            td, th {
                margin: 0;
                border: 0;
                padding-top: 0;
                padding-bottom: 0;
                padding-left: 0.15cm;
                padding-right: 0.15cm;
            }
            tr {
                margin: 0;
                border: 0;
                padding: 0;
            }
            
            .t-texts {
                width: 29cm;
                height: 9cm;
            }
            .t-texts .text-th {
                text-align: center;
                width: 14.5cm;
                height: 0.5cm;
                line-height: 1;
                font-size: 11px;
                vertical-align: middle;
            }
            .t-texts .text-td {
                text-align: justify;
                width: 14.5cm;
                height: 8.5cm;
                line-height: 1.2;
                font-size: 11px;
                vertical-align: top;
            }
            
            .t-questions {
                width: 29cm;
                height: 11cm;
            }
            .t-questions .n {
                width: 7.25cm;
                height: 0.5cm;
                text-align: center;
                font-weight: bold;
            }
            .t-questions .q {
                width: 7.25cm;
                height: 1cm;
                text-align: left;
                font-weight: bold;
            }
            .t-questions .a {
                width: 7.25cm;
                height: 1cm;
                text-align: center;
            }
            .t-questions .a-to-check {
                width: 7.25cm;
                height: 1cm;
                text-align: center;
                color: red;
            }
            .t-questions .a-full {
                width: 7.25cm;
                height: 3cm;
                text-align: center;
            }
        </style>
    </head>
    """

    html += "<body>"

    for paragraph in paragraphs:
        paragraph['original_text'] = paragraph['original_text'].replace('\n', '<br>')
        paragraph['simplified_text'] = paragraph['simplified_text'].replace('\n', '<br>')
        html += f"""
        <div class="page-content">
            <h1>Paragrafo {paragraph['paragraph_index']}</h1>
            <table class="t-texts">
                <tr>
                    <th class="text-th">Originale</th>
                    <th class="text-th">Semplificato</th>
                </tr>
                <tr>
                    <td class="text-td">{paragraph['original_text']}</td>
                    <td class="text-td">{paragraph['simplified_text']}</td>
                </tr>
            </table>
            
            <table class="t-questions">
                <tr>
                    <td class="n">Domanda</td>
                    <td class="n">Reviewer 1 ({paragraph['r1']['time']}s)</td>
                    <td class="n">Reviewer 2 ({paragraph['r2']['time']}s)</td>
                    <th class="n">Reviewer 3 ({paragraph['r3']['time']}s)</td>
                </tr>
                <tr>
                    <td class="q">Q1 - Sono presenti tutte le informazioni essenziali?<?td>
                    <td class="{class_for_check(paragraph['r1']['q1'], paragraph['r2']['q1'], paragraph['r3']['q1'])}">{paragraph['r1']['q1']}</td>
                    <td class="{class_for_check(paragraph['r1']['q1'], paragraph['r2']['q1'], paragraph['r3']['q1'])}">{paragraph['r2']['q1']}</td>
                    <td class="{class_for_check(paragraph['r1']['q1'], paragraph['r2']['q1'], paragraph['r3']['q1'])}">{paragraph['r3']['q1']}</td>
                </tr>
                <tr>
                    <td class="q">Q2 - Sono presenti parti/informazioni superflue che sono state eliminate?</td>
                    <td class="{class_for_check(paragraph['r1']['q2'], paragraph['r2']['q2'], paragraph['r3']['q2'])}">{paragraph['r1']['q2']}</td>
                    <td class="{class_for_check(paragraph['r1']['q2'], paragraph['r2']['q2'], paragraph['r3']['q2'])}">{paragraph['r2']['q2']}</td>
                    <td class="{class_for_check(paragraph['r1']['q2'], paragraph['r2']['q2'], paragraph['r3']['q2'])}">{paragraph['r3']['q2']}</td>
                </tr>
                <tr>
                    <td class="q">Q3 - Sono presenti parole (tecnicismi) con effetto giuridico che sono state cancellate creando problematicità al testo semplificato?</th>
                    <td class="{class_for_check(paragraph['r1']['q3'], paragraph['r2']['q3'], paragraph['r3']['q3'])}">{paragraph['r1']['q3']}</td>
                    <td class="{class_for_check(paragraph['r1']['q3'], paragraph['r2']['q3'], paragraph['r3']['q3'])}">{paragraph['r2']['q3']}</td>
                    <td class="{class_for_check(paragraph['r1']['q3'], paragraph['r2']['q3'], paragraph['r3']['q3'])}">{paragraph['r3']['q3']}</td>
                </tr>
                <tr class=r-full>
                    <td class="q">Q3.1 - in caso affermativo, elencarle:</th>
                    <td class="a-full">{paragraph['r1']['q3_1']}</td>
                    <td class="a-full">{paragraph['r2']['q3_1']}</td>
                    <td class="a-full">{paragraph['r3']['q3_1']}</td>
                </tr>
                <tr>
                    <td class="q">Q4 - Sono stati introdotti errori interpretativi?</th>
                    <td class="{class_for_check(paragraph['r1']['q4'], paragraph['r2']['q4'], paragraph['r3']['q4'])}">{paragraph['r1']['q4']}</td>
                    <td class="{class_for_check(paragraph['r1']['q4'], paragraph['r2']['q4'], paragraph['r3']['q4'])}">{paragraph['r2']['q4']}</td>
                    <td class="{class_for_check(paragraph['r1']['q4'], paragraph['r2']['q4'], paragraph['r3']['q4'])}">{paragraph['r3']['q4']}</td>
                </tr>
                <tr class=r-full>
                    <td class="q">Q5 - Altre considerazioni:</td>
                    <td class="a-full">{paragraph['r1']['q5']}</td>
                    <td class="a-full">{paragraph['r2']['q5']}</td>
                    <td class="a-full">{paragraph['r3']['q5']}</td>
                </tr>
            </table>
        </div>
        """
    html += "</body>"
    html += "</html>"
    return html


if __name__ == "__main__":
    df1 = pd.read_csv('./before_meeting_reviewer1.csv').to_dict('records')
    df2 = pd.read_csv('./before_meeting_reviewer2.csv').to_dict('records')
    df3 = pd.read_csv('./before_meeting_reviewer3.csv').to_dict('records')

    data = []
    for paragraph_1, paragraph_2, paragraph_3 in zip(df1, df2, df3):
        data.append({
            'paragraph_index': paragraph_1['paragraph_index'],
            'original_text': paragraph_1['original_text'],
            'simplified_text': paragraph_1['simplified_text'],
            'r1': {
                'q1': paragraph_1['q1'],
                'q2': paragraph_1['q2'],
                'q3': paragraph_1['q3'],
                'q3_1': paragraph_1['q3_1'] if not pd.isna(paragraph_1['q3_1']) else '',
                'q4': paragraph_1['q4'],
                'q5': paragraph_1['q5'] if not pd.isna(paragraph_1['q5']) else '',
                'time': paragraph_1['review_elapsed_time']
            },
            'r2': {
                'q1': paragraph_2['q1'],
                'q2': paragraph_2['q2'],
                'q3': paragraph_2['q3'],
                'q3_1': paragraph_2['q3_1'] if not pd.isna(paragraph_2['q3_1']) else '',
                'q4': paragraph_2['q4'],
                'q5': paragraph_2['q5'] if not pd.isna(paragraph_2['q5']) else '',
                'time': paragraph_2['review_elapsed_time']
            },
            'r3': {
                'q1': paragraph_3['q1'],
                'q2': paragraph_3['q2'],
                'q3': paragraph_3['q3'],
                'q3_1': paragraph_3['q3_1'] if not pd.isna(paragraph_3['q3_1']) else '',
                'q4': paragraph_3['q4'],
                'q5': paragraph_3['q5'] if not pd.isna(paragraph_3['q5']) else '',
                'time': paragraph_3['review_elapsed_time']
            }
        })

    with open('./before_meeting_report.pdf', 'w+b') as f:
        pisa.CreatePDF(html_template(data), dest=f)
