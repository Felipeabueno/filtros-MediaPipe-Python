import cv2
import math
import time
import numpy as np
from filters import PortalFiltros

class PortalGeometria:
    def __init__(self):
        self.cor_portal = (255, 255, 255) 
        self.espessura = 2
        self.meus_filtros = PortalFiltros()
        self.ultimo_palma = time.time() 

    def desenhar_portal(self, frame, coordenadas_maos, info_rosto):
        if len(coordenadas_maos) < 2:
            return frame

        altura, largura, _ = frame.shape
        mao1, mao2 = coordenadas_maos[0], coordenadas_maos[1]

        # Pega os 4 dedos e transforma num polígono fechado
        pontos = [mao1[8], mao1[4], mao2[8], mao2[4]]
        pts_array = np.array([[int(p.x * largura), int(p.y * altura)] for p in pontos], np.int32)
        
        # Cria a casca geométrica do polígono (Convex Hull)
        poligono = cv2.convexHull(pts_array)

        # SENSOR DE PALMAS
        pulso1_x, pulso1_y = int(mao1[0].x * largura), int(mao1[0].y * altura)
        pulso2_x, pulso2_y = int(mao2[0].x * largura), int(mao2[0].y * altura)
        if math.hypot(pulso2_x - pulso1_x, pulso2_y - pulso1_y) < 120 and (time.time() - self.ultimo_palma) > 1.0:
            self.meus_filtros.proximo_filtro()
            self.ultimo_palma = time.time()

        # O MODO AVANÇADO DE APLICAR O FILTRO NO POLÍGONO INCLINADO
        x, y, w, h = cv2.boundingRect(poligono)
        if w > 15 and h > 15 and x >= 0 and y >= 0 and (x+w) <= largura and (y+h) <= altura:
            roi_original = frame[y:y+h, x:x+w]
            coords_portal = (y, y+h, x, x+w)
            
            # Pega o filtro processado
            roi_filtrado = self.meus_filtros.aplicar_filtro(roi_original, info_rosto, coords_portal, frame)
            
            if roi_filtrado is not None:
                # Cria uma máscara preta do tamanho do quadrado
                mask = np.zeros((h, w), dtype=np.uint8)
                # Desenha o polígono inclinado em branco dentro da máscara
                poligono_deslocado = poligono - [x, y]
                cv2.fillConvexPoly(mask, poligono_deslocado, 255)

                # Funde a imagem: onde a máscara é branca, mostra o filtro. Onde é preta, mostra o normal.
                fundo = cv2.bitwise_and(roi_original, roi_original, mask=cv2.bitwise_not(mask))
                frente = cv2.bitwise_and(roi_filtrado, roi_filtrado, mask=mask)
                
                # Cola tudo de volta na tela
                frame[y:y+h, x:x+w] = cv2.add(fundo, frente)

        # Desenha as linhas inclinadas conectando os dedos
        cv2.polylines(frame, [poligono], isClosed=True, color=self.cor_portal, thickness=self.espessura)

        return frame