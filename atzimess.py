import json
vardnica = {}
ievadit=int(input("Ja vālaties ielādēt no faila json, rakstiet 1, ja ne, rakstiet 2: " ))
if ievadit == 1:
    with open('sample.json', 'r') as openfile:
        vardnica = json.load(openfile)
    for x in vardnica:
        for y in vardnica[x]:
            print("priekšmetā", x,"atzīme ir", y)

dzest=int(input("Ja vēlaties dzēst priekšmetus, rakstiet 3, ja ne, rakstiet 4:" ))
if dzest == 3:
    dzestpieksmet=input("ievadi prieksmetu, kuru gribi dēst")
    if dzestpieksmet in vardnica:
        del vardnica[dzestpieksmet]
    print(vardnica)




pievienot=input("ja vēlaties vēl ievadīt atzīmes, rakstiet yes")
while pievienot == "yes":
    prieksmets=input("ievadi priekšmetu")
    # Pārbaudi vai atzīmju vārdnīcā jau ir šāda atslēga (priekšmets)
    # Ja nav, izveido jaunu masīvu
    # atzimes[prieksmets]=[]
    if prieksmets not in vardnica:
        vardnica[prieksmets]=[]
    atzime=input("ievadi atzīmi")
    # Pārbaudi vai ir diapazonā no 1 - 10, vai nv
    # 0 = nv
    # Un pie izvades -
    # if atzime = 0: print("nv")
    vardnica[prieksmets].append(atzime)
    pievienot=input("ja vēlaties vēl ievadīt atzīmes, rakstiet yes")
'''
atzimes={}
atzimes["prieksmets 1"]=[5,6,7]
prieksmeta_nos = "prieksmets 1"
atzimes[prieksmeta_nos]
print(atzimes[prieksmeta_nos][1])
'''
for x in vardnica:
    for y in vardnica[x]:
        print("priekšmetā", x,"atzīme ir", y)

json_object = json.dumps(vardnica)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

