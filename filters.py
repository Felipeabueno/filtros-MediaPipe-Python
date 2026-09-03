import cv2
import numpy as np

class PortalFiltros:
    def __init__(self):
        pass

    # Essa função recebe a imagem recortada (ROI) e inverte as cores
    def filtro_negativo(self, roi):
        # bitwise_not inverte tudo, como num filme fotográfico antigo
        return cv2.bitwise_not(roi)