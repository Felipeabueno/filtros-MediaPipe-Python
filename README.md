Motor de Realidade Aumentada em Python com Visão Computacional

Sobre o Projeto

Este projeto consiste em um motor de realidade aumentada desenvolvido em Python com foco em interação gestual e processamento de imagem em tempo real. A ideia principal surgiu do desejo de criar um sistema onde o usuário pudesse manipular um portal visual usando as mãos, controlando filtros gráficos dinâmicos e interagindo com rastreamento facial baseado em expressões.

O sistema faz a leitura da webcam quadro a quadro, utilizando redes neurais otimizadas para detectar pontos específicos das mãos e do rosto, aplicando matrizes de transformação geométrica e máscaras para fundir efeitos visuais sem perda de fluidez.

Funcionalidades

Portal Polimórfico: O enquadramento do portal se adapta geometricamente à posição dos dedos indicadores e polegares de duas mãos, mantendo as bordas alinhadas mesmo com inclinações.
Sensor de Proximidade por Dedões: A troca de filtros foi pensada para ser fluida. Ao aproximar os polegares, o sistema reconhece o gatilho e alterna o efeito visual instantaneamente.
Arsenal de Filtros: O sistema conta com sete modos diferentes de renderização na região de interesse, indo desde mapas de calor e visão estilo raio-x até distorções geométricas e um sistema de emojis reativos mapeados pelas expressões do rosto.

Tecnologias Utilizadas

Python como linguagem principal de desenvolvimento.
OpenCV para manipulação do fluxo de vídeo, matrizes numpy, recortes por região de interesse e aplicação de transparências alfa.
MediaPipe Tasks para a inferência dos modelos de machine learning voltados ao rastreamento de mãos e landmarks faciais.

Estrutura do Repositório

main.py: Arquivo principal que inicia a captura de vídeo e gerencia o loop de execução.
hand_tracking.py: Módulo responsável por carregar os modelos de IA e processar as coordenadas das mãos e do rosto.
geometry.py: Módulo matemático que calcula o polígono delimitador do portal e controla a lógica de colisão dos dedos.
filters.py: Central de processamento de imagem que aplica os filtros visuais e gerencia a sobreposição dos sprites em PNG.

Como Executar na sua Máquina

Primeiro, clone este repositório na sua máquina e entre na pasta do projeto pelo terminal.
Instale as dependências essenciais executando o comando pip install opencv-python mediapipe numpy.
Certifique-se de baixar os arquivos de modelo hand_landmarker.task e face_landmarker.task, deixando-os salvos na raiz do projeto junto com os códigos.
Adicione três imagens em formato PNG com fundo transparente nomeadas como neutro.png, feliz.png e bravo.png na mesma pasta.
Por fim, execute o projeto rodando o script principal pelo terminal.