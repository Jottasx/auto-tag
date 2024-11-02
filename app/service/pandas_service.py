import pandas as pd
from typing import List
from app.model.product import Product

class Sheet():

    def __init__(self, io) -> None:
        try:
            self.__df = pd.read_excel(io, dtype={'preço': float})
        except FileNotFoundError as Error:
            print(f'[Erro] A planilha não foi encontrada no caminho "{io}", verifique se o caminho está correto.')
       
    def get_products(self) -> List[Product]:
        products = []
        seriazable = []
        for row in self.__df.iterrows():
            # Ignora células onde a descrição está vazia (sem estoque na planilha)
            if type(row[1]['desc']) != str:
                continue

            products.append(
                Product(
                    id=None,
                    code=row[1]['cod'],
                    description=row[1]['desc'],
                    price=row[1]['preço'],
                    emb=row[1]['embb'],
                    link=None,
                    edited=False,
                    printed=False,
                )
            )

        for product in products:
            seriazable.append(product.toJSON())

        return seriazable
