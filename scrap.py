import pandas as pd
import xlsxwriter
import random
import string

name = 'email'
df = pd.read_excel(name+'.xlsx')

username = df['Username'].values.tolist()
Email = df['Email'].values.tolist()
Password = df['Password'].values.tolist()
count = 0
res = []
for item in range(len(username)):
    url = (username[count] + '.page.tl')
    count = count + 1
    res.append(url)
    
letters = string.ascii_lowercase
rand = ( ''.join(random.choice(letters) for i in range(5)) )

workbook = xlsxwriter.Workbook(name+rand+'Output.xlsx')
sheet = workbook.add_worksheet()

sheet.write("A1", "Email")
sheet.write("B1", "Username")
sheet.write("C1", "URL")

for item in range(len(Email)):
    sheet.write(item+1, 0, Email[item])
    sheet.write(item+1, 1, username[item])
    sheet.write(item+1, 2, res[item])
    

workbook.close()