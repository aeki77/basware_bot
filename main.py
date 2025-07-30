import os

from dotenv import load_dotenv
from core.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.home_page import HomePage

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

    # Prochaine étape : page formulaire...
