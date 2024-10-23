class Product():
    def __init__(self, id: str, code: str, price: float, emb: str, link: str, edited: bool, printed: bool) -> None:
        self.__id = id
        self.__code = code
        self.__price = price
        self.__emb = emb
        self.__link = link
        self.__edited = edited
        self.__printed = printed

    def get_id(self):
        return self.__id
    
    def get_code(self):
        return self.__code
    
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
