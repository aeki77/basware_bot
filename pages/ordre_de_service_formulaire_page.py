import time  # en haut du fichier

from core.base_page import BasePage
from core.helpers import safe_click, safe_fill


class OrdreDeServiceFormulairePage(BasePage):

    # ------------------------------------------------------------------ #
    #  API publique
    # ------------------------------------------------------------------ #
    def modifier_la_demande_d_achat(self, timeout=10000):
        try:
            print("📝 Ouverture de la modification de la demande d'achat...")

            bouton = self.page.locator("pal-title-bar") \
                .filter(has_text="Retour Ajouter à la demande") \
                .get_by_label("Modifier la demande d'achat")

            safe_click(bouton, timeout)

            print("✅ Modification de la demande d'achat ouverte")
        except Exception as e:
            print(f"❌ Erreur lors de l'ouverture de la modification : {e}")

    def remplir_champs(
        self,
        code_fournisseur: str,
        fournisseur: str,
        code_categorie_achat: str,
        categorie_achat: str,
        code_lot: str,
        designation_des_travaux: str,
        montant_ht: str,
        montant_puc: str,
        approbateur: str,
        nom_site: str,
        timeout=10000
    ):
        self._remplir_fournisseur(code=code_fournisseur, fournisseur=fournisseur, timeout=timeout)
        self._remplir_categorie_achat(code_categorie=code_categorie_achat, categorie=categorie_achat, timeout=timeout)
        self._remplir_text_designation_des_travaux(texte=designation_des_travaux, timeout=timeout)
        self._remplir_puc(montant_puc, timeout=timeout)
        self._remplir_operation(f"{code_lot}-{designation_des_travaux}-{nom_site}", timeout=timeout)
        self._remplir_montant_HT(montant_ht, timeout=timeout)
        time.sleep(2)
        self._remplir_approbateur(nom=approbateur, timeout=timeout)
        self._remplir_centre_de_couts(nom_site=nom_site, timeout=timeout)
        self._remplir_projet_ou_sous_site(timeout=timeout)
        self._remplir_type_depense(timeout=timeout)

    # ------------------------------------------------------------------ #
    #  Méthodes privées
    # ------------------------------------------------------------------ #
    def _remplir_categorie_achat(self, code_categorie: str, categorie: str, timeout=10000):
        try:
            print(f"🔎 Remplissage catégorie d'achat avec : {code_categorie}")

            # Étape 1 : Ouvre le combobox
            self.page.get_by_role("combobox", name="Catégorie d'achat *", exact=True) \
                .get_by_label("toggle") \
                .click()

            # Étape 2 : Remplit la barre de recherche
            champ_recherche = self.page.get_by_role("searchbox")
            safe_fill(champ_recherche, code_categorie, timeout)

            # Étape 3 : Attente d’un span contenant le texte complet
            # Exemple : "VOIRIE RESEAUX DIVERS"
            option = self.page.locator("pal-tree-item").filter(has_text=categorie)
            option.wait_for(state="visible", timeout=timeout)

            # Étape 4 : Valide avec Entrée
            champ_recherche.press("Enter")

            print(f"✅ Catégorie d'achat sélectionnée : {code_categorie}")
        except Exception as e:
            print(f"❌ Erreur lors de la sélection de la catégorie d'achat : {e}")

    def _remplir_operation(self, texte: str, timeout=10000):
        try:
            champ_operation = self.page.get_by_role("textbox", name="Opération *")
            champ_operation.click()
            safe_fill(champ_operation, texte, timeout)
            print(f"✅ Champ 'Opération *' rempli avec : {texte}")
        except Exception as e:
            print(f"❌ Erreur lors du remplissage du champ 'Opération *' : {e}")

    def _remplir_puc(self, montant: str, timeout=10000):
        try:
            if "." in montant:
                montant = montant.replace(".", ",")

            champ_puc = self.page.get_by_role("textbox", name="Montant de la PUC")
            champ_puc.click()
            safe_fill(champ_puc, montant, timeout)
            champ_puc.press("Enter")
            print(f"✅ Montant de la PUC renseigné : {montant}")
        except Exception as e:
            print(f"❌ Erreur lors du remplissage de la PUC : {e}")

    def _remplir_montant_HT(self, montant: str, timeout=10000):
        try:
            if "." in montant:
                montant = montant.replace(".", ",")

            champ_ht = self.page.get_by_role("textbox", name="Montant HT *")
            champ_ht.click()
            safe_fill(champ_ht, montant, timeout)
            champ_ht.press("Enter")
            print("Valeur effective :", champ_ht.input_value())
            print(f"✅ Champ 'Montant HT *' rempli avec : {montant}")
        except Exception as e:
            print(f"❌ Erreur lors du remplissage du champ 'Montant HT *' : {e}")

    def _remplir_text_designation_des_travaux(self, texte: str, timeout=10000):
        champ_designation = self.page.get_by_role("textbox", name="Désignation des travaux")
        champ_designation.click()
        safe_fill(champ_designation, texte)

    def _remplir_fournisseur(self, fournisseur: str, code: str, timeout=10000):
        try:
            print("🔎 Sélection du fournisseur...")

            # Étape 1 : Cliquer sur le bouton de déploiement de la combobox
            self.page.locator("bw-freetext-category-supplier-field") \
                .get_by_role("combobox") \
                .locator("div") \
                .filter(has_text="Développer") \
                .get_by_label("Fournisseur *") \
                .click()

            # Étape 2 : Remplir le champ avec le code fournisseur
            champ_fournisseur = self.page.get_by_role("textbox", name="Fournisseur *")
            safe_fill(champ_fournisseur, code, timeout)

            # Étape 3 : Cliquer sur le nom du fournisseur dans la liste déroulante
            # option = self.page.get_by_text(f"- {fournisseur}", exact=True)
            option = self.page.get_by_role("option", name=f"- {fournisseur}")
            option.wait_for(timeout=timeout)
            safe_click(option, timeout)

            print(f"✅ Fournisseur sélectionné : {fournisseur} (code {code})")

        except Exception as e:
            print(f"❌ Échec lors de la sélection du fournisseur '{fournisseur}' : {e}")

    def _remplir_approbateur(self, nom: str, timeout=10000):
        try:
            print(f"🔎 Sélection de l’approbateur : {nom}")

            # Étape 1 : Ouvre le combobox
            self.page.get_by_role("combobox", name="Approbateur") \
                .get_by_label("toggle") \
                .click()

            # Étape 2 : Remplit le champ texte
            champ = self.page.get_by_role("textbox", name="Approbateur")
            safe_fill(champ, nom, timeout)

            # Étape 3 : Attente que l’option filtrée apparaisse (ex. : même nom ou partie du nom)
            option_attendue = self.page.get_by_role("option", name=nom.upper())
            option_attendue.wait_for(state="visible", timeout=timeout)

            # Étape 3 : Valide avec Entrée
            champ.press("Enter")

            print(f"✅ Approbateur sélectionné : {nom}")
        except Exception as e:
            print(f"❌ Erreur lors de la sélection de l’approbateur : {e}")

    def _remplir_centre_de_couts(self, nom_site: str, timeout=10000):
        try:
            print(f"🔎 Remplissage du centre de coûts : {nom_site}")

            # Étape 1 : Ouvre le combobox
            self.page.get_by_role("combobox", name="Centre de coûts (ou Site) *") \
                .get_by_label("toggle") \
                .click()

            # Étape 2 : Remplit le champ
            champ = self.page.get_by_role("textbox", name="Centre de coûts (ou Site) *")
            safe_fill(champ, nom_site, timeout)

            # Étape 3 : Attend qu’une option soit disponible avant validation
            option = self.page.get_by_role("option", name=nom_site.upper())
            option.wait_for(state="visible", timeout=timeout)

            # Étape 3 : Valide
            champ.press("Enter")

            print(f"✅ Centre de coûts sélectionné : {nom_site}")
        except Exception as e:
            print(f"❌ Erreur lors du remplissage du centre de coûts : {e}")

    def _remplir_projet_ou_sous_site(self, timeout=10000):
        try:
            print("🔎 Sélection du projet : '0 - OUVERTURE'")

            # Étape 1 : Ouvre le combobox
            self.page.get_by_role("combobox", name="Projet (ou Sous-site) *") \
                .get_by_label("toggle") \
                .click()

            # Étape 2 : Remplit le champ
            champ = self.page.get_by_role("textbox", name="Projet (ou Sous-site) *")
            safe_fill(champ, '0', timeout)

            # Étape 3 : Attendre que l'option souhaitée apparaisse
            option = self.page.get_by_role("option", name="0 - OUVERTURE")
            option.wait_for(state="visible", timeout=timeout)

            # Étape 3 : Valide avec Enter
            champ.press("Enter")

            print("✅ '0 - OUVERTURE sélectionné")
        except Exception as e:
            print(f"❌ Erreur lors de la sélection du projet : {e}")

    def _remplir_type_depense(self, timeout=10000):
        try:
            print("🔎 Sélection du type de dépense : CAPEX")

            # Étape 1 : Ouvre le combobox
            self.page.get_by_role("combobox", name="Type de dépense *") \
                .get_by_label("toggle") \
                .click()

            # Étape 2 : Clique sur l’option souhaitée
            option = self.page.get_by_role("option", name='CAPEX')
            option.wait_for(state="visible", timeout=timeout)
            option.click()

            print("✅ Type de dépense sélectionné : 'CAPEX'")
        except Exception as e:
            print(f"❌ Erreur lors de la sélection du type de dépense : {e}")
