from handlers.language import escolher_idioma
from handlers.menu import menu_principal, menu_centros, menu_sistemas
from utils.usuarios import obter_usuario, reiniciar_usuario
from data.centros import CENTROS
from data.sistemas import SISTEMAS
from data.textos import TEXTOS


def iniciar(user_id):
    reiniciar_usuario(user_id)
    return [escolher_idioma()]


def texto(idioma, chave):
    if idioma in TEXTOS and chave in TEXTOS[idioma]:
        return TEXTOS[idioma][chave]
    return TEXTOS["pt"][chave]


def texto_cpf(idioma, usuario):
    base = texto(idioma, "cpf")
    centro_id = usuario.get("centro")

    if centro_id and centro_id in CENTROS:
        centro = CENTROS[centro_id]
        complemento = texto(idioma, "cpf_endereco_com_centro").format(
            centro=centro["nome"],
            cidade=centro["cidade"]
        )
    else:
        complemento = texto(idioma, "cpf_endereco_sem_centro")

    return base + complemento


def texto_tutoria(idioma, usuario):
    intro = texto(idioma, "tutoria_intro")
    centro_id = usuario.get("centro")

    if not centro_id or centro_id not in CENTROS:
        return intro + texto(idioma, "tutoria_sem_centro")

    centro = CENTROS[centro_id]
    tutoria = centro.get("tutoria")

    if tutoria:
        corpo = texto(idioma, "tutoria_com_dados").format(
            centro=centro["nome"],
            site=tutoria["site"],
            email=tutoria["email"],
            equipe=tutoria["equipe"]
        )
    else:
        corpo = texto(idioma, "tutoria_sem_dados").format(
            centro=centro["nome"],
            site=centro["site"]
        )

    return intro + corpo


def responder(user_id, mensagem):
    usuario = obter_usuario(user_id)
    mensagem = mensagem.strip()
    estado = usuario["state"]

    if mensagem == "0" and estado != "escolhendo_idioma":
        usuario["language"] = None
        usuario["state"] = "escolhendo_idioma"
        return [escolher_idioma()]

    if estado == "escolhendo_idioma":
        return tratar_idioma(usuario, mensagem)

    if estado == "menu_principal":
        return tratar_menu_principal(usuario, mensagem)

    if estado == "menu_centros":
        return tratar_centros(usuario, mensagem)

    if estado == "menu_sistemas":
        return tratar_sistemas(usuario, mensagem)

    return [escolher_idioma()]


def tratar_idioma(usuario, mensagem):
    if mensagem == "1":
        usuario["language"] = "pt"
        usuario["state"] = "menu_principal"
        return ["Idioma definido como Português 🇧🇷", menu_principal("pt")]

    elif mensagem == "2":
        usuario["language"] = "en"
        usuario["state"] = "menu_principal"
        return ["Language set to English 🇺🇸", menu_principal("en")]

    elif mensagem == "3":
        usuario["language"] = "es"
        usuario["state"] = "menu_principal"
        return ["Idioma cambiado a Español 🇪🇸", menu_principal("es")]

    return ["Escolha 1, 2 ou 3.\nChoose 1, 2 or 3.\nElige 1, 2 o 3."]


def tratar_menu_principal(usuario, mensagem):
    idioma = usuario["language"]

    if mensagem == "1":
        usuario["state"] = "menu_centros"
        return [menu_centros(idioma)]

    elif mensagem == "2":
        usuario["state"] = "menu_sistemas"
        return [menu_sistemas(idioma)]

    elif mensagem == "3":
        return [texto(idioma, "id_udesc"), menu_principal(idioma)]

    elif mensagem == "4":
        return [texto_cpf(idioma, usuario), menu_principal(idioma)]

    elif mensagem == "5":
        return [texto_tutoria(idioma, usuario), menu_principal(idioma)]

    elif mensagem == "6":
        return [texto(idioma, "soe"), menu_principal(idioma)]

    elif mensagem == "7":
        return [texto(idioma, "residencia"), menu_principal(idioma)]

    return [opcao_invalida(idioma), menu_principal(idioma)]


def tratar_centros(usuario, mensagem):
    idioma = usuario["language"]

    if mensagem in CENTROS:
        centro = CENTROS[mensagem]
        usuario["centro"] = mensagem

        if idioma == "en":
            resposta = (
                f"{centro['nome']}\n\n"
                f"City: {centro['cidade']}\n"
                f"Address: {centro['endereco']}\n"
                f"Website: {centro['site']}"
            )
        elif idioma == "es":
            resposta = (
                f"{centro['nome']}\n\n"
                f"Ciudad: {centro['cidade']}\n"
                f"Dirección: {centro['endereco']}\n"
                f"Sitio: {centro['site']}"
            )
        else:
            resposta = (
                f"{centro['nome']}\n\n"
                f"Cidade: {centro['cidade']}\n"
                f"Endereço: {centro['endereco']}\n"
                f"Site: {centro['site']}"
            )

        usuario["state"] = "menu_principal"
        return [resposta, menu_principal(idioma)]

    if idioma == "en":
        return ["Invalid center. Choose a number from the list."]
    elif idioma == "es":
        return ["Centro inválido. Elige un número de la lista."]
    return ["Centro inválido. Escolha um número da lista."]


def tratar_sistemas(usuario, mensagem):
    idioma = usuario["language"]

    if mensagem in SISTEMAS:
        sistema = SISTEMAS[mensagem]

        if idioma == "en":
            resposta = f"{sistema['nome']}\n\nDescription:\n{sistema['descricao']}\n\nRequirements:\n"
            for requisito in sistema["requisitos"]:
                resposta += f"- {requisito}\n"
            resposta += f"\nAccess:\n{sistema['link']}"
        elif idioma == "es":
            resposta = f"{sistema['nome']}\n\nDescripción:\n{sistema['descricao']}\n\nRequisitos:\n"
            for requisito in sistema["requisitos"]:
                resposta += f"- {requisito}\n"
            resposta += f"\nAcceso:\n{sistema['link']}"
        else:
            resposta = f"{sistema['nome']}\n\nDescrição:\n{sistema['descricao']}\n\nRequisitos:\n"
            for requisito in sistema["requisitos"]:
                resposta += f"- {requisito}\n"
            resposta += f"\nAcesso:\n{sistema['link']}"

        usuario["state"] = "menu_principal"
        return [resposta, menu_principal(idioma)]

    if idioma == "en":
        return ["Invalid system. Choose an option from the list."]
    elif idioma == "es":
        return ["Sistema inválido. Elige una opción de la lista."]
    return ["Sistema inválido. Escolha uma opção da lista."]


def opcao_invalida(idioma):
    if idioma == "en":
        return "Invalid option. Please choose a number from the menu."
    elif idioma == "es":
        return "Opción inválida. Elige un número del menú."
    return "Opção inválida. Escolha um número do menu."
