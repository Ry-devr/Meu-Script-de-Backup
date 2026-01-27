import subprocess

pendrive = subprocess.check_output(["ls", f"/run/media/ryan/"], text=True).strip()
print(pendrive)
