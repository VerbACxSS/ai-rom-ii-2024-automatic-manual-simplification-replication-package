from xhtml2pdf import pisa
import pandas as pd


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
                height: 10cm;
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
                height: 9cm;
                line-height: 1.2;
                font-size: 11px;
                vertical-align: top;
            }
            
            .t-questions {
                width: 29cm;
                height: 10cm;
            }
            .t-questions th{
                width: 29cm;
                height: 0.5cm;
                text-align: center;
                font-weight: bold;
            }
            .t-questions td.normal {
                width: 29cm;
                height: 0.5cm;
                text-align: center;
            }
            .t-questions td.long {
                width: 29cm;
                height: 2.5cm;
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
                    <th>Q1 - Sono presenti tutte le informazioni essenziali?</td>
                </tr>
                <tr>
                    <td class="normal">{paragraph['q1']}</td>
                </tr>
                <tr>
                    <th>Q2 - Sono presenti parti/informazioni superflue che sono state eliminate?</td>
                </tr>
                <tr>
                    <td class="normal">{paragraph['q2']}</td>
                </tr>
                <tr>
                    <th>Q3 - Sono presenti parole (tecnicismi) con effetto giuridico che sono state cancellate creando problematicità al testo semplificato?</td>
                </tr>
                <tr>
                    <td class="normal">{paragraph['q3']}</td>
                </tr>
                <tr>
                    <th>Q3.1 - in caso affermativo, elencarle:</td>
                </tr>
                <tr>
                    <td class="long">{'' if pd.isna(paragraph['q3_1']) else paragraph['q3_1']}</td>
                </tr>
                <tr>
                    <th>Q4 - Sono stati introdotti errori interpretativi?</td>
                </tr>
                <tr>
                    <td class="normal">{paragraph['q4']}</td>
                </tr>
                <tr>
                    <th>Q5 - Altre considerazioni:</td>
                </tr>
                <tr>
                    <td class="long">{'' if pd.isna(paragraph['q5']) else paragraph['q5']}</td>
                </tr>
            </table>
        </div>
        """
    html += "</body>"
    html += "</html>"
    return html


if __name__ == "__main__":
    data = pd.read_csv('./after_meeting.csv').to_dict('records')
    with open('after_meeting_report.pdf', 'w+b') as f:
        pisa.CreatePDF(html_template(data), dest=f)
