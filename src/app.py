from model.sheet import Sheet

def main():
    sheet = Sheet("C:\\Users\\lovej\\Downloads\\planilha.xlsx")
    for product in sheet.get_products():
        print(product)
if __name__ == '__main__':
    main()