#  Motor de Realidade Aumentada (AR) com Python

Projeto de realidade aumentada desenvolvido em Python que cria um portal interativo no vídeo da câmera através do rastreamento de mãos e rostos em tempo real.

---

##  Demonstração / Preview
*(Adicione aqui um print ou gif da sua aplicação funcionando, por exemplo: `![Preview da Aplicação](assets/demo.gif)`)*

---

##  Stack Tecnológica
* **Python** — Linguagem principal de desenvolvimento.
* **OpenCV (`cv2`)** — Processamento digital de imagens, manipulação de matrizes, recortes por região de interesse (ROI) e alpha blending.
* **MediaPipe Tasks Vision** — Inferência de Machine Learning de alta performance para rastreamento de *Hand Landmarker* e *Face Landmarker*.
* **NumPy** — Computação numérica e manipulação de matrizes de pixels.

---

##  Arquitetura do Projeto
O código é modularizado para separar a lógica de negócio, visão computacional e geometria:
* `main.py` — Orquestrador principal responsável por capturar o fluxo da webcam e reger o loop da aplicação.
* `hand_tracking.py` — Módulo responsável por carregar os modelos de IA e processar as coordenadas dos landmarks das mãos e do rosto.
* `geometry.py` — Módulo matemático que calcula o polígono inclinado do portal e gerencia o gatilho de colisão por toque dos polegares.
* `filters.py` — Fábrica de efeitos visuais responsável pelo processamento de imagem e sobreposição dinâmica dos sprites PNG transparentes.

---

##  Funcionalidades
1. **Portal Polimórfico Inclinado:** As bordas do portal se adaptam perfeitamente à posição dos dedos indicadores e polegares de ambas as mãos, mantendo um enquadramento geométrico estável em qualquer ângulo.
2. **Sensor de Toque por Dedões:** Aproxime os polegares para disparar o gatilho e alternar entre os filtros visuais instantaneamente.
3. **Arsenal de Filtros Dinâmicos:**
   * Mapa de Calor (`COLORMAP_INFERNO`)
   * Pixelado Retro (Estilo Minecraft)
   * Raio-X Neon (Detecção de contornos via Canny)
   * Negativo Fotográfico
   * Filtro Sépia (Vintage)
   * Cyberpunk (Inversão de canais RGB)
   * **Memoji 2D Reativo:** Sistema de rastreamento facial que mapeia as expressões do rosto (Neutro, Feliz e Bravo) e aplica o sprite PNG correspondente em tempo real.

---

##  Como Executar Localmente

### Pré-requisitos
* Python 3.8 ou superior instalado.
* Uma webcam funcional conectada ao computador.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Felipeabueno/Motor-AR-Python.git](https://github.com/Felipeabueno/Motor-AR-Python.git)
   cd Motor-AR-Python

   Crie e ative um ambiente virtual (Opcional, mas recomendado):

```Bash
python -m venv venv
# No Windows (PowerShell):
.\venv\Scripts\Activate
```

Instale as dependências:

```Bash
pip install opencv-python mediapipe numpy
```

Baixe os arquivos de modelo do MediaPipe:

Coloque os arquivos hand_landmarker.task e face_landmarker.task na raiz do projeto.

Adicione os ativos (Assets) faciais:

Insira três imagens .png com fundo transparente nomeadas exatamente como: neutro.png, feliz.png e bravo.png.

Execute a aplicação:

```Bash
python main.py
```

Depois de colar isso no `README.md`, salvar (`Ctrl + S`), rodar o comando de atualizar a URL do repositório que ajustamos agora pouco, é só mandar:

```bash
git add .
git commit -m "docs: atualiza readme e estrutura do projeto"
git push -u origin main
