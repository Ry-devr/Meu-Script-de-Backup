import os, shutil, subprocess

usuario = subprocess.check_output(["whoami"], text=True).strip() # ver usuario longado, q tbm tem o memsmo nomd das pasta que sera usada ;)

if os.path.isdir(f'/run/media/{usuario}/Ventoy'):
    subprocess.run(['tar', '-xvzf', f'/run/media/{usuario}/Ventoy/backup.tar.gz', 'pkglist.txt'])

else:
    subprocess.run(['tar', '-xvzf', '/home/ryan/Backups/backup.tar.gz', 'pkglist.txt'])
