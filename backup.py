import os
import shutil
import subprocess

##### PACOTES PACMAN #####
with open("pkglist.txt", "w") as f:
     subprocess.run(["pacman", "-Qn",], stdout=f)

##### PACOTES AUR #####
with open("aurlist.txt", "w") as f:
     subprocess.run(["yay", "-Qm", "--aur"], stdout=f)

usuario = subprocess.check_output(["whoami"], text=True).strip() # Ver usuario longado, q tbm tem o memsmo nome das pasta que sera usada ;)

##### COMPRIMIR #####

subprocess.run([ 
    "tar", "-czvf", f"backup.tar.gz",
    f"/home/{usuario}/Estudos",
    f"/home/{usuario}/projetos",
    f"/home/{usuario}/Imagens",
    f"/home/{usuario}/Documentos",
    f"/home/{usuario}/.config",
    f"/home/{usuario}/bin",
    f"/home/{usuario}/.local/share/fonts",
    f"/home/{usuario}/.local/share/icons",
    f"/home/{usuario}/.local/share/applications",
    f"/home/{usuario}/.zshrc",
    "aurlist.txt", "pkglist.txt"
])

##### LOCAL DE SALVAMENTO DO BACKUP #####

if os.path.isdir(f"/run/media/{usuario}"): # verificar se o pendrive esta
    media_disk = os.listdir(f"/run/media/{usuario}")
    if os.path.exists(f"/run/media/{usuario}/{media_disk[0]}/backup.tar.gz"):
        os.remove(f"/run/media/{usuario}/{media_disk[0]}/backup.tar.gz")

    print(f"\nenviando para {media_disk[0]}...")
    shutil.move("backup.tar.gz", f"/run/media/{usuario}/{media_disk[0]}")
    print("arquivo!!")

else: # caso nao encontre pendrive ele salva na pasta /home/usuario/backup
    if os.path.exists(f"/home/{usuario}/Backups/backup.tar.gz"):
        os.remove(f"/home/{usuario}/Backups/backup.tar.gz")

    print("media não encontrado!!")
    print('\nenviando para home...')
    shutil.move("backup.tar.gz", f"/home/{usuario}/Backups")
    print("enviado!!")
