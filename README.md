# **Detecção de Placas de Trânsito Brasileiras**
--- 

## Estudantes
- Caio Lauro de Lima
- Luma da Silva Bergmann
- Yuri Daniel Moreira Gomes

## Sobre o Trabalho
O objetivo desse trabalho é treinar um modelo de Inteligência Artificial capaz de detectar as principais placas de trânsito brasileiras. \
A Inteligência Artificial foi treinada usando o YOLOv8 no modelo Small e o dataset utilizado é proveniente do GitHub e do Roboflow.

Link para o Google Colab com códigos e detalhes sobre o treinamento: https://colab.research.google.com/drive/1eLLzWHIWbaGtdoQbOKnJLypjfExzhhG9

## Datasets
### Datasets Usados
Nesse trabalho foi utilizado os seguintes datasets prontos:
- Dataset do GitHub: https://github.com/jean2612/Dataset-Placas-Transito
- Dataset do Roboflow: https://universe.roboflow.com/placas-brasileiras/placas-0iqjy

O dataset final que foi usado para treinar a inteligência artificial possui 3763 imagens e está no formato usado pelo YOLOv8. \
O nosso dataset final está disponível em: https://universe.roboflow.com/luma-bergmann/ic_dataset2

## Ferramentas para usar o Agente Inteligente
Para executar o agente inteligente do arquivo `agente_inteligente.py` é necessário a instalação dos seguintes pacotes:
```
ultralytics
opencv-python
pyttsx3
tkinter
libgl1-mesa-glx (para Linux)
python3-tk (para Linux)
```

## Agente Inteligente
Nesse projeto foi implmentado um agente inteligente para ter um retorno após o reconhecimento de uma placa. \
Ao executar o arquivo `agente_inteligente.py` é exibido uma caixa com as seguintes três opções:
- **"Sim" (imagem):** é solicitado o envio de uma imagem ao usuário;
- **"Não" (vídeo):** é solicitado o envio de um vídeo ao usuário;
- **"Cancelar":** encerra o programa.

Nas funções de imagem e vídeo, caso haja seja reconhecido de uma placa, é usado *Text-to-Speech* (conversão de texto para fala) para ditar o que a placa representa.
