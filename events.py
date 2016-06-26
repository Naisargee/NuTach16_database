from bs4 import BeautifulSoup
import HTML
soup=BeautifulSoup(open("../sortedData.html"),"lxml")

table = soup.find("table")
rows = table.findAll("tr")

events=["Cham E Car","Chemology","Industrial Experience","Chemical Housie","Electro Vyapar","E Placement","Tech Treasurehunt","Audio Visual Quiz","Vyapaar","ROCKETSINGH","B-Rodies","Maad-Mad About Ad","Twist And Turn","Friends-O-Mania","Void FNX","LAN Gaming","Hackathon","Bugs Bunny","Code-De-Pirates","Read and decipher","Think You're Ready?","InfoManiacs","Water Rocket","HydroArm","Aeromobile Quiz","Mock CID","Quiz-O-Dare","Block-Tackle(JAM)","Bag","Best From Waste","NU-Lens(Online)","Crackduino","Make in EC","Digimania","AnalogSim","Paper Presentation-EC","Death Race","Shotput","Robominton","Hell in Cell","Line Follower Rac","Robot Soccer","Junkyard Electronics","Diji-Tronics","E-mania","Civilion hunt","Plan De Nirma","Frame The Helipad","Civil geek","Poster Presentation - Digitalization In Civil","India Quiz","Debate","Scavenger Hunt","Spell Bee","Gully Cricket/BasketBall","Paper Pesentation","Project Presentation","Poster Presentation"]

dic={}
dic_reverse={}
i=0
for k in events:
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

events_data=[[] for i in range(len(events))]
for tr in rows:
    table_row=[]
    cols=tr.findAll("td")
    if cols:
        for td in cols: table_row.append(td.text)
        table_row[8]=table_row[8].split(",")
        for i in table_row[8]:
            i=i.strip()
            if i in dic:
                k=dic[i]
                selected_row=selection(list(table_row))
                selected_row=[len(events_data[k])+1]+selected_row
                events_data[k].append(selected_row)

for i in range(0,len(events)):
    k="%s.html" % dic_reverse[i].replace(' ','')
    k=k.replace('/','')
    hfile=open(k,"w")
    hfile.write('<h1>'+dic_reverse[i]+'</h1>'+HTML.table(events_data[i],header_row=['No','NuID','Name','Contact Number','Email','Present']))
    hfile.close()
    print dic_reverse[i],"-",len(events_data[i])
print ""
print "done",len(events)
