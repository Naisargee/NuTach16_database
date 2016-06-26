from bs4 import BeautifulSoup
import HTML
soup=BeautifulSoup(open("../sortedData.html"),"lxml")

table = soup.find("table")
rows = table.findAll("tr")

workshops=["Internet Of Things","Android 6.0 Development","Website Design using Google Blogger","Hands-on with Arduino","Auto Extravaganze","Creo workshop","Workshop on entrepreneurship","Design And Analysis of 3-Storey Building","Sophisticated Analytical Instruments","Application of MATLAB in Electrical Engg.","Advanced Photography with 360 degree Techniques"]

dic={}
dic_reverse={}
i=0
for k in workshops:
    dic[k]=i
    dic_reverse[i]=k
    i=i+1

def selection(l):
    ln=[]
    ln.append(l[0])
    ln.append(l[2])
    ln.append(l[3])
    ln.append(l[4])
    ln.append(' ')
    return list(ln)

workshops_data=[[] for i in range(len(workshops))]
for tr in rows:
    table_row=[]
    cols=tr.findAll("td")
    if cols:
        for td in cols: table_row.append(td.text)
        table_row[9]=table_row[9].split(",")
        for i in table_row[9]:
            i=i.strip()
            if i in dic:
                k=dic[i]
                selected_row=selection(list(table_row))
                selected_row=[len(workshops_data[k])+1]+selected_row
                workshops_data[k].append(selected_row)

for i in range(0,len(workshops)):
    k="%s.html" % dic_reverse[i].replace(' ','')
    k=k.replace('/','')
    hfile=open(k,"w")
    hfile.write('<h1>'+dic_reverse[i]+'</h1>'+HTML.table(workshops_data[i],header_row=['No','NuID','Name','Contact Number','Email','Present']))
    hfile.close()
    print dic_reverse[i],"-",len(workshops_data[i])
print ""
print "done",len(workshops)
