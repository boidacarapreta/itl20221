from dotenv import load_dotenv
from os import getenv
import serial
import pygame


def main():
    load_dotenv()

    # Definir as variáveis de video e porta serial
    getenv("SDL_VIDEODRIVER", default="dummy")
    serial_port = getenv("SERIAL_PORT", default="/dev/ttyACM0")
    serial_speed = getenv("SERIAL_SPEED", default=115200)
    try:
        rasp = serial.Serial(serial_port, serial_speed)
    except:
        rasp = None

    # Iniciar o pygame e relógio interno
    pygame.init()
    clock = pygame.time.Clock()

    # Detectar todos os joysticks e iniciá-los
    joysticks = [pygame.joystick.Joystick(
        i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()

    # Mapear os botões e bairros
    botoes = {
        1: 3,  # Bairro 1 = botão 3 (Y)
        2: 0,  # Bairro 2 = botão 0 (A)
        3: 2,  # Bairro 3 = botão 2 (X)
        4: 1,  # Bairro 4 = botão 1 (B)
        5: 4,  # Bairro 5 = botão 4 (LB)
        6: 5,  # Bairro 6 = botão 5 (RB)
        7: 6,  # Bairro 7 = botão 6 (Back)
        8: 7,  # Bairro 8 = botão 7 (Start)
        9: 8   # Bairro 9 = botão 8 (Xbox)
    }

    # Iniciar os estados dos bairros
    estados = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False
    }

    # Entrar em loop (até haver algum problema com joystick)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for j in range(len(joysticks)):
                    for botao in botoes.keys():
                        if joysticks[j].get_button(botoes[botao]):
                            # Inverter o valor binário do estado
                            estados[botao] = not estados[botao]
                            # Montar a mensagem para enviar pela serial
                            mensagem = str(botao) + \
                                str(int(estados[botao])) + "\n"
                            # Escrever na porta serial (ou em stdout)
                            if rasp:
                                rasp.write(mensagem.encode())
                            else:
                                print(mensagem)

        # Aguardar 1 segundo
        clock.tick(1000)
        # Se todos os joysticks pararem, parar o loop
        if pygame.joystick.get_count() == 0:
            running = False

    # Fechar o pygame
    pygame.quit()


if __name__ == "__main__":
    main()
