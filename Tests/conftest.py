import pytest


@pytest.fixture(scope='function')
def init_driver(request):
      driver = webdriver.Remote(Config.HOST, Config.DESIRED_CAP)
      driver.implicitly_wait(5)
      request.cls.driver = driver
      yield
      driver.quit()