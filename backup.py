import os
import subprocess

##### PACOTES PACMAN #####
with open("pkglist.txt", "w") as f:
     subprocess.run(["pacman", "-Qqm",], stdout=f)

##### PACOTES AUR #####
with open("aurlist.txt", "w") as f:
     subprocess.run(["yay", "-Qm", "--aur"], stdout=f)

usuario = subprocess.check_output(["whoami"], text=True).strip()

compactar = subprocess.run([ "tar", "-czvf", "backup.tar.gz", f"/home/{usuario}/.config", f"/home/{usuario}/bin", f"/home/{usuario}/.local/share/fonts", f"/home/{usuario}/.local/share/icons", f"/home/{usuario}/.local/share/applications", f"/home/{usuario}/.zshrc" ,"aurlist.txt", "pkglist.txt"])

##### teste para por automaticamente e escolher a media #####
if os.path.isdir(f"/run/media/{usuario}/Ventoy"):
    print("pacote existe")

print(compactar)
