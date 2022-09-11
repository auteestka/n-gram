import os      
import pickle

# terminal usage libraries
import sys, getopt

# text clean and create 1-gramm dictionary d1 and 2-gramm dictionary d2
# THE PATH WITH MODEL WILL BE CALLED 'dictionaries.pickle'
def reading(pathfrom,pathdicts):
    all_files = os.listdir(pathfrom)   
    lines = []
    for i in all_files:
        if i != '.DS_Store':
            with open(pathfrom+i) as f:
                lines += f.readlines()
    lines = ' '.join(lines)
    s = lines
    s = s.lower()
    s_new = ''
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'я' or s[i] =='ё' or s[i] ==' ' or s[i] == '-':
            s_new += s[i]
        elif s[i] in [',','.',':','!','?',';']:
            s_new += ' '
            s_new += s[i]
        elif s[i] == '\n':
            s_new += ' '

    s_new = s_new.split()

    d1 = {}
    for i in range(0,len(s_new)-1):
        if s_new[i] in d1:
            d1[s_new[i]] += [s_new[i+1]]
        else:
            d1[s_new[i]] = [s_new[i+1]]
    d2 = {}
    for i in range(1,len(s_new)-1):
        a = (s_new[i-1],s_new[i])
        if a in d2:
            d2[a] += [s_new[i+1]]
        else:
            d2[a] = [s_new[i+1]]

    with open(pathdicts+'dictionaries.pickle', 'wb') as handle:
        pickle.dump((d1,d2), handle, protocol=pickle.HIGHEST_PROTOCOL)
    
# terminal part + run the reading function
input_dir, model = '', ''
options, _ = getopt.getopt(sys.argv[1:],'input-dir:model:', ['input-dir=', 'model=',])
if not options:
    input_dir,model=input().split()
else:
    for opt,arg in options:
        if '--input-dir' in opt:
            input_dir=arg
        elif '--model' in opt:
            model=arg

reading(input_dir,model)