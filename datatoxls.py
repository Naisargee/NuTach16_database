from bs4 import BeautifulSoup
import HTML
soup=BeautifulSoup(open("data.html"),"lxml")

table = soup.find("table")
rows = table.findAll("tr")

import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('a test sheet')



table_data=[]
for tr in rows:
	table_row=[]
	cols=tr.findAll("td")
	if cols:
		for td in cols:
			table_row.append(td.text)
		#	y=y+1
		#x=x+1
		table_data.append(table_row)

from operator import itemgetter
table_data.sort(key=lambda x: x[1])

x=0
for i in range(0,len(table_data)):
	table_data[i]=["NU"+"%03d"%(i+1)]+table_data[i]
	y=1
	for k in table_data[i]:
		ws.write(x,y,k)
		y=y+1
	x=x+1

wb.save('BlastResults.xls')

htmlcode = HTML.table(table_data,header_row=['NuID','RegID','Name','Contact Number','Email','Total Fee','Paid','Remaining','Events','Workshops','Tutorials','Volunteer'])
print htmlcode
