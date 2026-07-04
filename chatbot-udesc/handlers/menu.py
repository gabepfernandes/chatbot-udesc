def menu_principal(idioma):
    if idioma == "pt":
        return (
            "🏠 Menu Principal\n\n"
            "1️⃣ Endereço dos Centros\n"
            "2️⃣ Sistemas UDESC\n"
            "3️⃣ Como obter o ID UDESC\n"
            "4️⃣ CPF\n"
            "5️⃣ Tutoria\n"
            "6️⃣ SOE\n"
            "7️⃣ Residência Estudantil"
        )

    elif idioma == "en":
        return (
            "🏠 Main Menu\n\n"
            "1️⃣ University Centers\n"
            "2️⃣ UDESC Systems\n"
            "3️⃣ UDESC ID\n"
            "4️⃣ CPF\n"
            "5️⃣ Tutoring\n"
            "6️⃣ Student Support\n"
            "7️⃣ Student Housing"
        )

    elif idioma == "es":
        return (
            "🏠 Menú Principal\n\n"
            "1️⃣ Centros\n"
            "2️⃣ Sistemas UDESC\n"
            "3️⃣ ID UDESC\n"
            "4️⃣ CPF\n"
            "5️⃣ Tutoría\n"
            "6️⃣ SOE\n"
            "7️⃣ Residencia Estudiantil"
        )

def tratar_menu_principal(mensagem, idioma):

    if mensagem == "1":
        return "Você escolheu Endereço dos Centros."

    elif mensagem == "2":
        return "Você escolheu Sistemas UDESC."

    elif mensagem == "3":
        return "Você escolheu Como obter o ID."

    elif mensagem == "4":
        return "Você escolheu CPF."

    elif mensagem == "5":
        return "Você escolheu Tutoria."

    elif mensagem == "6":
        return "Você escolheu SOE."

    elif mensagem == "7":
        return "Você escolheu Residência Estudantil."

    return "Escolha uma opção válida."