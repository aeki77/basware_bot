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
    Retourne un tuple (code, libellé) correspondant à un code lot donné,
    selon le référentiel BASWARE fourni.
    """
    correspondances = {
        "55-61bis": ("61", "REVETEMENT DE FACADE"),
        "56-61T": ("61", "REVETEMENT DE FACADE"),
        "35-60": ("60", "ELECTRICITE"),
        "67-60": ("60", "ELECTRICITE"),
        "67-59": ("59", "SANITAIRE PLOMBERIE"),
        "67-57": ("57", "VENTILATION CLIMATISATION"),
        "67-56": ("56", "PEINTURE"),
        "67-55": ("55", "REVETEMENTS SOLS"),
        "67-52": ("52", "FAUX PLAFONDS"),
        "67-51": ("51", "MENUISERIE INTERIEURE"),
        "39-60": ("60", "ELECTRICITE"),
        "39-59": ("59", "SANITAIRE PLOMBERIE"),
        "39-57": ("57", "VENTILATION CLIMATISATION"),
        "39-56": ("56", "PEINTURE"),
        "39-55": ("55", "REVETEMENTS SOLS"),
        "39-52": ("52", "FAUX PLAFONDS"),
        "39-50": ("50", "MENUISERIE EXT ALU"),
        "39-49": ("49", "ETANCHEITE EXTERIEURE"),
        "39-47": ("47", "COUVERTURE"),
        "39-43": ("43", "FONDATIONS"),
        "61bis": ("61", "REVETEMENT DE FACADE"),
        "61T": ("61", "REVETEMENT DE FACADE"),
        "36C": ("36", "REVETEMENTS TERRASSE"),
        "36B": ("36", "REVETEMENTS TERRASSE"),
        "35C": ("60", "ELECTRICITE"),
        "76": ("76", "REVETEMENTS MURAUX"),
        "60": ("60", "ELECTRICITE"),
        "61": ("61", "REVETEMENT DE FACADE"),
        "59": ("59", "SANITAIRE PLOMBERIE"),
        "57": ("57", "VENTILATION CLIMATISATION"),
        "56": ("56", "PEINTURE"),
        "55": ("55", "REVETEMENTS SOLS"),
        "54": ("54", "VITRERIE MIROITERIE"),
        "52": ("52", "FAUX PLAFONDS"),
        "51": ("51", "MENUISERIE INTERIEURE"),
        "50": ("50", "MENUISERIE EXT ALU"),
        "49": ("49", "ETANCHEITE EXTERIEURE"),
        "48": ("48", "CLOISONS INTERIEURES"),
        "47": ("47", "COUVERTURE"),
        "46": ("46", "CHARPENTE METALLIQUE"),
        "45": ("45", "STRUCTURE G.O"),
        "44": ("44", "ASSAINISSEMENT"),
        "43": ("43", "FONDATIONS"),
        "39": ("39", "OUVRAGE DIVERS"),
        "38": ("38", "ARROSAGE"),
        "37": ("37", "ESPACES VERTS"),
        "36": ("36", "REVETEMENTS TERRASSE"),
        "35": ("35", "VOIRIE RESEAUX DIVERS")
    }

    return correspondances.get(code_lot)
