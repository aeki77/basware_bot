import os
import time

from dotenv import load_dotenv
from core.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.ordre_de_service_formulaire_page import OrdreDeServiceFormulairePage

# Charger les variables du .env
load_dotenv()
USERNAME = os.getenv("BASWARE_USERNAME")
PASSWORD = os.getenv("BASWARE_PASSWORD")
URL = "https://frmcd.p2p.basware.com/"


with BrowserManager() as page:
    login = LoginPage(page)
    login.open(URL)
    login.login(USERNAME, PASSWORD)

    home = HomePage(page)
    home.clique_sur_menu_boutique()

    # home.modifie_le_proprietaire_de_la_demande_d_achat("TRUONG Pierre")
    # home.clique_sur_menu_boutique()
    home.clique_sur_bouton_ordre_de_service()

    OS_formulaire = OrdreDeServiceFormulairePage(page)
    OS_formulaire.remplir_champs(
        code_fournisseur="37840",
        fournisseur="ACTI NORD",
        code_categorie_achat="35",
        code_lot="35",
        designation_des_travaux="VRD",
        montant_ht="1000",
        montant_puc="12.7",
        approbateur="SIEMONEIT",
        nom_site="VOUZIERS",
        timeout=10000
    )
    OS_formulaire.modifier_la_demande_d_achat()
    time.sleep(127)

    # OS_formulaire._remplir_fournisseur(code="37840", fournisseur="ACTI NORD")
    # OS_formulaire._remplir_categorie_achat(code_categorie='35', timeout=10000)
    # time.sleep(.5)
    # OS_formulaire._remplir_text_designation_des_travaux(texte="Mon texte")
    # time.sleep(.5)
    # OS_formulaire._remplir_puc("57.69")
    # time.sleep(.5)
    # OS_formulaire._remplir_operation("Opération")
    # time.sleep(.5)
    # OS_formulaire._remplir_montant_HT("157.18")
    # time.sleep(2)
    # OS_formulaire._remplir_approbateur(nom="MARECHAL")
    # time.sleep(.5)
    # OS_formulaire._remplir_centre_de_couts(nom_site="VOUZIERS")
    # time.sleep(.5)
    # OS_formulaire._remplir_projet_ou_sous_site()
    # time.sleep(.5)
    # OS_formulaire._remplir_type_depense()
    # time.sleep(30)
    # OS_formulaire._remplir_combobox_categorie_achat("VOIRIE RESEAU DIVERS")
    # Prochaine étape : page formulaire...
