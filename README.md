# fan-speed-warning
Plays a tibetan gong if your laptop fan gets slow down or stuck beyond a certain critical speed. (for Mac but can work in other OSes since it is python based)

## Installing
Just add this file to your crontab (and run it every minute)
``* * * * * /usr/bin/python2.7 /path-to-file/temperature-demon.py``

## Dependencies 

### SMC command
You must download and compile SMC fan control for the command line: https://github.com/hholtmann/smcFanControl/tree/master/smc-command
I have embeded the needed .c files in this repo but this is by no means the most up to date version. 

If you are happy to use an old version of smc, just:
``cd smc-sources``
``make all``
``mv smc ..``

### Mplayer 
I use mplayer to play the sound files, you can use anything.
