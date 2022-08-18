def handleFile(f, userInput):
    userInput
    data = []
    for chunk in f.chunks():
        data.append(chunk.decode('utf-8'))
    data = data[0].split('\n')
    
    if data[-1] == '':
        data.pop()
    for i, el in enumerate(data):
        data[i] = data[i].rstrip()
        data[i] = data[i].split('\t')
    return dataToDF(data, userInput)

def parseRange(colInput):
    list_of_cols = []
    for el in colInput.split(','):
        try:
            list_of_cols.append(int(el))
        except ValueError:
            pass
    return list_of_cols


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(df):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    #plt.plot(x, y)
    df.plot.line()
    graph = get_graph()
    return graph


def dataToDF(data, userInput):
    toDelete = parseRange(userInput['columns'])
    df = pd.DataFrame.from_records(data)
    df['datetime'] = df.iloc[:, 1] + ' ' + df.iloc[:, 2]
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.set_index(df['datetime'])
    df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 29]], axis = 1, inplace = True)
    df.drop(toDelete, axis = 1, inplace = True) # delete selected columns
    df = df[~(df['datetime'] > np.datetime64(userInput['dateTo']))]
    df = df[~(df['datetime'] < np.datetime64(userInput['dateFrom']))]
    #df.drop(df.columns[toDelete], axis = 1, inplace = True) 
    df = df.drop(columns=['datetime'])
    df = df.astype(int)

    #df = df.resample(userInput['sampling']).sum().mean(axis=1)
    if userInput['selected_function'] == "MEAN":
        df = df.resample(userInput['sampling']).mean()
    elif userInput['selected_function'] == "SUM":
        df = df.resample(userInput['sampling']).sum()

    #df = df.resample(userInput['sampling']).sum()

    #df =  df.mean(axis=1)
    df = df.round(decimals=2)


    df.index = pd.to_datetime(df.index)
    myGraph = get_plot(df)
    return myGraph
    #plt.show()
    #df.drop(df.columns[toDelete], axis=1, inplace=True)

