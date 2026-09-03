import cv2
from filters import PortalFiltros

class PortalGeometria:
    def __init__(self):
        self.cor_portal = (0, 255, 0)
        self.espessura = 2
        self.meus_filtros = PortalFiltros()

    def desenhar_portal(self, frame, coordenadas_maos):
        if len(coordenadas_maos) < 2:
            return frame

        altura, largura, _ = frame.shape
        mao1 = coordenadas_maos[0]
        mao2 = coordenadas_maos[1]

        indicador1 = mao1[8]
        dedao2 = mao2[4]

        x1 = int(indicador1.x * largura)
        y1 = int(indicador1.y * altura)
        x2 = int(dedao2.x * largura)
        y2 = int(dedao2.y * altura)

        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)

        if x_min >= 0 and y_min >= 0 and x_max <= largura and y_max <= altura:
            
            # --- NOVA CAMADA DE DEFESA AQUI ---
            # Só recorta a imagem se a largura e a altura forem maiores que zero!
            if (x_max - x_min) > 0 and (y_max - y_min) > 0:
                roi_original = frame[y_min:y_max, x_min:x_max]
                
                roi_filtrado = self.meus_filtros.filtro_negativo(roi_original)
                
                # Segunda defesa: só cola de volta se o filtro funcionou
                if roi_filtrado is not None:
                    frame[y_min:y_max, x_min:x_max] = roi_filtrado

        cv2.rectangle(frame, (x1, y1), (x2, y2), self.cor_portal, self.espessura)

        return frame