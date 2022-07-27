def handleFile(f, cols):
    data = []
    for chunk in f.chunks():
        data.append(chunk.decode('utf-8'))
    print(len(data))
    data = data[0].split('\n')
    
    if data[-1] == '':
        data.pop()
    for i, el in enumerate(data):
        data[i] = data[i].rstrip()
        data[i] = data[i].split('\t')
    dataToDF(data, cols)
        

def transformDate():
    pass
    #to do
    #trnasform file date to datetime.time ore viceversa

def parseRange(input):
    input = list(map(int, input.split(',')))
    return input


import pandas as pd
def dataToDF(data, cols):
    df = pd.DataFrame.from_records(data)
    toDelete = parseRange(cols)
    df.drop(df.columns[toDelete], axis=1, inplace=True)
    print(df)

