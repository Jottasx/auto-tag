import pandas as pd
from pandas import DataFrame
from typing import List
from model.product import Product

class Sheet():

    df: DataFrame = None

    def __init__(self, path: str) -> None:
        try:
            self.df = pd.read_excel(path, dtype={'preço': float})
        except FileNotFoundError as Error:
            print(f'[Erro] A planilha não foi encontrada no caminho "{path}", verifique se o caminho está correto.')
       

    def get_products(self) -> List[Product]:
        products = []
        for i, row in self.df.iterrows():
            products.append(
                Product(
                    id=None,
                    code=row['cod'],
                    description=row['desc'],
                    price=row['preço'],
                    emb=row['embb'],
                    link=None,
                    edited=False,
                    printed=False
                )
            )

        return products
