import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class Rastreador:
    def __init__(self):
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
        self.detector = vision.HandLandmarker.create_from_options(options)

    def processar_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        
        resultados = self.detector.detect(mp_image)
        
        # Lista pra guardar as coordenadas limpinhas e mandar pra fora
        coordenadas_limpas = []

        if resultados.hand_landmarks:
            altura, largura, _ = frame.shape
            for mao in resultados.hand_landmarks:
                
                # Guarda as coordenadas da mão atual na lista
                coordenadas_limpas.append(mao)
                
                # Opcional: desenhar as bolinhas verdes de debug
                for ponto in mao:
                    x = int(ponto.x * largura)
                    y = int(ponto.y * altura)
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
                    
        # Devolvemos a imagem e a lista de coordenadas juntas!
        return frame, coordenadas_limpas