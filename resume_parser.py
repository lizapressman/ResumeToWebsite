from pyresparser import ResumeParser
from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
@cross_origin()
def parse():
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(filename)
    data = ResumeParser(filename).get_extracted_data()
    return data


@app.route('/create', methods=['POST'])
def create():
    content = request.json
    message = """<html>\n<head></head>\n<body>\n"""
    for key in content:
        message += f"""<p>{key}: {content.get(key)}</p>\n"""
    message += """</body>\n</html>"""
    return message
