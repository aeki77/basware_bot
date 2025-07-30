from core.base_page import BasePage
from core.helpers import safe_click


class ConstructionSansReceptionFormulairePage(BasePage):
    def attendre_formulaire_charge(self, timeout=10000):
        try:
            # Attente explicite de l’apparition du champ 'Fournisseur *'
            self.page.get_by_role("textbox", name="Fournisseur *").wait_for(state="visible", timeout=timeout)
            self.page.get_by_role('combobox', name='Fournisseur *', exact=True).wait_for(state="visible", timeout=timeout)

            # Attente explicite de l’apparition du champ 'Catégorie d'achat *'
            self.page.get_by_role("textbox", name="Catégorie d'achat *").wait_for(state="visible", timeout=timeout)
            self.page.get_by_role("combobox", name="Catégorie d'achat *", exact=True).wait_for(state="visible", timeout=timeout)

            print("✅ Formulaire d'ordre de service chargé")
        except TimeoutError:
            print("❌ Les champ 'Fournisseur *' et 'Catégorie d'achat *' ne se sont pas affichés à temps")

        ajout_pj_btn = self.page.locator('button[title="Ajouter un fichier joint"]')
        safe_click(ajout_pj_btn)
