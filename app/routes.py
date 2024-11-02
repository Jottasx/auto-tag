from flask import Blueprint, render_template, request, jsonify
from app.service.pandas_service import Sheet

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/load-excel', methods=['POST'])
def load_excel():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    sheet = Sheet(file)
    products = sheet.get_products()

    return jsonify({"products": products})