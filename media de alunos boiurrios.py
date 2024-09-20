import pandas as pd
notas = {
    'alunos': ['miguel','duda','jonas'],
    'burrice' : [100000000000000000000000000000000000000000000000000000000000000000000, 0, 0],
    'inteligawnscia' : [0, 100, 100],
    'spmama bola pra baixo' : [350, 1000, 40],
    'ser pobre' : [10000000000000000, 100, 0],
    'humilhar todos' :[-10000000000000000000000000000000000, 100, 100]
    }
df = pd.DataFrame(notas)



notas = df.loc[df['alunos'] == 'miguel']
print (notas)
