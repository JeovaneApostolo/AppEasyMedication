from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Isso aqui só precisa para corrigir o bug
from spacy.cli import download
download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("BotMed", tagger_language=ENGSM)

conversa = [
    "Olá",
    "Olá, tudo bem? Como posso ajudar?",
    "Quero adicionar um remédio na minha lista",
    "Qual seria o remédio?",
    "Ibuprofeno",
    "Mais algum?",
    "Não",
    "Ajudo em algo mais?",
    "Só isso, obrigado",
    "escreva parar para encerrar a conversa",
    "Quero saber quais remedios eu tenho",
    "Você tem Ibuprofeno, ",
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

while True:
    mensagem = input("usuario: ")
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)

chatbot.storage.drop()


