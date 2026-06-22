from ultralytics import YOLO
import cv2
import pyttsx3
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import queue
import time


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

# Carrega o arquivo best.pt do modelo treinado

model = YOLO("best.pt")

# Função para a criação de fala

fila_frases = queue.Queue(maxsize=5)   # Fila que conterá as frases


def controlador_frases():    # Thread dedicada para fala
    while True:
        texto = fila_frases.get()

        if texto is None:
            fila_frases.task_done()
            break

        try:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')

            voz_encontrada = False
            for voice in voices:
                if "MARIA" in voice.id.upper():     # Tipo de voz usada pelo pyttsx3
                    engine.setProperty('voice', voice.id)
                    voz_encontrada = True
                    break

            if not voz_encontrada:
                for voice in voices:
                    # Checa o idioma ou o nome da voz
                    lang = [str(l).upper()
                            for l in voice.languages] if voice.languages else []
                    if "PT" in lang or "BR" in lang or "PORTUGUESE" in voice.name.upper():
                        engine.setProperty('voice', voice.id)
                        voz_encontrada = True
                        break

            engine.setProperty('rate', 180)

            engine.say(texto)
            engine.runAndWait()

            engine.stop()

            del engine

        except Exception as e:
            print("Erro ao reproduzir fala: ", e)

        fila_frases.task_done()


# Inicializando a thread de frases
thread_frases = threading.Thread(target=controlador_frases, daemon=True)
thread_frases.start()


# Criação de menu visual

root = tk.Tk()
root.withdraw()

dialog = tk.Toplevel(root)
dialog.geometry('500x100')
dialog.title("DETECÇÃO DE PLACAS DE TRÂNSITO BRASILEIRAS")
dialog.resizable(False, False)
dialog.grab_set()

tk.Label(dialog, text='Selecione o tipo de entrada.', pady=10, padx=20).pack()

btn_frame = tk.Frame(dialog, pady=10)
btn_frame.pack()

resposta = None


def pick_value(value):
    global dialog, resposta

    resposta = value
    dialog.destroy()


tk.Button(btn_frame, text="🎬 Vídeo", width=10,
          command=lambda: pick_value("video")).pack(side="left", padx=8)
tk.Button(btn_frame, text="🖼️ Imagem", width=10,
          command=lambda: pick_value("imagem")).pack(side="right", padx=8)

dialog.protocol("WM_DELETE_WINDOW", lambda: pick_value(None))
root.wait_window(dialog)

if resposta is None:
    print("Encerrando....")
    exit()

if resposta == 'imagem':
    formatos = [("Imagens", "*.jpg *.jpeg *.png *.bmp")]
    caminho_foto = filedialog.askopenfilename(
        title="Selecione a Foto", filetypes=formatos)

    if not caminho_foto:
        print("Nenhum arquivo selecionado")
        exit()

    caminho_foto = os.path.abspath(caminho_foto)
    results = model.predict(source=str(caminho_foto), conf=0.6)

    for result in results:
        frame_placa = result.plot()

        cv2.namedWindow("Analisando foto", cv2.WINDOW_NORMAL)

        h, w = frame_placa.shape
        target_width = min(800, w)
        target_height = int(h * target_width / w)
        cv2.resizeWindow("Analisando foto", target_width, target_height)

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
            texto = ", ".join(frases)
            if not fila_frases.full():
                fila_frases.put(texto)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    formatos = [("Vídeos", "*.mp4 *.avi *.mkv *.mov")]
    caminho_video = filedialog.askopenfilename(
        title="Selecione o Vídeo", filetypes=formatos)

    if not caminho_video:
        print("Nenhum arquivo selecionado")
        exit()

    caminho_video = os.path.abspath(caminho_video)
    captura = cv2.VideoCapture(caminho_video)

    cv2.namedWindow("Analisando video", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Analisando video", 800, 600)

    placas_vistas = {}   # Armazena placas vistas recentemente para a ordem de fala

    print("Processando vídeo. Para sair, pressione 'q'")

    while captura.isOpened():
        possivel, frame_video = captura.read()

        if not possivel:
            break

        tempo_atual = time.time()

        results = model.predict(source=frame_video, conf=0.6, stream=True)

        for result in results:
            frame_placa = result.plot()

            caixas = result.boxes
            frases_frame = []

            for caixa in caixas:
                id_classe = int(caixa.cls[0])
                nome_classe = model.names[id_classe]

                if nome_classe in significados_placas:
                    significado = significados_placas[nome_classe]

                    tempo_anterior = placas_vistas.get(nome_classe, 0)

                    if tempo_atual - tempo_anterior > 4.0:
                        print(f"Detectada placa {nome_classe}: {significado}")

                        frases_frame.append(significado)
                        placas_vistas[nome_classe] = tempo_atual

            if frases_frame:
                texto = ", ".join(frases_frame)
                if not fila_frases.full():
                    fila_frases.put(texto)

        cv2.imshow("Analisando video", frame_placa)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    fila_frases.put(None)

    try:
        fila_frases.join()
    except:
        pass

    captura.release()
    cv2.destroyAllWindows()
