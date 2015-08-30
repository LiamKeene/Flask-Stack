import pytest

from appname import create_app

@pytest.fixture()
def test_client(request):
    app = create_app('appname.config.TestingConfig', env='testing')
    client = app.test_client()

    return client