# About

This script fetch the current user count of your Teamspeak 3 server and publishes it to a mqtt topic.
The published count can then for example be used in Home Assistant

# Installation
- Clone the script
- add the configuration file as defined below
- run `pip install -r requirements.txt`
- run `python3 main.py` to start

# Configuration file
you need to create a config.ini structured like this:
```
[connection]
host = 
port = 
user = 
password =

[mqtt]
host =
port =
username =
password =
topic = teamspeak/users/count

[vserver]
server_id = 1
```

# Home Assistant
The count published to the mqtt topic can be used in Home Assistant

Example Home Assistant sensor configuration:
```
mqtt:
    sensor:
        - name: "Teamspeak Server User count"
          state_topic: "teamspeak/users/count"
          unique_id: "sensor.teamspeak_user_count"