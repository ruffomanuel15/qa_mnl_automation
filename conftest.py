""" MODULARIZED PYTEST FIXTURE TO RE-USE ON THE TESTS """

import pytest, os
import inspect
import os.path

#  EXPECT FIXTURE
@pytest.fixture
def expect(request):
    def do_expect(expr, msg=""):
        if not expr:
            _log_failure(request.node, msg)

    return do_expect


def _log_failure(node, msg=""):
    # get filename, line, and context
    (filename, line, funcname, contextlist) = inspect.stack()[2][1:5]
    filename = os.path.basename(filename)
    context = contextlist[0]
    # format entry
    msg = "%s\n" % msg if msg else ""
    entry = ">%s%s%s:%s\n--------" % (context, msg, filename, line)
    # add entry
    if not hasattr(node, "_failed_expect"):
        node._failed_expect = []
    node._failed_expect.append(entry)


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    report = __multicall__.execute()

    if (
        (call.when == "call")
        and report.passed
        and hasattr(item, "_failed_expect")
    ):
        report.outcome = "failed"
        summary = "Failed Expectations:%s" % len(item._failed_expect)
        item._failed_expect.append(summary)
        report.longrepr = "\n".join(item._failed_expect)

    if call.when == "call" and not report.passed:
        pytest_html = item.config.pluginmanager.getplugin("html")

        extra = getattr(report, "extra", [])
        extra.append(pytest_html.extras.url(item.cls.driver.current_url))
        report.extra = extra

    return report


# BROWSER SELECTION
CHROME_DRIVER = os.getenv("CHROME_DRIVER_PATH", "../drivers/chromedriver")
FIREFOX_DRIVER = "../drivers/geckodriver"
os.environ[
    "SELENIUM_SERVER_JAR"
] = "../drivers/selenium-server-standalone-3.141.59.jar"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome-headless",
        help="Please select the browser you wish to use.",
    )
    parser.addoption(
        "--vdi",
        action="store_true",
        default=False,
        help="Run VDI marked tests.",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--vdi"):
        return
    skip_vdi = pytest.mark.skip(
        reason="not in VDI environment, use --vdi to run"
    )
    for item in items:
        if "vdi" in item.keywords:
            item.add_marker(skip_vdi)


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        # RUNNING NORMAL
        global driver
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

    elif browser == "firefox":
        # RUNNING NORMAL
        driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER)

    elif browser == "safari":
        # RUNNING NORMAL
        # Prerequisite to run in Safari:
        # 1. Pull down the “Safari” menu and choose “Preferences”
        # 2. Click on the “Advanced” tab.
        # 3. Check the box next to “Show Develop menu in menu bar”
        # 4. Click the Develop menu from the menu bar
        # 5. Enable Allow Remote Automation
        driver = webdriver.Safari(quiet=True)

    elif browser == "chrome-headless":
        # RUNNING HEADLESS
        options = ChromeOptions()
        options.headless = True
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(
            options=options, executable_path=CHROME_DRIVER
        )

        """run ./drivers/chromedriver -v in terminal to check for the latest version of Chromedriver"""

    elif browser == "firefox-headless":
        # RUNNING HEADLESS
        options = FirefoxOptions()
        options.headless = True
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--no-sandbox")
        driver = webdriver.Firefox(
            options=options, executable_path=FIREFOX_DRIVER
        )

        """run ./drivers/geckodriver --version in terminal to check for the latest version of Geckodriver"""

    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.close()
    driver.quit()
    print("\nTest is finished.")
