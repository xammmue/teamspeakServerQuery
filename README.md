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