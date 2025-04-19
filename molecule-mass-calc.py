# -*- coding: utf-8 -*-
# v1.1.2
print('LAPADKA(R) MolecularMass calculator\n')
formula=input('enter formula:')

UpperCase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numbers=['1','2','3','4','5','6','7','8','9','0']

CalcList=formula[0]
for tree in range(len(formula)-1):
    if UpperCase.count(formula[tree+1])>0:
        CalcList+=' '+formula[tree+1]
    else:
        CalcList+=formula[tree+1]
CL=CalcList.split(' ')

MolecularMassChart={'H':1.008,'He':4.002602,'Li':6.94,'Be':9.0121831,'B':10.81,'C':12.011,'N':14.007,'O':15.999,'F':18.998403163,
                    'Ne':20.1797,'Na':22.98976928,'Mg':24.305,'Al':26.9815385,'Si':28.085,'P':30.973761998,'S':32.06,'Cl':35.45,
                    'Ar':39.948,'K':39.0983,'Ca':40.078,'Sc':44.955908,'Ti':47.867,'V':50.9415,'Cr':51.9961,'Mn':54.938044,
                    'Fe':55.845,'Co':58.933194,'Ni':58.6934,'Cu':63.546,'Zn':65.38,'Ga':69.723,'Ge':69.723,'As':74.921595,
                    'Se':78.971,'Br':79.904,'Kr':83.798}
MolecularMass=0
MM=0

for t in CL:
    if t[-1] not in Numbers:
            MolecularMass+=MolecularMassChart.get(t)
    else:        
        for r in range(len(t)):
#1.this is more efficient since index 0 is never a number so the process start from t[1]...
#2.bug fix* the last version did not stop after indexing 1'st number of (t)
            if t[r+1] in Numbers:
                MM+=int(t[(r+1)::])
                MM*=MolecularMassChart.get(t[:(r+1):])
                MolecularMass+=MM
                MM-=MM
                break
print(str(MolecularMass)+' g/mol')

input("enter any key to quit.")
