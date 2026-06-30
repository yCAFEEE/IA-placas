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
A divisão dessas imagens se deu da seguinte forma:

> **`test` — 407 imagens** (aprox. 11% do dataset) \
> Imagens separadas apenas para teste.

> **`train` — 2695 imagens** (aprox. 72% do dataset) \
> Imagens usadas para treinar a IA.

> **`valid` — 661 imagens** (aprox. 18% do dataset) \
> Imagens usadas pela IA para validar o treinamento. 

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
Ao executar o arquivo `agente_inteligente.py` é exibido uma caixa com as seguintes opções:
- **Imagem:** é solicitado o envio de uma imagem ao usuário;
- **Vídeo:** é solicitado o envio de um vídeo ao usuário;

Nas funções de imagem e vídeo, caso seja reconhecido de uma placa, é usado *Text-to-Speech* (conversão de texto para fala) para ditar o que a placa representa.

## Placas
Ao todo, a IA é capaz de reconhecer 23 tipos de placas diferentes, sendo elas:
### Placas de regulamentação
- **R-1**: Parada obrigatória
- **R-2**: Dê a preferência
- **R-6a**: Proibido estacionar
- **R-6b**: Estacionamento regulamentado
- **R-6c**: Proibido parar e estacionar
- **R-7**: Proibido ultrapassar
- **R-19**: Velocidade máxima permitida
- **R-24a**: Sentido de circulação de via/pista
- **R-24b**: Passagem obrigatória
- **R-33**: Sentido de circulação na rotatória

### Placas de advertência
- **A-1a**: Curva acentuada à esquerda
- **A-1b**: Curva acentuada à direita
- **A-2a**: Curva à esquerda
- **A-2b**: Curva à direita
- **A-12**: Interseção em círculo
- **A-13a**: Confluência à esquerda
- **A-14**: Semáforo à frente
- **A-18**: Saliência ou lombada
- **A-25**: Mão dupla adiante
- **A-27**: Área com desmoronamento
- **A-32a**: Trânsito de pedestres
- **A-32b**: Passagem sinalizada de pedestres
- **A-35**: Animais
