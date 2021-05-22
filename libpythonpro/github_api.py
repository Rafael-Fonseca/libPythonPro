import requests


def buscar_avatar(nome):
    """
    Busca o avatar de um usuário no github
    :param nome: String -> Nome do usuário
    :return: String -> Link do avatar
    """

    url = f'https://api.github.com/users/{nome}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']
