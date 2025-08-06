import configparser
import ast
import os


def donne_code_fournisseur_BASWARE(cle_nom_entreprise: str, chemin_ini=".fournisseurs_BASWARE.ini") -> tuple[str, str] | None:
    """
    Charge le fichier .fournisseurs_BASWARE.ini et retourne un tuple (code, nom_complet)
    correspondant à la clé fournie. Retourne None si la clé n'existe pas.
    """
    if not os.path.exists(chemin_ini):
        raise FileNotFoundError(f"Le fichier {chemin_ini} est introuvable.")

    config = configparser.ConfigParser()
    # Pour lire un fichier INI sans section, on ajoute une section fictive
    with open(chemin_ini, 'r', encoding='utf-8') as f:
        contenu = f.read()
        contenu_modifie = "[FOURNISSEURS]\n" + contenu
        config.read_string(contenu_modifie)

    try:
        valeur = config["FOURNISSEURS"][cle_nom_entreprise]
        # Convertir la chaîne de tuple en tuple réel
        return ast.literal_eval(valeur)
    except KeyError:
        return None
    except (SyntaxError, ValueError):
        raise ValueError(f"Le format de la valeur associée à la clé '{cle_nom_entreprise}' est invalide.")


def donne_Moex_BASWARE(nom: str) -> str | None:
    """
    Retourne le nom complet du MOEX Basware associé à l'entrée `nom`.
    La casse des valeurs de retour est préservée.
    """
    nom_normalise = nom.strip().lower()

    correspondances_truong = {"pierre", "truong", "pierre truong"}
    correspondances_magron = {
        "ghislain", "mg", "magron", "magron ghislain",
        "jean-philippe charon", "jp"
    }

    if nom_normalise in correspondances_truong:
        return "TRUONG Pierre"
    elif nom_normalise in correspondances_magron:
        return "MAGRON Ghislain"
    else:
        return None


def donne_code_categorie_d_achat_BASWARE(code_lot: str) -> tuple[str, str] | None:
    """
    Retourne un tuple (code_categorie_d_achat_BASWARE, libelle_categorie_d_achat_BASWARE, designation_des_travaux_BASWARE) correspondant à un code lot donné,
    selon le référentiel BASWARE fourni.
    """
    correspondances = {
        "55-61bis": ("61", "REVETEMENT DE FACADE", "REVETEMENT DE FACADE COLLE"),
        "56-61T": ("61", "REVETEMENT DE FACADE", "ENDUIT RPE FACADE"),
        "35-60": ("60", "ELECTRICITE", "VRD ELECTRICITE"),
        "67-60": ("60", "ELECTRICITE", "DECO ELECTRICITE"),
        "67-59": ("59", "SANITAIRE PLOMBERIE", "DECO PLOMBERIE"),
        "67-57": ("57", "VENTILATION CLIMATISATION", "DECO CVC"),
        "67-56": ("56", "PEINTURE", "DECO PEINTURE"),
        "67-55": ("55", "REVETEMENTS SOLS", "DECO SOLS CARRELAGE"),
        "67-52": ("52", "FAUX PLAFONDS", "DECO FAUX-PLAFONDS"),
        "67-51": ("51", "MENUISERIE INTERIEURE", "DECO MENUISERIE INTERIEURE"),
        "39-60": ("60", "ELECTRICITE", "ELECTRICITE LOCAL ANNEXE"),
        "39-59": ("59", "SANITAIRE PLOMBERIE", "PLOMBERIE LOCAL ANNEXE"),
        "39-57": ("57", "VENTILATION CLIMATISATION", "CVC LOCAL ANNEXE"),
        "39-56": ("56", "PEINTURE", "PEINTURE LOCAL ANNEXE"),
        "39-55": ("55", "REVETEMENTS SOLS", "SOLS DURS LOCAL ANNEXE"),
        "39-52": ("52", "FAUX PLAFONDS", "FAUX-PLAFONDS LOCAL ANNEXE"),
        "39-50": ("50", "MENUISERIE EXT ALU", "MENUISERIE EXTERIEURE LOCAL ANNEXE"),
        "39-49": ("49", "ETANCHEITE EXTERIEURE", "ETANCHEITE LOCAL ANNEXE"),
        "39-47": ("47", "COUVERTURE", "COUVERTURE LOCAL ANNEXE"),
        "39-43": ("43", "FONDATIONS", "GO FONDATIONS"),
        "61bis": ("61", "REVETEMENT DE FACADE", "REVETEMENT DE FACADE COLLE"),
        "61T": ("61", "REVETEMENT DE FACADE", "ENDUIT RPE FACADE"),
        "36C": ("36", "REVETEMENTS TERRASSE", "CARRELAGE TERRASSE"),
        "36B": ("36", "REVETEMENTS TERRASSE", "DALLAGE TERRASSE"),
        "35C": ("60", "ELECTRICITE", "VRD ELECTRICITE"),
        "76": ("76", "REVETEMENTS MURAUX", "REVETEMENTS MURAUX"),
        "60": ("60", "ELECTRICITE", "ELECTRICITE RESTAURANT"),
        "61": ("61", "REVETEMENT DE FACADE", "REVETEMENT DE FACADE RESTAURANT"),
        "59": ("59", "SANITAIRE PLOMBERIE", "PLOMBERIE RESTAURANT"),
        "57": ("57", "VENTILATION CLIMATISATION", "CVC RESTAURANT"),
        "56": ("56", "PEINTURE", "PEINTURE RESTAURANT"),
        "55": ("55", "REVETEMENTS SOLS", "CARRELAGE RESTAURANT"),
        "54": ("54", "VITRERIE MIROITERIE", "VITRERIE RESTAURANT"),
        "52": ("52", "FAUX PLAFONDS", "FAUX PLAFONDS RESTAURANT"),
        "51": ("51", "MENUISERIE INTERIEURE", "MENUISERIES INTERIEURES RESTAURANT"),
        "50": ("50", "MENUISERIE EXT ALU", "MENUISERIES EXTERIEURES RESTAURANT"),
        "49": ("49", "ETANCHEITE EXTERIEURE", "ETANCHEITE RESTAURANT"),
        "48": ("48", "CLOISONS INTERIEURES", "CLOISONS RESTAURANT"),
        "47": ("47", "COUVERTURE", "COUVERTURE RESTAURANT"),
        "46": ("46", "CHARPENTE METALLIQUE", "CHARPENTE RESTAURANT"),
        "45": ("45", "STRUCTURE G.O", "DALLAGE RESTAURANT"),
        "44": ("44", "ASSAINISSEMENT", "RESEAUX SOUS DALLAGE RESTAURANT"),
        "43": ("43", "FONDATIONS", "FONDATIONS RESTAURANT"),
        "39": ("39", "OUVRAGE DIVERS", "OUVRAGE DIVERS"),
        "38": ("38", "ARROSAGE", "ESPACES VERTS ARROSAGE"),
        "37": ("37", "ESPACES VERTS", "ESPACES VERTS "),
        "36": ("36", "REVETEMENTS TERRASSE", "DALLAGE TERRASSE"),
        "35": ("35", "VOIRIE RESEAUX DIVERS", "VRD"),
        "65": ("65", "NETTOYAGE-PROTECTION-DIVERS", "INSTALLATIONS DE CHANTIER")
    }

    return correspondances.get(code_lot)
