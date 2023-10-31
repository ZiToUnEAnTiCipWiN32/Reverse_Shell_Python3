import random  # Importation de la bibliotheque random pour generer des nombres aleatoires
import fileinput  # Importation de la bibliotheque fileinput pour la manipulation de fichiers

# Generation d'un nombre aleatoire entre -10 et 10 et initialisation de la variable 'derniere_valeur_decalage'
derniere_valeur_decalage = valeur_decalage = random.randint(-10, 10)

# Chemin du script de deobfuscation
chemin_script_deobfuscation = "deobfuscate_script.py"

try:
    # Lecture du contenu du fichier "generateur_script_modele.py" qui contient le script modele
    with open("generateur_script_modele.py", "r", encoding="utf-8") as fichier_modele:
        script_modele = fichier_modele.read()

    # Definition d'une fonction pour obfusquer du texte
    def obfuscation(texte):
        texte_obfusque = ""
        for caractere in texte:
            # Obfuscation en ajoutant un decalage aleatoire a chaque caractere
            caractere_obfusque = chr(ord(caractere) + valeur_decalage)
            texte_obfusque += caractere_obfusque
        return texte_obfusque

    # Obfuscation du script modele
    script_modele_obfusque = obfuscation(script_modele)

    # Mise a jour de la variable 'script_modele_obfusque' dans le script de deobfuscation
    nouveau_script_obfusque = script_modele_obfusque
    try:
        with fileinput.FileInput(chemin_script_deobfuscation, inplace=True) as fichier:
            for ligne in fichier:
                if ligne.strip().startswith("script_modele_obfusque ="):
                    # Remplacement de la ligne contenant 'script_modele_obfusque' par la nouvelle valeur
                    print(f'script_modele_obfusque = {nouveau_script_obfusque!r}')
                else:
                    print(ligne, end='')
        print(f"[+] La variable 'script_modele_obfusque' dans '{chemin_script_deobfuscation}' a ete mise a jour.")
        #print(f"[+] La variable '{script_modele_obfusque}' dans '{chemin_script_deobfuscation}' a ete mise a jour.") # pour afficher le payload
    except Exception as e:
        print(f"[!] Une erreur s'est produite lors de la mise a jour de la variable 'script_modele_obfusque' : {str(e)}")

    # Mise a jour de la variable 'derniere_valeur_decalage' dans le script de deobfuscation
    nouvelle_derniere_valeur_decalage = derniere_valeur_decalage
    try:
        with fileinput.FileInput(chemin_script_deobfuscation, inplace=True) as fichier:
            for ligne in fichier:
                if ligne.strip().startswith("derniere_valeur_decalage ="):
                    # Remplacement de la ligne contenant derniere_valeur_decalage par la nouvelle valeur
                    print(f'derniere_valeur_decalage = {nouvelle_derniere_valeur_decalage!r}')
                else:
                    print(ligne, end='')
        print(f"[+] La variable 'derniere_valeur_decalage' dans '{chemin_script_deobfuscation}' a ete mise a jour avec la valeur '{nouvelle_derniere_valeur_decalage}'.\n")
    except Exception as e:
        print(f"[!] Une erreur s'est produite lors de la mise a jour de la variable 'derniere_valeur_decalage' : {str(e)}")
    
except Exception as e:
    print(f"[!] Une erreur s'est produite : {str(e)}")
