import os
import subprocess

##### PACOTES PACMAN #####
with open("pkglist.txt", "w") as f:
    subprocess.run(["pacman", "-Qqm",], stdout=f)

##### PACOTES AUR #####
with open("aurlist.txt", "w") as f:
    subprocess.run(["yay", "-Qm", "--aur"], stdout=f)

compactar = subprocess.run([ "tar", "-czvf", "backup.tar.gz", "/home/ryan/.config", "/home/ryan/bin", "/home/ryan/.local/share/fonts", "/home/ryan/.local/share/icons", "/home/ryan/.local/share/applications", "/home/ryan/.zshrc" ,"aurlist.txt", "pkglist.txt"])

print(compactar)
