def safe_fill(locator, text, timeout=5000):
    locator.wait_for(state="visible", timeout=timeout)
    locator.fill(text)


def safe_click(locator, timeout=5000):
    locator.wait_for(state="visible", timeout=timeout)
    locator.click()
