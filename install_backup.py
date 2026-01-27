import os, subprocess

usuario = subprocess.check_output(["whoami"], text=True).strip() 

##### PACOTES #####
if os.path.isfile(f'/run/media/{usuario}/Ventoy/backup.tar.gz'):
    subprocess.run(['tar', '-xvzf', f'/run/media/{usuario}/Ventoy/backup.tar.gz', 'pkglist.txt', 'aurlist.txt'])
elif os.path.isfile(f'/home/{usuario}/Backups/backup.tar.gz'):
    subprocess.run(['tar', '-xvzf', f'/home/{usuario}/Backups/backup.tar.gz', 'pkglist.txt','aurlist.txt'])
else:
    print("arquivo nao encontrado")

#### TEMPORARIO ESPERO
print("Abra outro terminal e rode o comando: 'pacman -S $(cat pkglist.txt)', depois disso o outro comando: 'yay -S $(cat aurlist.txt)'")
input("Aperte enter quando tudo ja for instalado: ")

##### ARQUIVOS NA HOME #####
subprocess.run(['tar', '-xvzf', 'backup.tar.gz', '-C', f'/home/{usuario}'])
