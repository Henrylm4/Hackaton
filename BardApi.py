from bardapi import Bard
import openai
import os 
import Interpreter

openai.api_key = "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"
os.environ["_BARD_API_KEY"] = "YgibgNtefjuLXcbnx9WLGzFp1AiSdHmDvFA0elFUPBsQ3lZLR-SBuiERL1zupq5Nz3detw."
deftext= "Puedes traducir lo siguiente al inglés:"
deftext2= "Can you give me with hashtags the latest trends in Tiktok in the next areas: "
deftext3= "Puedes eliminar los corchetes y el texto dentro de ellos además de traducir el siguiente texto al español:"

categories= Interpreter.categorias()
#Traduce el área
#prompt = input("\nIntroduce tu área según el tipo de contenido que creas: ")
completion = openai.Completion.create(engine = "text-davinci-003",
                            prompt = deftext+categories, #cual es la pregunta
                            max_tokens = 4000) #La cantidad de caracteres
print(completion.choices[0].text)

#Consulta a Bard
response= Bard().get_answer(str(deftext2+completion.choices[0].text))["content"]
print(response)


#Traducir Respuesta 
completion2 = openai.Completion.create(engine = "text-davinci-003",
                            prompt = deftext3+response, #cual es la pregunta
                            max_tokens = 3000) #La cantidad de caracteres
print(completion2.choices[0].text)

#Si se desea resumir summary = summarizer.summarize(input_text)
