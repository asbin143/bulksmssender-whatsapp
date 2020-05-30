import webbrowser
import time
import pyautogui as gui
from pandas import read_excel

my_sheet = 'Sheet1' # change it to your sheet name
file_name = 'sheet.xlsx' # change it to the name of your excel file
df = read_excel(file_name, sheet_name = my_sheet)
df['Number'] = '91' + df['Number'].astype(str)
interval = 3
position = 846,195
numbers=df['Number'].values.tolist()
msg ="Bulk sms using python"
for i in numbers:
    url='https://wa.me/{}?text={}'.format(i,msg)
    webbrowser.open(url)
    time.sleep(5)
    gui.click(position)
    time.sleep(5)
    gui.press('enter')
    time.sleep(interval)