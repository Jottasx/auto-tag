from flask import Blueprint, render_template, request, redirect, jsonify
from .service.pandas_service import Sheet
from .service.sasoi006_service import Sasoi006
from .service.selenium_service import Browser
from .service.tagsell_service import TagSell
from .models import Product
from app import db
import datetime

main = Blueprint("main", __name__)

@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        products = Product.query.all()

        return render_template('index.html', products=products)
    
    if request.method == "POST":
        excel_file = request.files["file"]

        if excel_file:
            sheet = Sheet(excel_file)
            products = sheet.get_products()

            for product in products:
                db.session.add(product)
                
            db.session.commit()    
            
            return jsonify({"msg": "ok"})
        
        return jsonify({"Erro": "Erro"})

@main.route('/clear_products', methods=["GET"])                     
def clear_products():
    if Product.query.count() > 0:
        try:
            db.session.query(Product).delete()
            db.session.commit()
        except:
            return jsonify({"Erro": "Não foi possível deletar os produtos"})        
        return redirect("/")
    
    return redirect("/")

@main.route('/call_sasoi006', methods=["POST"])
def send_to_sasoi006():
    data = request.get_json()
    product_codes = []
    
    if data is None:
        return jsonify({"Erro": "Dados recebidos invalidos"})

    for item in data.get("checked_products"):
        product_codes.append(item.get("product_code"))

    if len(product_codes) > 0:
        browser = Browser("./driver/chromedriver.exe")
        sasoi006 = Sasoi006(browser)

        user_data = data.get("user_data")

        if user_data.get("login") and user_data.get("password") and user_data.get("filial"):
            login = user_data.get("login")
            password = user_data.get("password")
            filial = user_data.get("filial")
            if not sasoi006.login(login=login, password=password, branch=filial):
                return jsonify({"msg": "Credenciais Inválidas"})

            # Fazer query no banco pelos produtos e comparar com a lista de checados, os que tiverem checados precisam ser enviados para a sasoi006
            
            prodructs_from_db = Product.query.all()
            products = list(filter(lambda x: x.code in product_codes, prodructs_from_db))

            sended_products = sasoi006.fill_products(products)

            if len(sended_products) > 0:
                for code in sended_products:
                    product = Product.query.filter_by(code = code).first()
                    product.set_local(2)
                    db.session.commit()

            return jsonify({"Mensagem": "Produtos enviados a SASOI006"})

    return jsonify({"Mensagem": "Erro ao processar"})

@main.route('/call_tagsell', methods=["POST"])
def send_to_tagsell():
    data = request.get_json()

    if data:
        user_data = data.get("user_data")
        checked_products = data.get("checked_products")
        products = []

        login = user_data.get("login")
        password = user_data.get("password")

        # Procura no banco de dados os produtos que estão marcados na tabela
        for code in checked_products:
            products.append(Product.query.filter_by(code = code['product_code']).first())

        browser = Browser("./driver/chromedriver.exe")
        tagsell = TagSell(browser)

        tagsell.login(login, password)
        tagsell.handle_sketch(products)
        # rascunho

        return jsonify({"Data": products})

    return jsonify({"Data": "ok"})