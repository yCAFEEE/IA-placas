from ultralytics import YOLO
import cv2
import pyttsx3
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Inicializa a ferramenta que converte texto para voz
engine = pyttsx3.init()

# Criando dicionário para relacionar o código da placa com seu significado

significados_placas = {
    'R-1': 'Parada Obrigatória.',
    'R-2': 'Dê a preferência.',
    'R-6a': 'Proibido estacionar.',
    'R-6b': 'Estacionamento regulamentado.',
    'R-6c': 'Proibido parar e estacionar.',
    'R-7': 'Proibido ultrapassar.',
    'R-19': 'Velocidade máxima permitida.',
    'R-24a': 'Sentido de circulação de via.',
    'R-14b': 'Passagem obrigatória.',
    'R-33': 'Sentido de circulação na rotatória.',
    'A-1a': 'Curva acentuada à esquerda.',
    'A-1b': 'Curva acentuada à direita.',
    'A-2a': 'Curva à esquerda.',
    'A-2b': 'Curva à direita',
    'A-12': 'Interseção em círculo.',
    'A-13a': 'Confluência à esquerda.',
    'A-14': 'Semáforo à frente',
    'A-18': 'Lombada',
    'A-25': 'Mão dupla adiante.',
    'A-27': 'Área com desmoronamento.',
    'A-32a': 'Trânsito de pedestres.',
    'A-32b': 'Passagem sinalizada de pedestres',
    'A-35': 'Animais selvagens.'
}

# Carrega o arquvi best.pt do modelo treinado

model = YOLO("best.pt")

# Função para a criação de fala


# Criação de menu visual

root = tk.Tk()
root.withdraw()

resposta = messagebox.askyesnocancel("DETECÇÃO DE PLACAS DE TRÂNSITO BRASILEIRAS", "Clique em SIM para foto ou NÃO para vídeo")

if resposta is None:
    print("Encerrando....")
    exit()

# SE A ESCOLHA FOI FOTO
if resposta:
    formatos = [("Imagens", "*.jpg *.jpeg *.png *.bmp")]
    caminho_foto = filedialog.askopenfilename(title = "Selecione a Foto", filetypes = formatos)

    if not caminho_foto:
        print("Nenhum arquivo selecionado")
        exit()

    caminho_foto = os.path.abspath(caminho_foto)
    results = model.predict(source = str(caminho_foto), conf = 0.4)

    for result in results:
        frame_placa = result.plot()

        cv2.namedWindow(
            "Analisando foto", cv2.WINDOW_NORMAL)

        cv2.resizeWindow(
            "Analisando foto", 1200, 800)

        cv2.imshow("Analisando foto", frame_placa)

        caixas = result.boxes

        frases = []

        if len(caixas) == 0:
            print('NENHUMA PLACA DETECTADA')
        
        for caixa in caixas:
            id_classe = int(caixa.cls[0])
            nome_classe = model.names[id_classe]

            if nome_classe in significados_placas:
                significado = significados_placas[nome_classe]

                print(f"Detectada placa {nome_classe}: {significado}")

                frases.append(significado)

        if frases:
            texto = ", ".join(frases)   #CONTINUAR DAQUI

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# SE A ESCOLHA FOI VÍDEO
else:
    caminho_video = anexar_arquivo("video")

    if not caminho_video:
        print("Nenhum arquivo selecionado")
        exit()

    captura = cv2.VideoCapture(caminho_video)
    print("Processando vídeo. Para sair, pressione 'q'")

    while captura.isOpened():
        possivel, frame_video = captura.read()
        
        if not possivel:
            break

        results = model.predict(source = frame_video, conf = 0.4, stream = True)

        for result in results:
            frame_placa = result.plot()

            caixas = result.boxes
            for caixa in caixas:
                id_classe = int(caixa.cls[0])
                nome_classe = model.names[id_classe]

                if nome_classe in significados_placas:
                    significado = significados_placas[nome_classe]

                    print(f"Detectada placa {nome_classe}: {significado}")

                    engine.say(significado)
                    engine.runAndWait()
        
        cv2.imshow("Analisando vídeo", frame_placa)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    captura.release()
    cv2.destroyAllWindows()