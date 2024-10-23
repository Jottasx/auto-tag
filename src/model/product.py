class Product():
    def __init__(self, id: str|None, code: str, description: str|None, price: float, emb: str, link: str|None, edited: bool, printed: bool) -> None:
        self.__id = id
        self.__code = code
        self.__descritpion = description
        self.__price = price
        self.__emb = emb
        self.__link = link
        self.__edited = edited
        self.__printed = printed

    def get_id(self):
        return self.__id
    
    def get_code(self):
        return self.__code
    
    def get_descritpion(self):
        return self.__descritpion
    
    def get_price(self):
        return self.__price
    
    def get_emb(self):
        return self.__emb
    
    def get_link(self):
        return self.__link
    
    def is_edited(self):
        return self.__edited
    
    def is_printed(self):
        return self.__printed

    def __str__(self) -> str:
        return f'[ID: {self.get_id()} | Desc: {self.get_descritpion()[:7]} | Code: {self.get_code()} | EMB: {self.get_emb()} | Price: {self.get_price()}]'