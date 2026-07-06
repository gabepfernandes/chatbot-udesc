def menu_principal(idioma):
    if idioma == "en":
        return (
            "🏠 Main Menu\n\n"
            "1️⃣ University Centers\n"
            "2️⃣ UDESC systems the student will use\n"
            "3️⃣ How to get the UDESC ID\n"
            "4️⃣ How to get a CPF in Brazil\n"
            "5️⃣ Tutoring information\n"
            "6️⃣ SOE (Student Support)\n"
            "7️⃣ Student Housing information\n\n"
            "Type the number of the desired option or 0️⃣ to change the language."
        )

    elif idioma == "es":
        return (
            "🏠 Menú Principal\n\n"
            "1️⃣ Centros\n"
            "2️⃣ Sistemas UDESC que el estudiante utilizará\n"
            "3️⃣ Cómo obtener el ID UDESC\n"
            "4️⃣ Cómo obtener un CPF en Brasil\n"
            "5️⃣ Información sobre Tutoría\n"
            "6️⃣ SOE (Orientación al Estudiante)\n"
            "7️⃣ Información sobre Residencia Estudiantil\n\n"
            "Escribe el número de la opción deseada o 0️⃣ para cambiar el idioma."
        )

    return (
        "🏠 Menu Principal\n\n"
        "1️⃣ Endereços dos Centros\n"
        "2️⃣ Sistemas UDESC que o estudante utilizará\n"
        "3️⃣ Como obter o ID UDESC\n"
        "4️⃣ Como obter um CPF no Brasil\n"
        "5️⃣ Informações sobre Tutoria\n"
        "6️⃣ SOE (Serviço de Orientação ao Estudante)\n"
        "7️⃣ Informações sobre Residência Estudantil\n\n"
        "Digite o número da opção desejada ou 0️⃣ para trocar o idioma."
    )


def menu_centros(idioma):
    if idioma == "en":
        titulo = "🏫 Choose a UDESC Center:"
        rodape = "Type the number of the desired center."
    elif idioma == "es":
        titulo = "🏫 Elige un Centro de la UDESC:"
        rodape = "Escribe el número del centro deseado."
    else:
        titulo = "🏫 Escolha um Centro da UDESC:"
        rodape = "Digite o número correspondente ao centro desejado."

    return (
        f"{titulo}\n\n"
        "1 - CCT (Joinville)\n"
        "2 - CEART (Florianópolis)\n"
        "3 - CEFID (Florianópolis)\n"
        "4 - ESAG (Florianópolis)\n"
        "5 - FAED (Florianópolis)\n"
        "6 - CAV (Lages)\n"
        "7 - CEPLAN (São Bento do Sul)\n"
        "8 - CERES (Laguna)\n"
        "9 - CEAVI (Ibirama)\n"
        "10 - CEO (Chapecó e Pinhalzinho)\n"
        "11 - CESFI (Balneário Camboriú)\n"
        "12 - CESMO (Caçador)\n"
        "13 - CEAD (Florianópolis)\n\n"
        f"{rodape}"
    )


def menu_sistemas(idioma):
    if idioma == "en":
        titulo = "💻 UDESC Systems:"
        rodape = "Type the number of the desired system."
    elif idioma == "es":
        titulo = "💻 Sistemas UDESC:"
        rodape = "Escribe el número del sistema deseado."
    else:
        titulo = "💻 Sistemas UDESC:"
        rodape = "Digite o número do sistema desejado."

    return (
        f"{titulo}\n\n"
        "1 - SIGA\n"
        "2 - Moodle\n"
        "3 - Office 365\n"
        "4 - Biblioteca\n"
        "5 - SAS\n"
        "6 - Site UDESC\n\n"
        f"{rodape}"
    )
