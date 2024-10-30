import customtkinter
from PIL import Image
from src.UI.table import Table
from src.UI.console import Console 
from src.model.product import Product
from src.model.sheet import Sheet
from tkinter import filedialog, messagebox
from typing import List

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")

        # Configurações da janela
        self.geometry("1000x877")
        self.title("Auto Tag")
        self.resizable(False, False)

        # Widgets -----------------------------------------------------------
        # "Logo"
        self.h1_title = customtkinter.CTkLabel(
                self,
                text="AUTO TAG",
                font=("Inter", 26, "bold"),
                fg_color="transparent",
                text_color="#000",
                width=36,
            )
        self.h1_title.grid(row=0, column=0, padx=(50, 0), pady=(30, 0), sticky="nw")

        # Tabela de produtos
        # Título da tabela
        self.table_title = customtkinter.CTkLabel(
            self,
            text="Lista de produtos:",
            font=("Inter", 14, "bold"),
            fg_color="transparent",
            text_color="#000"
        )
        self.table_title.grid(row=1, column=0, padx=(50, 0), pady=(50, 0), sticky="w")

        # Tabela
        self.table = Table(master=self, products=[], width=650, height=450, corner_radius=0, fg_color="#DDD")
        self.table.grid(row=3, column=0, padx=(50, 0), pady=(1, 1), sticky="nsew")


        # Botões lado direito -----------------------------------------------------------
        img_excel = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/excel_icon.png"),
            size=(29, 29)
        )

        # Produtos
        self.btn_products_upper_text = customtkinter.CTkLabel(
            self,
            text="Carregar produtos",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_products_upper_text.grid(row=3, column=2, padx=(80, 0), pady=(75, 1), sticky="ne")

        self.btn_products = customtkinter.CTkButton(
            self,
            text="Produtos",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_excel,
            width=140,
            height=45,
            corner_radius=0,
            command=self.load_products
        )
        self.btn_products.grid(row=3, column=2, padx=(80, 0), pady=(100, 1), sticky="ne")


        # SASOI006
        img_sasoi006 = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/sasoi006_icon.png"),
            size=(26, 26)
        )

        self.btn_sasoi006_upper_text = customtkinter.CTkLabel(
            self,
            text="Enviar para SASOI006",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_sasoi006_upper_text.grid(row=3, column=2, padx=(80, 0), pady=(150, 1), sticky="ne")

        self.btn_sasoi006 = customtkinter.CTkButton(
            self,
            text="SASOI006",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_sasoi006,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_sasoi006.grid(row=3, column=2, padx=(80, 0), pady=(175, 1), sticky="ne")



        # TAGSELL
        img_tagsell = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/tagsell_icon.png"),
            size=(27, 27)
        )

        self.btn_tagsell_upper_text = customtkinter.CTkLabel(
            self,
            text="Enviar para o TagSell",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_tagsell_upper_text.grid(row=3, column=2, padx=(80, 0), pady=(225, 1), sticky="ne")

        self.btn_tagsell = customtkinter.CTkButton(
            self,
            text="TAGSELL",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_tagsell,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_tagsell.grid(row=3, column=2, padx=(80, 0), pady=(250, 1), sticky="ne")


        # Botões de baixo -----------------------------------------------------------------------
        # Preço
        img_price = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/price_icon.png"),
            size=(24, 24)
        )

        self.btn_price_upper_text = customtkinter.CTkLabel(
            self,
            text="Alterar os preços",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_price_upper_text.grid(row=4, column=0, padx=(50, 0), pady=(0, 0), sticky="nw")

        self.btn_price = customtkinter.CTkButton(
            self,
            text="PREÇO",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_price,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_price.grid(row=4, column=0, padx=(50, 0), pady=(25, 0), sticky="w")

        # Imprimir
        img_print = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/pdf_icon.png"),
            size=(24, 24)
        )

        self.btn_print_upper_text = customtkinter.CTkLabel(
            self,
            text="Salvar em PDF",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_print_upper_text.grid(row=4, column=0, padx=(205, 0), pady=(0, 0), sticky="nw")

        self.btn_print = customtkinter.CTkButton(
            self,
            text="IMPRIMIR",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_print,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_print.grid(row=4, column=0, padx=(205, 0), pady=(25, 0), sticky="nw")

        # Limpar
        img_clear = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/clear_icon.png"),
            size=(24, 24)
        )

        self.btn_clear_upper_text = customtkinter.CTkLabel(
            self,
            text="Limpar a lista",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_clear_upper_text.grid(row=4, column=0, padx=(0, 73), pady=(0, 0), sticky="ne")

        self.btn_clear = customtkinter.CTkButton(
            self,
            text="LIMPAR",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_clear,
            command=self.clear_products,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_clear.grid(row=4, column=0, padx=(0, 0), pady=(25, 0), sticky="ne")


        # Console --------------------------------------------------------------------
        self.console_upper_text = customtkinter.CTkLabel(
            self,
            text="LOG do sistema:",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.console_upper_text.grid(row=5, column=0, padx=(50, 0), pady=(20, 0), sticky="nw")
        
        self.console = Console(self, corner_radius=0, height=120, fg_color="#DDD")
        self.console.grid(row=6, column=0, padx=(50, 0), pady=(0, 0), columnspan=12, sticky="we")


        # Créditos
        self.credits = customtkinter.CTkLabel(
            self,
            text="Desenvolvido por João Pedro Mesquita | j.pedro.mesquita.cst@gmail.com",
            text_color="#000",
            font=("Inter", 10, "bold")
        )
        self.credits.grid(row=7, column=0, padx=(50, 0), pady=(20, 0), sticky="nse")
        
    def update_table(self, produtcs: List[Product]):
        if len(produtcs) > 0:
            self.table = Table(self,  produtcs)
            self.table.grid(row=3, column=0, padx=(50, 0), pady=(1, 1), sticky="nsew")

    def load_products(self):
        file_path = filedialog.askopenfilename(title="Carregue a planilha com os produtos")
        
        if file_path:
            sheet = Sheet(file_path)
            self.show_dialog_box("Produtos importados com sucesso!")
            self.update_table(sheet.get_products())
            return
            
        self.show_dialog_box("Nenhum arquivo foi selecionado.")

    def clear_products(self):
        self.table = Table(self, products=[])
        self.table.grid(row=3, column=0, padx=(50, 0), pady=(1, 1), sticky="nsew")
        

    def show_dialog_box(self, txt):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Importação de produtos")
        dialog.geometry("300x150")

        # Esse código centraliza a dialog no meio da janela principal
        main_x = self.winfo_x()
        main_y = self.winfo_y()
        main_width = 1000
        main_height = 877
        dialog_width = 300
        dialog_height = 150

        pos_x = main_x + (main_width - dialog_width) // 2
        pos_y = main_y + (main_height - dialog_height) // 2
        dialog.geometry(f"{dialog_width}x{dialog_height}+{pos_x}+{pos_y}")

        # Deixa a dialog em foco
        dialog.grab_set()        

        # Mensagem da dialog box
        label = customtkinter.CTkLabel(
            dialog,
            text=txt,
            font=("Arial", 14)
        )
        label.pack(pady=10)
            
        # Botão para fechar a dialog box
        close_button = customtkinter.CTkButton(dialog, text="OK", command=dialog.destroy)
        close_button.pack(pady=10)