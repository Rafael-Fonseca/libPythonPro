import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from unittest.mock import Mock

@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='Rafael', email='rafael@gmail.com'), Usuario(nome='Isabela', email='isabela@gmail.com')],
        [Usuario(nome='Rafael', email='rafael@gmail.com')]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rafael@gmail.com',
        'Curso Python Pro',
        'Confira os novos módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Destinario', email='destinatario@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'remetente@gmail.com',
        'Curso Python Pro',
        'Confira os novos módulos'
    )
    enviador.enviar.assert_called_once_with == (
        'remetente@gmail.com',
        'destinatario@gmail.com',
        'Curso Python Pro',
        'Confira os novos módulos'
    )
