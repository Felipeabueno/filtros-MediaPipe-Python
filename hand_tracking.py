import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class Rastreador:
    def __init__(self):
        # Carrega o modelo de IA que você baixou na pasta
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
        self.detector = vision.HandLandmarker.create_from_options(options)

    def processar_frame(self, frame):
        # Prepara a imagem para o formato que a nova IA exige
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        
        # Pede pra IA processar
        resultados = self.detector.detect(mp_image)

        # Desenha os pontos na raça usando OpenCV (fugindo do bug das soluções do mediapipe!)
        if resultados.hand_landmarks:
            altura, largura, _ = frame.shape
            for mao in resultados.hand_landmarks:
                for ponto in mao:
                    # Converte a coordenada matemática da IA para o pixel real da sua tela
                    x = int(ponto.x * largura)
                    y = int(ponto.y * altura)
                    
                    # Desenha uma bolinha verde em cada junta da mão
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                    
        return frame