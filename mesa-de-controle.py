import pygame
pygame.init()


def main():

    botoes = {
        5: 3,  # Bairro 5 = botão 3 (Y)
        6: 0,  # Bairro 5 = botão 0 (A)
        7: 2,  # Bairro 5 = botão 2 (X)
        8: 1  # Bairro 5 = botão 1 (B)
    }

    estados = {
        5: False,
        6: False,
        7: False,
        8: False
    }

    clock = pygame.time.Clock()

    joysticks = [pygame.joystick.Joystick(
        i) for i in range(pygame.joystick.get_count())]

    for joy in joysticks:
        joy.init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for j in range(len(joysticks)):
                    for botao in botoes.keys():
                        if joysticks[j].get_button(botoes[botao]):
                            estados[botao] = not estados[botao]
                            print("Bairro", botao, estados[botao])

        clock.tick(1000)
        if pygame.joystick.get_count() == 0:
            running = False

    pygame.quit()


if __name__ == '__main__':
    main()
