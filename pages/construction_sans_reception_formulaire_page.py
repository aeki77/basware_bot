from core.base_page import BasePage
from core.helpers import safe_click, safe_fill


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

    def _ouvrir_modale_ajout_pj(self):
        bouton = self.page.locator('button[title="Ajouter un fichier joint"]')
        safe_click(bouton)

        # Attente explicite des éléments dans la modale
        self.page.get_by_text("Ajouter un fichier joint").wait_for(state="visible", timeout=10000)
        self.page.get_by_text("Sélectionner un fichier").wait_for(state="visible", timeout=10000)
        self.page.get_by_role("checkbox", name="Fichier joint envoyé au").wait_for(state="visible", timeout=10000)

        print("✅ Modale 'Ajouter un fichier joint' affichée")

    def _cocher_envoi_fichier_joint(self):
        checkbox = self.page.get_by_role("checkbox", name="Fichier joint envoyé au")
        checkbox.check()
        print("☑️  Checkbox 'Fichier joint envoyé au' cochée")

    def _uploader_fichier_joint(self, chemin_pdf):
        nom_fichier = chemin_pdf.split("/")[-1]  # récupère juste "dave.jpg"

        # Sélectionner l'input file et y envoyer le fichier
        input_file = self.page.locator('input[type="file"]')
        input_file.set_input_files(chemin_pdf)
        print(f"📤 Upload lancé : {nom_fichier}")

        # Attendre que le nom de fichier apparaisse dans la modale
        self.page.get_by_role("dialog").get_by_text(nom_fichier).wait_for(state="visible", timeout=10000)
        print(f"✅ Fichier visible dans la modale : {nom_fichier}")

    def _valider_ajout_fichier_joint(self):
        try:
            bouton_ajouter = self.page.get_by_role("button", name="Ajouter")
            bouton_ajouter.wait_for(state="visible", timeout=5000)
            safe_click(bouton_ajouter)
            print("✅ Fichier joint validé")
        except TimeoutError:
            print("❌ Le bouton 'Ajouter' ne s’est pas activé à temps")

    def ajouter_fichier_joint(self, chemin_pdf):
        self._ouvrir_modale_ajout_pj()
        self._cocher_envoi_fichier_joint()
        self._uploader_fichier_joint(chemin_pdf)
        self._valider_ajout_fichier_joint()

    def remplir_champs(
        self,
        fournisseur: str,
        categorie_achat: str,
        date_debut: str,
        date_fin: str,
        montant_ht: str,
        approbateur: str,
        centre_couts: str,
        projet: str,
        type_depense: str
    ):
        # ✅ Fournisseur *
        try:
            print("🔎 Recherche fournisseur...")
            self.page.get_by_role("combobox", name="Fournisseur *").get_by_label("toggle").click()
            safe_fill(self.page.get_by_role("textbox", name="Fournisseur *"), fournisseur)

            option_selector = self.page.get_by_role("option", name=f"- {fournisseur.upper()}")
            option_selector.wait_for(timeout=3000)
            safe_click(option_selector)
            print(f"✅ Fournisseur sélectionné : {fournisseur}")
        except TimeoutError:
            print(f"❌ Fournisseur introuvable dans la liste : {fournisseur}")
            return

        # ✅ Catégorie d'achat *
        print("📂 Sélection catégorie d'achat")
        self.page.get_by_label("Catégorie d'achat *").click()
        safe_click(self.page.get_by_text(categorie_achat))
        print(f"✅ Catégorie sélectionnée : {categorie_achat}")

        # ✅ Dates
        print("📅 Début : ", date_debut)
        safe_fill(self.page.get_by_role("textbox", name="Début de validité *"), date_debut)

        print("📅 Fin : ", date_fin)
        safe_fill(self.page.get_by_role("textbox", name="Fin de validité *"), date_fin)

        # ✅ Montant HT
        print("💰 Montant HT : ", montant_ht)
        montant_input = self.page.get_by_role("textbox", name="Montant HT *")
        montant_input.click()
        montant_input.fill(montant_ht)

        # ✅ Approbateur
        print("👤 Approbateur : ", approbateur)
        self.page.get_by_role("combobox", name="Approbateur").get_by_label("toggle").click()
        safe_fill(self.page.get_by_role("textbox", name="Approbateur"), approbateur)
        safe_click(self.page.get_by_text(approbateur, exact=True))

        # ✅ Centre de coûts *
        print("🏢 Centre de coûts : ", centre_couts)
        self.page.get_by_role("combobox", name="Centre de coûts *").get_by_label("toggle").click()
        safe_fill(self.page.get_by_role("textbox", name="Centre de coûts *"), centre_couts)
        safe_click(self.page.get_by_role("option", name=f"- {centre_couts.upper()}"))

        # ✅ Projet *
        print("📁 Projet : ", projet)
        self.page.get_by_label("Projet *").nth(1).click()
        safe_click(self.page.get_by_text(projet))

        # ✅ Type de dépense *
        print("📦 Type de dépense : ", type_depense)
        self.page.get_by_label("Type de dépense *").nth(1).click()
        safe_click(self.page.get_by_text(type_depense))

        print("✅ Tous les champs ont été remplis")

    def soumettre_demande(self, timeout=30000):
        try:
            print("🚀 Soumission de la demande en cours...")

            # Clic sur "Modifier la demande d'achat"
            self.page.locator("pal-title-bar").filter(
                has_text="Retour Ajouter à la demande"
            ).get_by_label("Modifier la demande d'achat").click()

            # Attente que le composant de chargement disparaisse
            print("⏳ Attente de la fin du traitement (busy spinner)...")
            self.page.locator(".pal-actions-button-busy").wait_for(state="detached", timeout=timeout)

            print("🔁 Redirection en cours...")
            self.page.wait_for_url("**/#/pr-draft-details/**", timeout=timeout)

            # Vérification que certains éléments attendus apparaissent
            self.page.get_by_role("button", name="Données d'en-tête Données d'").wait_for(state="visible", timeout=10000)
            self.page.locator("#pr-details-page").get_by_text("Demande d'achat", exact=True).wait_for(state="visible", timeout=10000)

            print("✅ Demande soumise et brouillon visible")

        except TimeoutError:
            print("❌ Timeout lors de la soumission de la demande d'achat")
        except Exception as e:
            print(f"❌ Erreur lors de la soumission : {e}")
