import time  # en haut du fichier
from datetime import datetime

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from core.base_page import BasePage
from core.helpers import safe_click


class OrdreDeServiceFormulaireDemandeApprobationPage(BasePage):
    # ------------------------------------------------------------------ #
    #  API publique
    # ------------------------------------------------------------------ #
    def obtenir_approbation(self):
        self._remplir_date_livraison()
        self._remplir_adresse_vide()
        print("Il ne reste plus qu'à cliquer sur demander approbation !!!!")

    def ajouter_fichier_joint(self, chemin_pdf):
        self._ouvrir_modale_ajout_pj()
        self._cocher_envoi_fichier_joint()
        self._uploader_fichier_joint(chemin_pdf)
        self._valider_ajout_fichier_joint()

    # ------------------------------------------------------------------ #
    #  Méthodes privées
    # ------------------------------------------------------------------ #
    def _remplir_date_livraison(self, timeout=10000):
        try:
            print("📅 Remplissage de la date de livraison souhaitée...")

            # print("\t🖊️ Clic sur le bouton 'crayon' (édition)...")
            # # Clic sur le bouton avec icône crayon (⚠️ fragile)
            # bouton_crayon = self.page.get_by_role("button", name="", exact=True)
            # safe_click(bouton_crayon, timeout)
            # print("\t✅ Clic sur le bouton 'crayon' effectué")
            time.sleep(2)

            # 31 décembre de l’année en cours, au format mm/dd/yyyy
            fin_annee = datetime.now().replace(month=12, day=31).strftime("%d/%m/%Y")

            # Étape 1 : clic sur le champ date
            champ_date = self.page.get_by_role("textbox", name="Date de livraison souhaitée")
            safe_click(champ_date, timeout)
            champ_date.fill(fin_annee)

            time.sleep(2)

            # Étape 3 : clic sur Enregistrer
            bouton_enregistrer = self.page.get_by_label("Réduire Données d'en-tête").get_by_role("button", name="Enregistrer")
            safe_click(bouton_enregistrer, timeout)

            print(f"✅ Date de livraison définie au {fin_annee}")
            time.sleep(7)

        except Exception as e:
            print(f"❌ Erreur lors du remplissage de la date de livraison : {e}")

    def _remplir_adresse_vide(self, timeout=10000):
        try:
            print("📦 Remplissage de l’adresse de livraison personnalisée...")

            # Étape 1 : clic sur le bouton 'Modifier'
            bouton_modifier = self.page.get_by_role("button", name="Modifier", exact=True)
            safe_click(bouton_modifier, timeout)

            # Étape 2 : clic sur l’icône de sélection de l’adresse
            panneau_adresse = self.page.get_by_role("tabpanel", name="Adresse de livraison: null")
            bouton_select_box = panneau_adresse.get_by_label("Select box activate")
            safe_click(bouton_select_box, timeout)

            # Étape 3 : clic sur 'Adresse personnalisée'
            choix_personnalise = self.page.get_by_text("Adresse personnalisée").first
            safe_click(choix_personnalise, timeout)

            # Étape 4 : clic sur 'Enregistrer'
            bouton_enregistrer = self.page.get_by_role("button", name="Enregistrer", exact=True)
            safe_click(bouton_enregistrer, timeout)

            print("✅ Adresse personnalisée sélectionnée et enregistrée")

        except PlaywrightTimeoutError:
            print("❌ Timeout lors du remplissage de l’adresse")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

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

        time.sleep(7)
        # Attendre que le nom de fichier apparaisse dans la modale
        # self.page.get_by_role("dialog").get_by_text(nom_fichier).wait_for(state="visible", timeout=10000)
        print(f"✅ Fichier visible dans la modale : {nom_fichier}")

    def _valider_ajout_fichier_joint(self):
        try:
            bouton_ajouter = self.page.get_by_role("button", name="Ajouter")
            bouton_ajouter.wait_for(state="visible", timeout=5000)
            safe_click(bouton_ajouter)
            print("✅ Fichier joint validé")
        except TimeoutError:
            print("❌ Le bouton 'Ajouter' ne s’est pas activé à temps")