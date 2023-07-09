import json
import openai

openai.api_key = "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"
dtext= "Puedes darme las 5 categorías a las que pertenece el vídeo de tiktok según la transcripción: "
dtext2= ". Y según los objetos que aparecen en el vídeo: "

def categorias():

    with open('D:/Henry/Hackaton/rekognition_labels_metrics.json') as f:
        data = json.load(f)

    with open('transcription.txt', 'r') as archivo:
        contenido = archivo.read()


    dic={}

    dic_or = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

    lista=[]
    len=0
    for k in dic_or:
        if len<15:
            lista.append(k)
            len = len + 1

    images = ', '.join(lista)

    completion = openai.Completion.create(engine = "text-davinci-003",prompt = dtext+contenido+dtext2+images,max_tokens = 1000) #La cantidad de caracteres
    #print(completion.choices[0].text)
    respuesta = completion.choices[0].text
    return respuesta 

