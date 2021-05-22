from unittest.mock import Mock

import pytest

from libpythonpro import github_api

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'Rafael-Fonseca', 'id': 24555167,
        'avatar_url': 'https://avatars.githubusercontent.com/u/24555167?v=4',
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield resp_mock.json.return_value['avatar_url']
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Rafael-Fonseca')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('Rafael-Fonseca')
    assert 'https://avatars.githubusercontent.com/u/24555167?v=4' == url
