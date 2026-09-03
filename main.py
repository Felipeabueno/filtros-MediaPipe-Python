import cv2
from hand_tracking import Rastreador
from geometry import PortalGeometria

meu_rastreador = Rastreador()
meu_portal = PortalGeometria() # Inicia o desenhista do portal

cap = cv2.VideoCapture(0)
print("Dando start na webcam... aperta Q pra sair")

while True:
    foi, frame = cap.read()
    if not foi:
        break
        
    frame = cv2.flip(frame, 1)

    # Passo 1: A IA rastreia as mãos e devolve a imagem + as coordenadas
    frame, coordenadas = meu_rastreador.processar_frame(frame)

    # Passo 2: A Geometria pega as coordenadas e desenha o portal
    frame = meu_portal.desenhar_portal(frame, coordenadas)

    cv2.imshow("Projeto AR", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()