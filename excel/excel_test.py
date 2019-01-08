from openpyxl import load_workbook
# 默认可读写，若有需要可以指定write_only和read_only为True
wb = load_workbook('C:\\Users\\27351\\Desktop\\sdma\\合同明细_20181211053606.xlsx')

print(wb.get_sheet_names)