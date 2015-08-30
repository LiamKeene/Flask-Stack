import pytest

from conftest import test_client

def test_index(request):
    response = test_client(request).get('/')
    assert response.status_code == 200

    assert 'Hello World' in response.get_data()