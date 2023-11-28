from flask import Flask, request
import en_core_web_md

app = Flask(__name__)

@app.route('/')
def index():
    return 'Text similarity analysis service.'

#Json fields: expected, answer. The values in each field will be analyzed against each other.
@app.route('/analysis', methods=['POST'])
def analysis():
    print("The following statements are being submitted for text analysis: " + request.data.decode('utf-8'))
    percent = evalSimilarity(str(request.json['expected']), str(request.json['answer']))
    return percent



def evalSimilarity(expected,answer):
    nlp = en_core_web_md.load()
    statement1 = nlp(expected)
    statement2 = nlp(answer)

    # Similarity of two statements
    print(statement1, "<->", statement2, statement1.similarity(statement2))

    #Return similarity score
    return str(statement1.similarity(statement2))