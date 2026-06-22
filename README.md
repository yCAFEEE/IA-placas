# Estudantes
- Caio Lauro de Lima
- Luma da Silva Bergmann
- Yuri Daniel Moreira Gomes

# Sobre o Trabalho
O objetivo desse trabalho é treinar um modelo de Inteligência Artificial capaz de detectar as principais placas de trânsito brasileiras. \
A Inteligência Artificial foi treinada usando o YOLOv8 no modelo Small e o dataset utilizado é proveniente do GitHub e do Roboflow.

### Datasets Usados
- Dataset do GitHub: https://github.com/jean2612/Dataset-Placas-Transito
- Dataset do Roboflow: https://universe.roboflow.com/placas-brasileiras/placas-0iqjy

O nosso dataset utilizado para treinar a IA está disponível em: https://universe.roboflow.com/luma-bergmann/ic_dataset2 \
Link para o Google Colab com códigos e detalhes sobre o treinamento: https://colab.research.google.com/drive/1eLLzWHIWbaGtdoQbOKnJLypjfExzhhG9

# Ferramentas para usar o Agente Inteligente
Para executar o agente inteligente do arquivo `agente_inteligente.py` é necessário a instalação dos seguintes pacotes:
```
ultralytics
opencv-python
pyttsx3
tkinter
libgl1-mesa-glx (para Linux)
python3-tk (para Linux)
```

# Agente Inteligente
Nesse projeto foi implmentado um agente inteligente para ter um retorno após o reconhecimento de uma placa. \
Ao executar o arquivo `agente_inteligente.py` é exibido uma caixa com as seguintes três opções:
- **"Sim" (imagem):** é solicitado o envio de uma imagem ao usuário;
- **"Não" (vídeo):** é solicitado o envio de um vídeo ao usuário;
- **"Cancelar":** encerra o programa.

Nas funções de imagem e vídeo, caso haja seja reconhecido de uma placa, é usado *Text-to-Speech* (conversão de texto para fala) para ditar o que a placa representa.
