import pandas as pd
from typing import List
from src.model.product import Product

class Sheet():

    def __init__(self, path: str) -> None:
        try:
            self.__df = pd.read_excel(path, dtype={'preço': float})
        except FileNotFoundError as Error:
            print(f'[Erro] A planilha não foi encontrada no caminho "{path}", verifique se o caminho está correto.')
       
    def get_products(self) -> List[Product]:
        products = []
        for row in self.__df.iterrows():
            # Ignora células onde a descrição está vazia (sem estoque na planilha)
            if type(row['desc']) != str:
                continue

            products.append(
                Product(
                    id=None,
                    code=row['cod'],
                    description=row['desc'],
                    price=row['preço'],
                    emb=row['embb'],
                    link=None,
                    edited=False,
                    printed=False,
                    local=1,
                    status=1
                )
            )

        return products
