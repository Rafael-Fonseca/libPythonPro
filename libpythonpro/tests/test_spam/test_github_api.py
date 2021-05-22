from unittest.mock import Mock

import pytest

from libpythonpro import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'Rafael-Fonseca', 'id': 24555167,
        'avatar_url': 'https://avatars.githubusercontent.com/u/24555167?v=4',
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value=resp_mock
    return resp_mock.json.return_value['avatar_url']


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Rafael-Fonseca')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
