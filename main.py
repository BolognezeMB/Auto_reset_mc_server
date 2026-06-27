import subprocess
import time
import os
from datetime import datetime, date, timedelta
import variables

def log(text = "TEST"):
    print("   {" + str(datetime.now()) + "}     " + text)

log("STARTING THE LOOP")

os.makedirs("server_files", exist_ok=True)
os.chdir("server_files")
log("changed dir")

process = None

while True:
    last_date_raw = open("../last_date", "rt").readline().strip()
    log("Last server start:" + last_date_raw)
    last_date = last_date = datetime.strptime(last_date_raw, "%Y-%m-%d").date()
    today = date.today()

    if today - last_date >= timedelta(days=variables.daysToReset):
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

        ## Changing some files to defaults or specified by user
        f = open("eula.txt", "w")
        f.write("eula=true")
        f.close()

        os.system("cp -f ../banned* ./")
        os.system("cp -f ../ops.json ./")
        os.system("cp -f ../server-icon.png server-icon.png")
        os.system("cp -f ../whitelist.json ./")
        os.system("cp -f ../default.properties server.properties")

        log("All needed files changed, added, edited")
        
        process = subprocess.Popen(variables.command, stdout=open("../minecraft_server.log", "a"), stderr=subprocess.STDOUT, shell=True)
        log("PROCESS STARTED" + str(process))

    else:
        log("Server is running well!")
    time.sleep(60)
