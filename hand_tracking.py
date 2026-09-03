import cv2
import mediapipe as mp
import math
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class Rastreador:
    def __init__(self):
        base_maos = python.BaseOptions(model_asset_path='hand_landmarker.task')
        self.det_maos = vision.HandLandmarker.create_from_options(vision.HandLandmarkerOptions(base_options=base_maos, num_hands=2))

        base_rosto = python.BaseOptions(model_asset_path='face_landmarker.task')
        self.det_rosto = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=base_rosto, num_faces=1))

    def processar_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        
        res_maos = self.det_maos.detect(mp_img)
        res_rosto = self.det_rosto.detect(mp_img)
        
        coordenadas_maos = res_maos.hand_landmarks if res_maos.hand_landmarks else []
        info_rosto = None

        if res_rosto.face_landmarks:
            rosto = res_rosto.face_landmarks[0]
            altura, largura, _ = frame.shape
            
            # --- SENSOR DE EXPRESSÃO MAIS SENSÍVEL ---
            abertura_boca = math.hypot(rosto[13].x - rosto[14].x, rosto[13].y - rosto[14].y)
            dist_sobrancelhas = math.hypot(rosto[105].x - rosto[334].x, rosto[105].y - rosto[334].y)

            expressao = "neutro"
            # Se abrir um pouco a boca ou sorrir, fica feliz. 
            if abertura_boca > 0.03: 
                expressao = "feliz"
            # Se juntar as sobrancelhas, fica bravo.
            elif dist_sobrancelhas < 0.13: 
                expressao = "bravo"

            # --- AUMENTANDO O TAMANHO DO EMOJI ---
            margem_x = 50
            margem_y = 80 # Mais espaço para cima para cobrir a testa/cabelo
            
            x_min = max(0, int(min([p.x for p in rosto]) * largura) - margem_x)
            x_max = min(largura, int(max([p.x for p in rosto]) * largura) + margem_x)
            y_min = max(0, int(min([p.y for p in rosto]) * altura) - margem_y)
            y_max = min(altura, int(max([p.y for p in rosto]) * altura) + margem_x)
            
            info_rosto = {"expressao": expressao, "bbox": (x_min, y_min, x_max, y_max)}

        return frame, coordenadas_maos, info_rosto