from dotenv import load_dotenv
from os import getenv
import serial
import pygame


def main():
    load_dotenv()

    # Definir as variáveis da porta serial
    serial_port = getenv("SERIAL_PORT", default="/dev/ttyACM0")
    serial_speed = getenv("SERIAL_SPEED", default=115200)
    rasp = serial.Serial(serial_port, serial_speed)

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
        5: 3,  # Bairro 5 = botão 3 (Y)
        6: 0,  # Bairro 5 = botão 0 (A)
        7: 2,  # Bairro 5 = botão 2 (X)
        8: 1  # Bairro 5 = botão 1 (B)
    }

    # Iniciar os estados dos bairros
    estados = {
        5: False,
        6: False,
        7: False,
        8: False
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
                            # Escrever na porta serial
                            rasp.write(mensagem.encode())

        # Aguardar 1 segundo
        clock.tick(1000)
        # Se todos os joysticks pararem, parar o loop
        if pygame.joystick.get_count() == 0:
            running = False

    # Fechar o pygame
    pygame.quit()


if __name__ == "__main__":
    main()
