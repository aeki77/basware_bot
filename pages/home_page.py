from core.base_page import BasePage
from core.helpers import safe_click, safe_fill


class HomePage(BasePage):
    def clique_sur_menu_boutique(self, timeout=10000):
        # Étape 1 : Clique sur le menu "Boutique"
        boutique_item = self.page.get_by_role("menuitem", name="Boutique")
        safe_click(boutique_item)

        # Étape 2 : Attente que le contenu de la boutique se charge
        try:
            self.page.wait_for_selector("text='Construction - avec réception'", timeout=timeout)
            self.page.wait_for_selector("text='Ordre de service'", timeout=timeout)
            self.page.wait_for_selector("text='Construction - sans réception'", timeout=timeout)
            print("✅ Éléments de la boutique visibles")
        except TimeoutError:
            print("❌ Les éléments attendus n'ont pas été trouvés à temps")
            return

    def clique_sur_bouton_construction_sans_reception(self, timeout=10000):
        try:
            bouton = self.page.get_by_text("Construction - sans réception")
            self.page.wait_for_selector("text='Construction - sans réception'", timeout=timeout)
            safe_click(bouton)
            print("✅ Clic sur 'Construction - sans réception' réussi'")
        except TimeoutError:
            print("❌ Le bouton 'Construction - sans réception' n'est pas apparu à temps")

    def clique_sur_bouton_ordre_de_service(self, timeout=10000):
        bouton = self.page.get_by_text('Ordre de service')
        safe_click(bouton)

        # Étape 2 : Attente que le contenu du formulaire OS se charge
        try:
            titre = self.page.get_by_text('Ordre de service')
            titre.wait_for(state='visible', timeout=timeout)
            print("✅ Clic sur 'Ordre de service'")
        except TimeoutError:
            print("❌ Le titre 'Ordre de service' n'est pas apparu à temps")

    def modifie_le_proprietaire_de_la_demande_d_achat(self, proprietaire: str, timeout=10000):
        # Étape 1 : Ouvrir le menu "Boutique" si nécessaire
        self.clique_sur_menu_boutique(timeout)

        # Étape 2 : Aller dans "Votre demande"
        bouton_votre_demande = self.page.get_by_role('menuitem', name='Votre demande')
        safe_click(bouton_votre_demande, timeout)

        # Étape 3 : Cliquer sur le bouton "Modifier le propriétaire"
        bouton_modif = self.page.locator("pal-title-bar-actions").get_by_role("button", name="Modifier le propriétaire")
        safe_click(bouton_modif, timeout)

        # Étape 4 : Cliquer sur le bouton déroulant (toggle)
        toggle = self.page.get_by_role("button", name="toggle")
        safe_click(toggle, timeout)

        # Étape 5 : Saisir le nom du propriétaire (au moins une partie pour déclencher l'autocomplete)
        champ = self.page.get_by_role("textbox")
        safe_fill(champ, proprietaire[:3], timeout)  # Ex : "TRU"

        # Étape 6 : Cliquer sur l'option correspondante dans la liste déroulante
        option = self.page.get_by_role("option", name=proprietaire)
        safe_click(option, timeout)

        # Étape 7 : Valider la sélection
        bouton_select = self.page.get_by_role('button', name='Sélectionner')
        safe_click(bouton_select, timeout)

        print(f"✅ Propriétaire modifié avec succès : {proprietaire}")


# from core.base_page import BasePage
# from core.helpers import safe_click


# class HomePage(BasePage):
#     def clique_sur_menu_boutique(self, timeout=10000):
#         # Étape 1 : Clique sur le menu "Boutique"
#         boutique_item = self.page.get_by_role("menuitem", name="Boutique")
#         safe_click(boutique_item)

#         # Étape 2 : Attente que le contenu de la boutique se charge
#         try:
#             self.page.wait_for_selector("text='Construction - avec réception'", timeout=timeout)
#             self.page.wait_for_selector("text='Ordre de service'", timeout=timeout)
#             self.page.wait_for_selector("text='Construction - sans réception'", timeout=timeout)
#             print("✅ Éléments de la boutique visibles")
#         except TimeoutError:
#             print("❌ Les éléments attendus n'ont pas été trouvés à temps")
#             return

#     def clique_sur_bouton_construction_sans_reception(self, timeout=10000):
#         try:
#             bouton = self.page.get_by_text("Construction - sans réception")
#             self.page.wait_for_selector("text='Construction - sans réception'", timeout=timeout)
#             safe_click(bouton)
#             print("✅ Clic sur 'Construction - sans réception' réussi'")
#         except TimeoutError:
#             print("❌ Le bouton 'Construction - sans réception' n'est pas apparu à temps")

#     async def clique_sur_bouton_ordre_de_service(self, timeout=10000):
#         bouton = self.page.get_by_text('Ordre de service')
#         safe_click(bouton)

#         # Étape 2 : Attente que le contenu du formulaire OS se charge
#         try:
#             titre = self.page.get_by_text('Ordre de service')
#             await titre.wait_for(state='visible', timeout=timeout)
#             print("✅ Clic sur 'Ordre de service'")
#         except TimeoutError:
#             print("❌ Le titre 'Ordre de service' n'est pas apparu à temps")

#     def modifie_le_proprietaire_de_la_demande_d_achat(self, proprietaire: str, timeout=10000):
#         # Étape 1 : Clique sur le menu "Boutique"
#         self.clique_sur_menu_boutique(timeout)

#         bouton_votre_demande = self.page.get_by_role('menuitem', name='Votre demande')
#         safe_click(bouton_votre_demande)

#         bouton_modification_proprietaire = self.page.locator("pal-title-bar-actions").get_by_role("button", name="Modifier le propriétaire")
#         safe_click(bouton_modification_proprietaire)
#         self.page.get_by_role('textbox').fill(proprietaire)
#         safe_click(self.page.get_by_role('button', name='Sélectionner'))
