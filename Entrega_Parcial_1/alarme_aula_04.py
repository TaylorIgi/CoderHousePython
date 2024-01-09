# Criando um alerta com notification.notify()
# A função precisa ter essa definição: 'def alerta(nivel, base, etapa)'
# Ao chamar a função deverá gerar uma janela de alerta;
# Exibir a mensagem "Falha no carregamento da base {base} na etapa {etapa}";
# Exibir a data atual
# O título "Alerta Baixo" quando nivel = 1, "Alerta Medio" quando nivel = 2 e "Alerta Alto" quando nivel = 3

from plyer import notification
from datetime import datetime

def alerta(nivel, base, etapa):
    
    # Identifica o título da mensagem de acordo com o 'nivel' informado
    if nivel == 1:
        MyTitle = "Alerta Baixo"
    elif nivel == 2:
        MyTitle = "Alerta Medio"
    elif nivel == 3:
        MyTitle = "Alerta Alto!!!"
    else:
        MyTitle = "Nivel do alerta não identificado!"

    # Checa se o input 'base' está preenchido
    if base == "":
        MyBase = "NÃO IDENTIFICADA"
    else:
        MyBase = base

    # Checa se o input 'etapa' está preenchido
    if etapa == "":
        MyStage = "NÃO IDENTIFICADA"
    else:
        MyStage = etapa

    # Identifica o horário da notificação
    MyDate = datetime.now().strftime('%y-%m-%d, %H:%M:%S')

    # Exibe a notificação
    notification.notify(
            title = "ATENÇÃO: " + MyTitle,
            message = "Falha durante o carregamento." + "\n" + \
                "Base: " + MyBase + "\n" + \
                "Etapa: " + MyStage + "\n" + \
                "Data: " + MyDate,
            # app_name = "App teste",
            timeout = 20
            # toast = True
        )
    
# Chama a função conforme os inputs do usuário
UserNivel = int(input("Digite o nivel do alerta: "))
UserBase = str(input("Digite o nome da base (deixe em branco se não for possível identificar): "))
UserStage = str(input("Digite o nome da etapa (deixe em branco se não for possível identificar): "))
alerta(UserNivel, UserBase, UserStage)