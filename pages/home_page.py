from core.base_page import BasePage
from core.helpers import safe_click


class HomePage(BasePage):
    def clique_sur_menu_boutique(self):
        # Étape 1 : Clique sur le menu "Boutique"
        boutique_item = self.page.get_by_role("menuitem", name="Boutique")
        safe_click(boutique_item)

        # Étape 2 : Attente que le contenu de la boutique se charge
        try:
            self.page.wait_for_selector("text='Construction - avec réception'", timeout=10000)
            self.page.wait_for_selector("text='Ordre de service'", timeout=10000)
            self.page.wait_for_selector("text='Construction - sans réception'", timeout=10000)
            print("✅ Éléments de la boutique visibles")
        except TimeoutError:
            print("❌ Les éléments attendus n'ont pas été trouvés à temps")
            return

    def clique_sur_bouton_construction_sans_reception(self, timeout=10000):
        try:
            bouton = self.page.get_by_text("Construction - sans réception")
            self.page.wait_for_selector("text='Construction - sans réception'", timeout=timeout)
            safe_click(bouton)
            print("✅ Clic sur 'Construction - sans réception' réussi")
        except TimeoutError:
            print("❌ Le bouton 'Construction - sans réception' n'est pas apparu à temps")
