import xlrd
def work():
    workbook = xlrd.open_workbook('C:/Users/tyza66/Desktop/1.xls')
    worksheet = workbook.sheet_by_index(5)
    for row in range(worksheet.nrows):
        cell_value = worksheet.cell(row, 4).value
        #print(cell_value)
        end = 0
        a = len(cell_value.split('、'))
        b = len(cell_value.split('^'))
        c = len(cell_value.split(','))
        d = len(cell_value.split('，'))
        end = max(a,b,c,d)
        #print(cell_value)
        if(row>=73):
            print(end)

if __name__ == '__main__':
    work()

