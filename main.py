import cv2
from hand_tracking import Rastreador

# Instanciando o nosso rastreador
meu_rastreador = Rastreador()

cap = cv2.VideoCapture(0)
print("Dando start na webcam... aperta Q pra sair")

while True:
    foi, frame = cap.read()
    if not foi:
        print("Deu ruim no frame da câmera")
        break
        
    # Espelha a imagem pra não bugar a cabeça (como um espelho normal)
    frame = cv2.flip(frame, 1)

    # Passa o frame pro nosso rastreador fazer a mágica
    frame = meu_rastreador.processar_frame(frame)

    cv2.imshow("Projeto AR", frame)

    # Gambiarra padrão do OpenCV pra fechar a janela no 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()