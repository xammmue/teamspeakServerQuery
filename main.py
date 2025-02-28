from ServerQuery import ServerQuery
import configparser
import paho.mqtt.publish as publish
from time import sleep

config = configparser.ConfigParser()

config.read('config.cfg')

connection_details = config['connection']
server_details = config['vserver']
mqtt_details = config['mqtt']

query = ServerQuery(
    host=connection_details['host'],
    port=int(connection_details['port']),
    username=connection_details['user'],
    password=connection_details['password'],
    server_id=int(server_details['server_id'])
)

while True:
    host_info = query.load_host_info()
    clients_online = host_info.virtual_servers_total_clients_online
    max_clients = host_info.virtual_servers_total_max_clients

    print(clients_online)
    print('There are {}/{} users online'.format(clients_online, max_clients))

    publish.single(
        mqtt_details['topic'],
        clients_online,
        hostname=mqtt_details['host'],
        port=int(mqtt_details['port']),
        auth={'username': mqtt_details['username'], 'password': mqtt_details['password']}
    )

    sleep(30)