import json
from app.enum.local import get_local_name
from app.enum.status import get_status_name

class Product():
    
    def __init__(
            self,
            id: str|None,
            code: str,
            description: str|None,
            price: float,
            emb: str,
            link: str|None,
            edited: bool,
            printed: bool,
            status = get_status_name(1),
            local = get_local_name(1),
        ) -> None:

        self.__id = id
        self.__code = code
        self.__descritpion = description
        self.__price = price
        self.__emb = emb
        self.__link = link
        self.__edited = edited
        self.__printed = printed
        self.__local = local
        self.__status = status

    def get_id(self):
        return self.__id
    
    def set_id(self, id: str):
        self.__id = id
    
    def get_code(self):
        return self.__code
    
    def get_descritpion(self):
        return self.__descritpion
    
    def get_price(self):
        return self.__price
    
    def get_emb(self):
        return self.__emb
    
    def set_product_link(self, link: str):
        self.__link = link
    
    def get_link(self):
        return self.__link
    
    def set_edited(self, edited: bool):
        self.__edited = edited
    
    def is_edited(self):
        return self.__edited
    
    def is_printed(self):
        return self.__printed
    
    def set_printed(self, printed: bool):
        self.is_printed = printed

    def set_local(self, local: int):
        self.__local = local

    def get_local(self):
        return self.__local
    
    def set_status(self, status: int):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)

    def __str__(self) -> str:
        return f'[ID: {self.get_id()} | Desc: {self.get_descritpion()[:7]} | Code: {self.get_code()} | EMB: {self.get_emb()} | Price: {self.get_price()}]'