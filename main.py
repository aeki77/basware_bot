import os
import time
import pandas as pd

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from dotenv import load_dotenv
from core.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.ordre_de_service_formulaire_page import OrdreDeServiceFormulairePage
from pages.ordre_de_service_formulaire_demande_approbation_page import OrdreDeServiceFormulaireDemandeApprobationPage


from utils.utils_entrees_OS import donne_code_categorie_d_achat_BASWARE
from core.helpers import safe_click

# Charger les variables du .env
load_dotenv()
USERNAME = os.getenv("BASWARE_USERNAME")
PASSWORD = os.getenv("BASWARE_PASSWORD")
URL = "https://frmcd.p2p.basware.com/"

# from OS_Vouziers import OS_Vouziers

# # Création d’un DataFrame pandas
# df = pd.DataFrame(OS_Vouziers)

# df.to_excel('recapitulatif_OS_VOUZIERS.xlsx', index=False)

# print("Fichier Excel exporté avec succès.")

df = pd.read_excel("recapitulatif_OS_VOUZIERS-restants.xlsx")
OS_Vouziers_donnees = df.to_dict(orient="records")

timeout = 5000
timeout_global = 15000

with BrowserManager() as page:
    login = LoginPage(page)
    login.open(URL)
    login.login(USERNAME, PASSWORD)

    home = HomePage(page)

    home.clique_sur_menu_boutique(timeout=30000)

    home.modifie_le_proprietaire_de_la_demande_d_achat("MAGRON Ghislain")

    OS_formulaire = OrdreDeServiceFormulairePage(page)
    nom_site = "VOUZIERS"
    for ligne in OS_Vouziers_donnees:
        code_categorie_d_achat_BASWARE, libelle_categorie_d_achat_BASWARE, designation_des_travaux_BASWARE = donne_code_categorie_d_achat_BASWARE(code_lot=str(ligne['code_lot']))
        montant_puc = str(round(ligne['montant_puc'] - ligne['montant_ht'], 2))
        ma_designation_des_travaux = "ACTE3 / " + nom_site + " / " + str(ligne['code_lot']) + " / " + designation_des_travaux_BASWARE
        DPGF_to_upload = ligne['chemin_dpgf']
        print(
            f"Code fourn. : {ligne['code_fournisseur']}, "
            f"Fournisseur : {ligne['nom_entreprise']}, "
            f"Cat. Acht . : {code_categorie_d_achat_BASWARE}, "
            f"Code Lot . : {ligne['code_lot']}, "
            f"HT : {ligne['montant_ht']} €, "
            f"PUC : {montant_puc} €"
            f"DPGF : {DPGF_to_upload}"
        )

        home.clique_sur_bouton_ordre_de_service(timeout=30000)

        OS_formulaire.remplir_champs(
            code_fournisseur=str(ligne['code_fournisseur']),
            fournisseur=str(ligne['nom_entreprise']),
            code_categorie_achat=code_categorie_d_achat_BASWARE,
            categorie_achat=libelle_categorie_d_achat_BASWARE,
            code_lot=str(ligne['code_lot']),
            designation_des_travaux=ma_designation_des_travaux,
            montant_ht=str(ligne['montant_ht']),
            montant_puc=montant_puc,
            approbateur="SIEMONEIT",
            nom_site=nom_site,
            timeout=20000
        )
        OS_formulaire.modifier_la_demande_d_achat()
        time.sleep(14)

        OS_upload_DPGF_et_approbation = OrdreDeServiceFormulaireDemandeApprobationPage(page)
        time.sleep(2)

        OS_upload_DPGF_et_approbation._remplir_date_livraison(timeout=30000)
        time.sleep(2)

        OS_upload_DPGF_et_approbation._remplir_adresse_vide(timeout=30000)
        time.sleep(2)

        OS_upload_DPGF_et_approbation.ajouter_fichier_joint(chemin_pdf=DPGF_to_upload)
        time.sleep(2)

        bouton_approbation = OS_upload_DPGF_et_approbation.page.get_by_role("button", name="Obtenir l'approbation").first
        safe_click(bouton_approbation)
        time.sleep(2)

        OS_upload_DPGF_et_approbation.cliquer_sur_bouton_continuer_modal(timeout=timeout)

        time.sleep(7)
        print("Au suivant ... !")
