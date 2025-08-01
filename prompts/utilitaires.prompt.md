J'ai besoin d'une fonction donne_code_fournisseur_BASWARE(cle_nom_entreprise:str). Cette fonction charge le fichier ini .fournisseurs_BASWARE.ini et cherche la clé cle_nom_entreprise et retourne la valeur associée.
Le fichier ini .fournisseurs_BASWARE.ini a le format suivant
ACTINORD = "37840", "ACTI NORD"
COLAS = "6671", "COLAS FRANCE"
HOUOT = "12625", "HOUOT CHARPENTE"
FASTE = "69214", "FASTE"
SCM = "46983", "SILVA CONSTRUCTIONS METALLIQUES"
ADI = "65243", "ADI ENTREPRISE"
M2C = "68611", "M2C"
ERIF = "64135", "ERIF"
FORET = "11671", "FORET ENTREPRISE"
RCE = "70242", "REIMS CHAMPAGNE ELECTRICITE"

J'ai besoin d'une fonction donne_Moex_BASWARE(nom:str). Cette fonction renoie

- "TRUONG Pierre", si nom = pierre, Pierre, Truong, Pierre TRUONG
- "MAGRON Ghislain", si nom = Ghislain, mg, Magron, MAGRON, Jean-Philippe CHARON, jp
- None sinon

J'ai besoin d'une fonction donne_code_categorie_d_achat_BASWARE(code_lot:str). Cette fonction renvoie un tuple. Voila de manière exhaustive, les sorties en fonction des entrées possibles

- 55-61bis -> ("61", "REVETEMENT DE FACADE")
- 56-61T -> ("61", "REVETEMENT DE FACADE")
- 35-60 -> ("60", "ELECTRICITE")
- 67-60 -> ("60", "ELECTRICITE")
- 67-59 -> ("59", "SANITAIRE PLOMBERIE")
- 67-57 -> ("57", "VENTILATION CLIMATISATION")
- 67-56 -> ("56", "PEINTURE")
- 67-55 -> ("55", "REVETEMENTS SOLS")
- 67-52 -> ("52", "FAUX PLAFONDS")
- 67-51 -> ("51", "MENUISERIE INTERIEURE")
- 39-60 -> ("60", "ELECTRICITE")
- 39-59 -> ("59", "SANITAIRE PLOMBERIE")
- 39-57 -> ("57", "VENTILATION CLIMATISATION")
- 39-56 -> ("56", "PEINTURE")
- 39-55 -> ("55", "REVETEMENTS SOLS")
- 39-52 -> ("52", "FAUX PLAFONDS")
- 39-50 -> ("50", "MENUISERIE EXT ALU")
- 39-49 -> ("49", "ETANCHEITE EXTERIEURE")
- 39-47 -> ("47", "COUVERTURE")
- 39-43 -> ("43", "FONDATIONS")
- 61bis -> ("61", "REVETEMENT DE FACADE")
- 61T -> ("61", "REVETEMENT DE FACADE")
- 36C -> ("36", "REVETEMENTS TERRASSE")
- 36B -> ("36", "REVETEMENTS TERRASSE")
- 35C -> ("60", "ELECTRICITE")
- 76 -> ("76", "REVETEMENTS MURAUX")
- 60 -> ("60", "ELECTRICITE")
- 61 -> ("61", "REVETEMENT DE FACADE")
- 59 -> ("59", "SANITAIRE PLOMBERIE")
- 57 -> ("57", "VENTILATION CLIMATISATION")
- 56 -> ("56", "PEINTURE")
- 55 -> ("55", "REVETEMENTS SOLS")
- 54 -> ("54", "VITRERIE MIROITERIE")
- 52 -> ("52", "FAUX PLAFONDS")
- 51 -> ("51", "MENUISERIE INTERIEURE")
- 50 -> ("50", "MENUISERIE EXT ALU")
- 49 -> ("49", "ETANCHEITE EXTERIEURE")
- 48 -> ("48", "CLOISONS INTERIEURES")
- 47 -> ("47", "COUVERTURE")
- 46 -> ("46", "CHARPENTE METALLIQUE")
- 45 -> ("45", "STRUCTURE G.O")
- 44 -> ("44", "ASSAINISSEMENT")
- 43 -> ("43", "FONDATIONS")
- 39 -> ("39", "OUVRAGE DIVERS")
- 38 -> ("38", "ARROSAGE")
- 37 -> ("37", "ESPACES VERTS")
- 36 -> ("36", "REVETEMENTS TERRASSE")
- 35 -> ("35", "VOIRIE RESEAUX DIVERS")
