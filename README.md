# Auto_reset_mc_server

You can alter the files: **variables.py**, **ops.json**, **whitelist.json**, **default.properties** and the jsons for bans to adjust your server's settings every time it resets.
It is __**HIGHLY RECOMMENDED**__ to change all of the above before the 1st run :)

By default it resets every week, last reset date is the Chernobyl's explosion (to force it to reset on 1st start).

You can safely put it in the crontab file *(if you use the one and only correct OS)*
For example:

``@reboot cd /home/user/minecraft/Auto_reset_mc_server/ && python3 main.py > log.txt 2>&1``

**THE FILE FOR RUNNING THE SERVER IS main.py**
