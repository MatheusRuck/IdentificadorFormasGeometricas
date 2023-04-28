import cv2

# Inicializa a câmera
cap = cv2.VideoCapture(0)

# Loop principal
while True:
    # Lê um quadro da câmera
    ret, frame = cap.read()

    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplica um filtro de desfoque para reduzir o ruído
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    edged = cv2.Canny(blur, 40, 150)

    # Encontra os contornos das formas geométricas presentes na imagem
    _, thresh = cv2.threshold(edged, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenha os contornos e coloca o nome da forma geométrica em cima
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = float(w)/h

            if len(approx) == 3:
                cv2.putText(frame, "Triangulo", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.drawContours(frame, [cnt], -1, (255, 0, 0), 5)
    
            elif len(approx) == 4:
                 # Verifica a relação entre altura e largura para determinar se é um quadrado ou retângulo
                if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                    cv2.putText(frame, "Quadrado", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Retangulo", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
                cv2.drawContours(frame, [cnt], -1, (255, 0, 0), 5)

            elif len(approx) == 5:
                cv2.putText(frame, "Pentagono", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.drawContours(frame, [cnt], -1, (255, 0, 0), 5)

            elif len(approx) == 6:
                cv2.putText(frame, "Hexagono", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.drawContours(frame, [cnt], -1, (255, 0, 0), 5)

            else:
                # verifica se o contorno é um círculo
                (xc, yc), radius = cv2.minEnclosingCircle(cnt)
                area_ratio = area / (3.14 * radius * radius)
                if area_ratio > 0.8:
                    cv2.putText(frame, "Circulo", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.drawContours(frame, [cnt], -1, (255, 0, 0), 5)


    # Exibe o quadro resultante na janela
    cv2.imshow('frame', frame)

    # Encerra o loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
