from core.base_page import BasePage
from core.helpers import safe_fill, safe_click

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class LoginPage(BasePage):
    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        safe_fill(self.page.get_by_role("textbox", name="Username"), username)
        safe_fill(self.page.get_by_role("textbox", name="Password"), password)
        safe_click(self.page.get_by_role("button", name="Log in"))

        try:
            # On attend que le fond soit chargé
            fond = self.page.locator(".background-container.task")
            fond.wait_for(state="visible", timeout=20000)  # 10s max
            print("✅ Fond d'écran Basware chargé")
        except PlaywrightTimeoutError:
            print("❌ Le fond n’est pas apparu à temps.")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")
