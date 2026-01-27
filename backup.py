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
    "tar", "-czvf", "backup.tar.gz",
    f"/home/{usuario}/.config",
    f"/home/{usuario}/bin",
    f"/home/{usuario}/.local/share/fonts",
    f"/home/{usuario}/.local/share/icons",
    f"/home/{usuario}/.local/share/applications",
    f"/home/{usuario}/.zshrc",
    "aurlist.txt", "pkglist.txt"
])

##### LOCAL DE SALVAMENTO DO BACKUP #####
media_Disk = subprocess.check_output(["ls", f"/run/media/{usuario}"], text=True).strip() # Descobrir o nome da media removivel

if os.path.isdir(f"/run/media/{usuario}/{media_Disk}"): # verificar se o pendrive esta
    if os.path.exists(f"/run/media/{usuario}/{media_Disk}/backup.tar.gz"):
        os.remove(f"/run/media/{usuario}/{media_Disk}/backup.tar.gz")

    print("\n\nenviando para media...")
    shutil.move("backup.tar.gz", f"/run/media/{usuario}/{media_Disk}")
    print("arquivo!!")

else: # caso nao encontre pendrive ele salva na pasta /home/usuario/backup
    if os.path.exists(f"/home/{usuario}/Backups/backup.tar.gz"):
        os.remove(f"/home/{usuario}/Backups/backup.tar.gz")

    print("media não encontrado!!")
    print('\n\nenviando para home...')
    shutil.move("backup.tar.gz", f"/home/{usuario}/Backups")
    print("\n\nenviado!!")
