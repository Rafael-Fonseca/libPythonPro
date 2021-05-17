from libpythonpro.spam.enviador_email import Enviador
import pytest

def test_criar_enviador_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['remetente@email.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'destinatario@email.com',
        'assunto',
        'corpo do email'
    )
    assert destinatario in resultado