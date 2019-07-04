from random import randint
print ('------------------------------------------------------------')
print ('digite 1 para fila de ALTA PRIORIDADE - idosos (60+)')
print ('digite 2 para fila de MEDIA PRIORIDADE - gestantes')
print ('digite 3 para fila de BAIXA PRIORIDADE - resto da população')
print ('------------------------------------------------------------')
print ('Ps. sao apenas 4 atendentes.')
print (' ')

while True:
    f1=[]
    f2=[]
    f3=[]
    for i in range(5):
        b=(randint(0,99))
        inp=int(input('digite em qual fila deseja dar entrada: '))
        if ((inp)==1):
           f1.append(b)
           print ('a fila 1 tem as senhas: ',(f1))
        elif ((inp)==2):
           f2.append(b)
           print ('a fila 2 tem as senhas: ',(f2))
        elif ((inp)==3):
           f3.append(b)
           print ('a fila 3 tem as senhas: ',(f3))
    for i in range(4):   
        if f1!=[]:
            for i in (f1):
                    print ('')
                    print('o primeiro da fila 1 acaba de ser chamado...')
                    print('-------------------------------')
                    f1.pop(0)
                    print ('a fila tem',len(f1),'pessoas')
                    print ('')
        elif (f1==[])and(f2!=[]):
            for i in (f2):
                    print ('')
                    print('o primeiro da fila 2 acaba de ser chamado...')
                    print('-------------------------------')
                    f2.pop(0)
                    print ('a fila tem',len(f2),'pessoas')
                    print ('')
        elif (f1==[])and(f2==[])and(f3!=[]):
            for i in (f3):
                    print ('')
                    print('o primeiro da fila 3 acaba de ser chamado...')
                    print('-------------------------------')
                    f3.pop(0)
                    print ('a fila tem',len(f3),'pessoas')
                    print ('')

                




        

    

