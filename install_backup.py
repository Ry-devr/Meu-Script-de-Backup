import os, shutil, subprocess

usuario = subprocess.check_output(["whoami"], text=True).strip() # ver usuario longado, q tbm tem o memsmo nome das pasta que sera usada ;)

##### PACOTES #####
if os.path.isfile(f'/run/media/{usuario}/Ventoy/backup.tar.gz'):
    subprocess.run(['tar', '-xvzf', f'/run/media/{usuario}/Ventoy/backup.tar.gz', 'pkglist.txt', 'aurlist.txt'])
elif os.path.isfile(f'/home/{usuario}/Backups/backup.tar.gz'):
    subprocess.run(['tar', '-xvzf', f'/home/{usuario}/Backups/backup.tar.gz', 'pkglist.txt','aurlist.txt'])
else:
    print("arquivo nao encontrado")


