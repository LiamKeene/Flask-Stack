from appname import create_app


class TestConfig:
    def test_dev_config(self):
        """Tests development config loads correctly."""
        app = create_app('appname.config.DevelopmentConfig', env='development')

        assert app.config['DEBUG'] is True

    def test_test_config(self):
        """Tests test config loads correctly."""
        app = create_app('appname.config.TestingConfig', env='testing')

        assert app.config['DEBUG'] is False

    def test_prod_config(self):
        """Tests production config loads correctly."""
        app = create_app('appname.config.ProductionConfig', env='production')