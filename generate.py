import pickle
import random

#terminal libraries
import sys, getopt

# generates next 3rd word randomly with frequency weights according to dictionary-model
def generation(pathdicts,stroka,n):
    n=int(n)
    with open(pathdicts, 'rb') as handle:
        d1,d2 = pickle.load(handle)

    stroka = stroka.split()
    if len(stroka) == 0:
        s = random.choice(list(d1.keys())[:-1])
        stroka = (s, random.choice(d1[s]))
    elif len(stroka)==1:
        if stroka[0] not in d1:
            s = random.choice(list(d1.keys())[:-1])
            stroka = (s, random.choice(d1[s]))
        else:
            stroka = (stroka[0], random.choice(d1[stroka[0]]))
    else:
        if len(stroka)>n:
            print('please stop typin')
            exit()
        else:
            if (stroka[-2],stroka[-1]) not in d2:
                if stroka[-1] not in d1:
                    s = random.choice(list(d1.keys())[:-1])
                    stroka = (s, random.choice(d1[s]))
                else:
                    stroka = (stroka[-1], random.choice(d1[stroka[-1]]))
            else:
                stroka = (stroka[-2],stroka[-1])

    key=stroka
    spisok = [key[0],key[1]]
    for i in range(n-2):
        if key in d2:
            newWord=random.choice(d2[key])
            spisok += [newWord]
            key = (key[1],newWord)
        else:
            s = random.choice(list(d1.keys())[:-1])
            word=random.choice(d1[s])
            newWord=random.choice(d2[(s, word)])
            spisok += [newWord]
            key = (word,newWord)

    result = spisok[0]
    for i in spisok[1:]:
        if i in [',','.',':','!','?',';']:
            result += i
        else:
            result += ' '+i
    
    print(result)

# terminal part + run function generation
model, prefix, length= 0, '', 0
options, _ = getopt.getopt(sys.argv[1:],'model:prefix:length:', ['model=', 'prefix=','length='])

for opt,arg in options:
    if '--prefix' in opt:
        prefix=arg
    elif '--model' in opt:
        model=arg
    elif '--length' in opt:
        length=arg

if not model or not length:
    print('not enough params')
    exit()

generation(model,prefix,length)