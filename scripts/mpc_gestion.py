import subprocess
import random
import time

# Objectifs :
#  - define if there is sound and "enough" mouvement
#  - launch random music (fade) and define wich is best to stop mouvement
#  - send alert (mail, sms...?)
#  - stop music (fade)
#  - record all infos (date, music, duration...)


# launch mpc stats
p = subprocess.Popen('mpc stats', shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
# txt file
testfile = open('/home/webcam/scripts/retour.txt', 'w')

# get info from subrocess stdout and get line with total tracks number
# write it on txt file
for line in p.stdout.readlines():
    if line[:5] == 'Songs':
        nbr_tracks = line[-5:]
        testfile.write(nbr_tracks)
        testfile.close()

p.wait()

# open and read txt file
mon_fichier = open('/home/webcam/scripts/retour.txt', 'r')
contenu = mon_fichier.read()

# get total tracks number, define random int and lanch mpc with it
zob = random.randint(0, int(contenu))
commande1 = 'mpc play '+zob

subprocess.Popen(commande1, shell=True, stdout=subprocess.PIPE,
                 stderr=subprocess.STDOUT)
