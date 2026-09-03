import cv2
from hand_tracking import Rastreador
from geometry import PortalGeometria

meu_rastreador = Rastreador()
meu_portal = PortalGeometria()

cap = cv2.VideoCapture(0)
print("Motor AR iniciado. Pressione 'q' para fechar.")

while True:
    foi, frame = cap.read()
    if not foi:
        break
        
    frame = cv2.flip(frame, 1)

    # Agora a IA devolve 3 coisas: frame, coordenadas das mãos e as info do rosto!
    frame, coordenadas, info_rosto = meu_rastreador.processar_frame(frame)

    # Repassamos tudo para a geometria desenhar o portal e gerenciar os filtros
    frame = meu_portal.desenhar_portal(frame, coordenadas, info_rosto)

    cv2.imshow("Projeto AR", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()