from flask import Blueprint, render_template, request, redirect
from .service.pandas_service import Sheet
from .models import Product
from app import db

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
                _product = Product(
                    code=product.get_code(),
                    description=product.get_descritpion(),
                    price=product.get_price(),
                    emb=product.get_emb(),
                    link=product.get_link(),
                    edited=product.is_edited(),
                    printed=product.is_printed(),
                    local=product.get_local(),
                )
                db.session.add(_product)
                db.session.commit()
            
            return redirect("/")

@main.route('/clear_products', methods=["GET"])                     
def clear_products():
    if Product.query.count() > 0:
        try:
            db.session.query(Product).delete()
            db.session.commit()
        except:
            return "Não foi possível deletar os produtos"
        
        return redirect("/")
    
    return redirect("/")




    

