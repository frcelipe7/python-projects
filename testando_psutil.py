# BSD 3-Clause License

# Copyright (c) 2009, Jay Loden, Dave Daeschler, Giampaolo Rodola'
# All rights reserved.
import datetime
import psutil
from psutil._common import bytes2human


def verificar():
    print('O que voçê deseja inspecionar:')
    pergunta = input("1: Memória Ram\n2: Memória No Disco\n3: Bateria\n4: Internet Status/Velocidade\n\n")
    if pergunta.lower() in '1 memória ram memoria ram':
        memoria_ram()
    if pergunta.lower() in '2 memória no disco memoria no disco':
        memoria_disco()
    if pergunta.lower() in '3 bateria':
        bateria()
    if pergunta.lower() in '4 internet status velocidade':
        internet()


def eu_tentando(info):
    for elemento in info._fields:
        valor = getattr(info, elemento)
        if elemento != "percent":
            valor = bytes2human(valor)
        print(f"{elemento.capitalize()}: {valor}")


def memoria_ram():
    print('MEMÓRIA RAM\n------')
    eu_tentando(psutil.virtual_memory())
    print("\n")


def memoria_disco():
    print('MEMÓRIA NO DISCO\n------')
    eu_tentando(psutil.disk_usage('/'))
    print("\n")


def bateria():
    print('STATUS DA BATERIA\n------')
    battery = psutil.sensors_battery()
    tempo_restante = datetime.timedelta(seconds = battery.secsleft)
    print(f"Porcentagem: {battery.percent}%\nLigada na Tomada: {battery.power_plugged}\nTempo Restante Fora da Tomada: {tempo_restante}\n")
    if battery.percent < 20:
        from pynotifier import Notification

        Notification(
            title="Bateria Baixa",
            description=str(battery.percent) + "%" + " restante!!",
            duration=5,  # Duration in seconds
            
        ).send()


def internet():
    print('INTERNET STATUS/VELOCIDADE')
    net = psutil.net_if_stats()
    print(f"------ Conexão Ethernet ------\nConectado: {net['Ethernet'].isup}\nVelocidade: {net['Ethernet'].speed}")
    print(f"------ Conexão Wi-Fi ------\nConectado: {net['Wi-Fi'].isup}\nVelocidade: {str(float(net['Wi-Fi'].speed)/8.3886)[:7]}\n")


if __name__ == '__main__':
    verificar()