import cv2

class PortalGeometria:
    def __init__(self):
        # Cor do retângulo do portal (Verde em BGR)
        self.cor_portal = (0, 255, 0) 
        self.espessura = 2

    def desenhar_portal(self, frame, coordenadas_maos):
        # Se não tem pelo menos duas mãos na tela, nem tenta desenhar o portal
        if len(coordenadas_maos) < 2:
            return frame

        altura, largura, _ = frame.shape
        
        # Pega a primeira e a segunda mão detectadas
        mao1 = coordenadas_maos[0]
        mao2 = coordenadas_maos[1]

        # No MediaPipe, o Ponto 8 é a ponta do Indicador. 
        # O Ponto 4 é a ponta do Dedão.
        indicador1 = mao1[8]
        dedao2 = mao2[4]

        # Converte a coordenada abstrata (0 a 1) para o pixel real da sua tela
        x1 = int(indicador1.x * largura)
        y1 = int(indicador1.y * altura)
        
        x2 = int(dedao2.x * largura)
        y2 = int(dedao2.y * altura)

        # Desenha o retângulo na tela ligando as duas pontas dos dedos
        cv2.rectangle(frame, (x1, y1), (x2, y2), self.cor_portal, self.espessura)

        # Retorna o frame com o retângulo desenhado
        return frame