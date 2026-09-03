import cv2
import numpy as np

class PortalFiltros:
    def __init__(self):
        self.filtro_atual = 0
        self.total_filtros = 7 
        self.emojis = {}
        
        for emo in ["neutro", "feliz", "bravo"]:
            img = cv2.imread(f"{emo}.png", cv2.IMREAD_UNCHANGED)
            if img is not None:
                self.emojis[emo] = img
            else:
                print(f"AVISO: Imagem '{emo}.png' não encontrada na pasta!")

    def proximo_filtro(self):
        self.filtro_atual = (self.filtro_atual + 1) % self.total_filtros
        print(f"Filtro trocado para: {self.filtro_atual}")

    def sobrepor_png(self, fundo, overlay, x, y):
        if overlay is None: return fundo
        h, w = overlay.shape[0], overlay.shape[1]
        
        # Proteção rigorosa para não dar crash se o emoji vazar da tela
        if x < 0 or y < 0 or x + w > fundo.shape[1] or y + h > fundo.shape[0]: 
            return fundo
        
        alpha = overlay[:, :, 3] / 255.0
        for c in range(0, 3):
            fundo[y:y+h, x:x+w, c] = (alpha * overlay[:, :, c] + (1 - alpha) * fundo[y:y+h, x:x+w, c])
        return fundo

    def aplicar_filtro(self, roi, info_rosto, coords_portal, frame_inteiro):
        if self.filtro_atual == 6:
            if info_rosto and info_rosto["expressao"] in self.emojis:
                x, y, x2, y2 = info_rosto["bbox"]
                emoji_img = self.emojis[info_rosto["expressao"]]
                
                # Só processa se o emoji couber na tela perfeitamente
                if (x2 - x) > 0 and (y2 - y) > 0 and x >= 0 and y >= 0 and x2 <= frame_inteiro.shape[1] and y2 <= frame_inteiro.shape[0]:
                    emoji_redimensionado = cv2.resize(emoji_img, (x2 - x, y2 - y))
                    frame_temp = frame_inteiro.copy()
                    frame_temp = self.sobrepor_png(frame_temp, emoji_redimensionado, x, y)
                    
                    y_min, y_max, x_min, x_max = coords_portal
                    return frame_temp[y_min:y_max, x_min:x_max]
            return roi 

        # Outros filtros
        if self.filtro_atual == 0:
            return cv2.applyColorMap(roi, cv2.COLORMAP_INFERNO)
        elif self.filtro_atual == 1:
            h, w = roi.shape[:2]
            temp = cv2.resize(roi, (max(1, w//15), max(1, h//15)), interpolation=cv2.INTER_LINEAR)
            return cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
        elif self.filtro_atual == 2:
            cinza = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            bordas = cv2.Canny(cinza, 50, 150)
            raio_x = np.zeros_like(roi)
            raio_x[bordas == 255] = [0, 255, 0] 
            return raio_x
        elif self.filtro_atual == 3:
            return cv2.bitwise_not(roi)
        elif self.filtro_atual == 4:
            kernel = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
            sepia = cv2.transform(roi, kernel)
            return np.clip(sepia, 0, 255).astype(np.uint8)
        elif self.filtro_atual == 5:
            b, g, r = cv2.split(roi)
            return cv2.merge((r, b, g))
            
        return roi