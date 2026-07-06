usuarios = {}


def obter_usuario(user_id):
    if user_id not in usuarios:
        usuarios[user_id] = {
            "language": None,
            "state": "escolhendo_idioma"
        }
    return usuarios[user_id]


def reiniciar_usuario(user_id):
    usuarios[user_id] = {
        "language": None,
        "state": "escolhendo_idioma"
    }
    return usuarios[user_id]
