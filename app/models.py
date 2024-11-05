import json
from . import db 
from app.enum.local import get_local_name

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    emb = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(300), nullable=True)
    edited = db.Column(db.Integer, nullable=False)
    printed = db.Column(db.Integer, nullable=False)
    local = db.Column(db.String(20), nullable=False)

    def get_id(self):
        return self.id
    
    def set_id(self, id: str):
        self.id = id
    
    def get_code(self):
        return self.code
    
    def get_descritpion(self):
        return self.descritpion
    
    def get_price(self):
        return self.price
    
    def get_emb(self):
        return self.emb
    
    def set_product_link(self, link: str):
        self.link = link
    
    def get_link(self):
        return self.link
    
    def set_edited(self, edited: bool):
        self.edited = edited
    
    def is_edited(self):
        return self.edited
    
    def is_printed(self):
        return self.printed
    
    def set_printed(self, printed: bool):
        self.is_printed = printed

    def set_local(self, local: int):
        self.local = get_local_name(local)

    def get_local(self):
        return self.local
    
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)

    def __str__(self) -> str:
        return f'[ID: {self.get_id()} | Desc: {self.get_descritpion()[:7]} | Code: {self.get_code()} | EMB: {self.get_emb()} | Price: {self.get_price()}]'