import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store',default = 'en',
                     help="Choose language from the list: "
                          "ar, ca, cs, da, de, en-gb, el, es, fi, fr,it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk")

@pytest.fixture(scope = "function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language in ["ar", "ca", "cs", "da", "de", "en", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt",
                            "pt-br", "ro", "ru", "sk", "uk"]:
        logging.info("start chrome browser for test..")
    else:
        raise pytest.UsageError("Select a proper --language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()