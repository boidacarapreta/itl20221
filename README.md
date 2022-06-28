# Introdução às Telecomunicações, semestre 2022.1

Projeto de uma maquete viva feita com componentes elétricos, microcontrolados ([Micro:bit versão 1.3X](https://tech.microbit.org/hardware/1-3-revision/)) e microprocessados [Raspberry Pi modelo 3B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/).

```mermaid
flowchart LR
    subgraph Mesa de Controle
        Xbox0([Xbox One Controller]) -- USB --> Raspberry0[Raspberry Pi]
        Raspberry0 -- serial --> MicroBit0[Micro:bit]
    end

    subgraph Cidade
        MicroBit0 -- rádio --> Microbit1[Micro:bit - Bairro 1]
        MicroBit0 -- rádio --> Microbit2[Micro:bit - Bairro 2]
        MicroBit0 -- rádio --> Microbit3[Micro:bit - Bairro 3]
        MicroBit0 -- rádio --> Microbit4[Micro:bit - Bairro 4]
        MicroBit0 -- rádio --> Microbit5[Micro:bit - Bairro 5]
        MicroBit0 -- rádio --> Microbit6[Micro:bit - Bairro 6]
        MicroBit0 -- rádio --> Microbit7[Micro:bit - Bairro 7]
        MicroBit0 -- rádio --> Microbit8[Micro:bit - Bairro 8]
        MicroBit0 -- rádio --> Microbit9[Micro:bit - Bairro 9]
    end

    click Raspberry0 "https://github.com/boidacarapreta/itl20221/blob/main/mesa-de-controle.py"
    click Microbit0 "https://github.com/boidacarapreta/itl20221/blob/main/mesa-de-controle.js"
    click Microbit2 "https://github.com/boidacarapreta/itl20221/blob/main/bairro-2.js"
```
