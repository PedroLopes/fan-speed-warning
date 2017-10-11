import subprocess
import re

output = subprocess.check_output(['./smc', '-f']) #note if you run as crontab you must prepend the complete path here! 
output = re.split(':|\n',output)
for idx, word in enumerate(output):
    word = word.strip()
    if word == "Actual speed":
        speed = output[idx+1].strip()
        if int(speed) < 1500:
            subprocess.call(["osascript", "-e", "set Volume 5"])
            for a in range(10):
                subprocess.call(["mplayer","audio/emergency.wav"]) #note if you run as crontab you must prepend the complete path here! 
        break 
