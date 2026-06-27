import subprocess
import time
import os
from datetime import datetime, date, timedelta
import variables

def log(text = "TEST"):
    print("   {" + str(datetime.now()) + "}     " + text)

log("STARTING THE LOOP")

last_date_raw = open("last_date", "rt").readline().strip()
log(last_date_raw)
last_date = last_date = datetime.strptime(last_date_raw, "%Y-%m-%d").date()

os.chdir("server_files")
log("changed dir")

process = None

while True:
    today = date.today()
    if today - last_date > timedelta(days=7):
        if process != None:
            process.terminate()
            process.wait()

        log("Getting server files")
        os.system("rm -rf *")
        os.system("wget " + variables.wgetLink)
        log("Server download complete")

        f = open("../last_date", "w")
        f.write(str(today))
        f.close()
    else:
        log("Server doesn't need to get reset yet")

    if process == None or process.poll() != None:
        log("STARTING THE SERVER")
        process = subprocess.Popen(['xterm', '-e', variables.command])
        log("PROCESS STARTED" + str(process))

        f = open("eula.txt", "w")
        f.write("eula=true")
        f.close()

        log("EULA changed")
    else:
        log("Server is running well!")
    log("WAITING 1m")
    time.sleep(60)