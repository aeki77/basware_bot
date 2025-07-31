from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


def safe_fill(locator, text, timeout=10000):
    try:
        locator.wait_for(state="visible", timeout=timeout)
        locator.fill(text)
    except PlaywrightTimeoutError:
        print(f"❌ Impossible de remplir le champ : délai dépassé ({timeout} ms)")
    except Exception as e:
        print(f"❌ Erreur inattendue lors du remplissage : {e}")


def safe_click(locator, timeout=10000):
    try:
        locator.wait_for(state="visible", timeout=timeout)
        locator.click()
    except PlaywrightTimeoutError:
        print(f"❌ Impossible de cliquer sur l'élément : délai dépassé ({timeout} ms)")
    except Exception as e:
        print(f"❌ Erreur inattendue lors du clic : {e}")


def safe_select_option(locator, value, timeout=10000):
    try:
        locator.wait_for(state="visible", timeout=timeout)
        locator.select_option(value)
    except PlaywrightTimeoutError:
        print(f"❌ Sélection impossible : délai dépassé ({timeout} ms)")
    except Exception as e:
        print(f"❌ Erreur inattendue lors de la sélection : {e}")


def safe_press(locator, key, timeout=10000):
    try:
        locator.wait_for(state="visible", timeout=timeout)
        locator.press(key)
    except PlaywrightTimeoutError:
        print(f"❌ Touche '{key}' impossible à envoyer : délai dépassé")
    except Exception as e:
        print(f"❌ Erreur inattendue lors de la frappe : {e}")


def safe_wait_for_text(page, text, timeout=10000):
    try:
        locator = page.get_by_text(text)
        locator.wait_for(state="visible", timeout=timeout)
        return locator
    except PlaywrightTimeoutError:
        print(f"❌ Texte '{text}' non visible après {timeout} ms")
        return None
