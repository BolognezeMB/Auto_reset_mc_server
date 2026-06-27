import subprocess
import time
import os
from datetime import datetime, date, timedelta
import variables

def log(text = "TEST"):
    print("   {" + str(datetime.now()) + "}     " + text)

log("STARTING THE LOOP")

os.mkdir("server_files")
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
        process = subprocess.Popen( # Don't blame me for not having logs - Gemini AI wrote this lol
            variables.command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, 
            shell=isinstance(variables.command, str),
        )
        log("PROCESS STARTED" + str(process))

        ## Changing some files to defaults or specified by user
        f = open("eula.txt", "w")
        f.write("eula=true")
        f.close()

        default = open("../default.properties", "rt")
        properties = open("server.properties", "w")
        properties.write(default.read())

        default.close()
        properties.close()
        log("EULA and server properties changed")

        os.system("cp ../server-icon.png server-icon.png")
    else:
        log("Server is running well!")
    log("WAITING 1m")
    time.sleep(60)