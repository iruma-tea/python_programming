import subprocess

r = subprocess.run('lsa', shell=True)
print(r.returncode)
