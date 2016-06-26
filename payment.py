from bs4 import BeautifulSoup
import HTML
soup=BeautifulSoup(open("../sortedData.html"),"lxml")

table = soup.find("table")
rows = table.findAll("tr")

payments=["Full Payment","Partial Payment","No Payment"]

dic={}
dic_reverse={}
i=0
for k in payments:
    dic[k]=i
    dic_reverse[i]=k
    i=i+1

def selection(l):
    l.pop()
    return list(l)

payments_data=[[] for i in range(len(payments))]
for tr in rows:
    table_row=[]
    cols=tr.findAll("td")
    if cols:
        for td in cols: table_row.append(td.text)
        table_row.pop() ##removing Volunteer detail
        #table_row=list(table_row[0])+table_row[2:]
        table_row.append(' ')
        k=[]
        k.append(table_row[0])
        table_row=list(k+table_row[2:])
        #print(table_row)

        if int(table_row[4])==0 :
            payments_data[dic["No Payment"]].append(table_row)
        else:
            if int(table_row[6])==0 :
                payments_data[dic["Full Payment"]].append(table_row)
            else:
                payments_data[dic["Partial Payment"]].append(table_row)

for i in range(0,len(payments)):
    k="%s.html" % dic_reverse[i].replace(' ','')
    hfile=open(k,"w")
    hfile.write('<h1>'+dic_reverse[i]+'</h1>'+HTML.table(payments_data[i],header_row=['NuID','Name','Contact Number','Email','Total Fee','Paid','Remaining','Events','Workshops','Tutorials','Present']))
    hfile.close()

    print ""
    print dic_reverse[i],"-",len(payments_data[i])

    money_collected=0
    for x in payments_data[i]:
        money_collected=money_collected+int(x[4])
    print "          ","Collected : ",money_collected

    money_tocome=0
    for x in payments_data[i]:
        money_tocome=money_tocome+int(x[6])
    print "          ","Remaining : ",money_tocome

print ""
print "done",len(payments)
