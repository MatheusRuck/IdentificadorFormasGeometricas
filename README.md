# IdentificadorFormasGeometricas
Projeto desenvolvido em Python para aula de Visão Computacional para identificar formas geométricas.

Identificador de formas geométricas

Descrição do projeto
Este projeto utiliza a biblioteca OpenCV para detectar formas geométricas em tempo real através da câmera do computador. As formas detectadas incluem triângulos, quadrados, retângulos, pentágonos, hexágonos e círculos.

Dependências
OpenCV

Como funciona
O programa captura um quadro da câmera a cada iteração do loop principal. Em seguida, converte a imagem para tons de cinza, aplica um filtro de desfoque para reduzir o ruído e encontra os contornos das formas geométricas presentes na imagem.

A partir dos contornos encontrados, o programa utiliza aproximações para identificar as formas geométricas. Caso seja identificado um triângulo, quadrado, retângulo, pentágono, hexágono ou círculo, a forma é desenhada no quadro capturado e seu nome é exibido acima dela.

O programa continua a capturar e analisar cada quadro da câmera em tempo real até que o usuário pressione a tecla 'q' para sair.

Como executar
1. Clone o repositório ou faça o download dos arquivos em sua máquina
2. Instale as dependências do programa: pip install opencv-python
3. Execute o programa: identificador_formas.py
4. Certifique-se de que sua câmera esteja conectada e funcionando corretamente
5. O programa irá capturar a imagem da câmera e identificar as formas geométricas em tempo real
6. Para sair do programa, pressione a tecla 'q' no teclado. 

Limitações
1. O programa funciona melhor em ambientes com boa iluminação
2. A detecção de formas geométricas pode não ser precisa em imagens com muitos objetos e detalhes complexos
3. A identificação de formas geométricas pode falhar em objetos que não se enquadram em nenhuma das formas pré-definidas (triângulo, quadrado, retângulo, pentágono, hexágono ou círculo)
4. O programa pode ser executado em sistemas operacionais Windows, Mac ou Linux que possuam Python e OpenCV instalados.

