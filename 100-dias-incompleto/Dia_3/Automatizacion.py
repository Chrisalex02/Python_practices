import openpyxl

archivo_inventario = openpyxl.load_workbook("Inventario.xlsx")
inventario = archivo_inventario["Desarrollo"]
