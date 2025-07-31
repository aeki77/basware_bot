import time

from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from core.helpers import safe_click


class BrowserManager:
    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def __exit__(self, exc_type, exc_val, exc_tb):

        self._deconnecter_session()

        self.browser.close()
        self.playwright.stop()

    def _deconnecter_session(self, timeout=10000):
        try:
            print("🚪 Déconnexion en cours...")

            # Étape 1 : Clic sur le menu utilisateur
            bouton_user_menu = self.page.get_by_role("button", name="User menu")
            safe_click(bouton_user_menu, timeout)

            # Étape 2 : Clic sur l’option "Se déconnecter"
            bouton_logout = self.page.get_by_role("menuitem", name="Se déconnecter")
            safe_click(bouton_logout, timeout)

            time.sleep(2)
            # Étape 3 : Si le bouton "Cette session uniquement" existe, on clique dessus
            try:
                bouton_session = self.page.get_by_role("button", name="Cette session uniquement")
                bouton_session.wait_for(state="visible", timeout=3000)
                bouton_session.click()
                print("✅ Session actuelle déconnectée")
            except PlaywrightTimeoutError:
                print("ℹ️ Aucun choix de session proposé, déconnexion directe")

            print("✅ Déconnecté avec succès")
        except Exception as e:
            print(f"❌ Erreur lors de la déconnexion : {e}")
