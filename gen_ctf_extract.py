#!/bin/python
# -*- coding: utf-8 -*-


from namegen import * 
from random import randint 
import string 
import hashlib

# Count; id; etablissement; lycee; uid; teamname; uid1; nom1; prenom1; email1; ismail1confirmed; uid2; nom2; prenom2; email2; ismail2confirmed; state; flag
# 1; 2; 01 - Annecy; Lycée professionnel privé ECA; 5dfcb5470a82e; Ir0n 4ntr4x; 5dfcb5470a828; a; a; alain.roussel.74@free.fr; 1; 5dfcb5470a82d; b; b; arous@univ-smb.fr; 1; 0; 2
# 1; 3; 04 - Beziers; Lycée général et technologique Jean Moulin; 5dff794aeb98d; Major Bot; 5dff794aeb981; AA; Alice; christopheborelly@gmail.com; 1; 5dff794aeb98c; BB; Bob; j.doe480@laposte.net; 1; 0; 4
# 1; 1; 05 - Blagnac; Lycée général Pierre de Fermat; 5dfcaa259a4b3; Uber Byte; 5dfcaa259a4ab; Bob; Bob; fabrice.peyrard@univ-tlse2.fr; 1; 5dfcaa259a4b2; Alice; Alice; responsablert@gmail.com; 1; 0; 3
# 1; 4; 18 - Mont de Marsan; Lycée général et technologique René Josué Valin; 5e04aac42424c; no_name_yet; 5e04aac424246; RRRRR; RRRRR; r@test.fr; 0; 5e04aac42424b; TTTTT; TTTTT; t@test.fr; 0; 0; 0

etablissement_list = [
'Blagnac',
'Clermont-Ferrand',
'Auxerre',
'Chalons-en-Champagne',
'Caen-Ifs',
'La Reunion',
'Villetaneuse',
'Nancy',
'Lannion',
'La Rochelle',
'Beziers',
'Bethune',
]

count=0;
def gen_id():
    global count
    count=count+1
    id = hashlib.md5(str(count)).hexdigest()
    return id[0:13]
    
    
def gen_entry(count=1,id=0, etablissement='',  lycee=''):
    name = gen_random_name()
    surname = gen_random_surname()
    name2 = gen_random_name()
    surname2 = gen_random_surname()
    mail1confirmed = 1
    if (randint(1, 100)>90):
        mail1confirmed = 0
    mail2confirmed = 1
    if (randint(1, 100)>90):
        mail2confirmed = 0
    flagscount=randint(1, 4)
    teamname="Team_"+str(id)
    if ((mail1confirmed==0) or (mail1confirmed==0)):
        flagscount=int(0);
        teamname='no_name_yet'
        
    print str(count)+"; " \
        + str(id)+"; " \
        + etablissement +"; " \
        + "Lycee de "+etablissement+" "+str(randint(1, 3))+"; " \
        + gen_id()+"; "\
        + teamname+"; " \
        + gen_id()+"; " \
        + name+"; " \
        + surname+"; " \
        + name+"."+surname+"@mail.ctf; " \
        + str(mail1confirmed)+"; " \
        + gen_id()+"; " \
        + name2+"; "\
        + surname2+"; "\
        + name2+"."+surname2+"@mail.ctf; "\
        + str(mail2confirmed)+"; "\
        + "0; " \
        + str(flagscount)+"; " 
 
def my_main():
    id=0
    for etablissement in etablissement_list:
        for i in range(1, 30):
            id=id+1
            gen_entry(i, id, etablissement)
    


        

if __name__ == "__main__":
    my_main()
