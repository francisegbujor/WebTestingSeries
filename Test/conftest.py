import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = None
url = "https://the-internet.herokuapp.com/"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service()
        driver = webdriver.Ie(service=service_obj)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    print("Browser: ", browser_name)
    yield driver
    print("Close Driver")
    driver.close()

'''
def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extras = extra
'''


