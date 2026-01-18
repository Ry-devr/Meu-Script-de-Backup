import os
import shutil
import subprocess

##### PACOTES PACMAN #####
with open("pkglist.txt", "w") as f:
     subprocess.run(["pacman", "-Qn",], stdout=f)

##### PACOTES AUR #####
with open("aurlist.txt", "w") as f:
     subprocess.run(["yay", "-Qm", "--aur"], stdout=f)

usuario = subprocess.check_output(["whoami"], text=True).strip() # ver usuario longado, q tbm tem o memsmo nomd das pasta que sera usada ;)

compactar = subprocess.run([ "tar", "-czvf", "backup.tar.gz", f"/home/{usuario}/.config", f"/home/{usuario}/bin", f"/home/{usuario}/.local/share/fonts", f"/home/{usuario}/.local/share/icons", f"/home/{usuario}/.local/share/applications", f"/home/{usuario}/.zshrc" ,"aurlist.txt", "pkglist.txt"])
print(compactar)

##### LOCAL DE SALVAMENTO DO BACKUP #####
if os.path.isdir(f"/run/media/{usuario}/Ventoy"): # verificar se o pendrive esta
    if os.path.exists(f"/run/media/ryan/Ventoy/backup.tar.gz"):
        os.remove(f"/run/media/ryan/Ventoy/backup.tar.gz")

    shutil.move("backup.tar.gz", f"/run/media/{usuario}/Ventoy")
    print("arquivo enviado para pendrive")

else: # caso nao encontre pendrive ele salva na pasta /home/usuario/backup
    if os.path.exists(f"/home/{usuario}/backup"):
        os.remove(f"/run/media/ryan/Ventoy/backup.tar.gz")

    shutil.move("backup.tar.gz", f"/home/{usuario}/Backups")
    print("enviado para a home")
