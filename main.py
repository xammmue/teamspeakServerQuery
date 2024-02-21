from ServerQuery import ServerQuery
import configparser
import paho.mqtt.publish as publish

config = configparser.ConfigParser()

config.read('config.cfg')

connection_details = config['connection']
server_details = config['vserver']
mqtt_details = config['mqtt']

query = ServerQuery(host=connection_details['host'], port=int(connection_details['port']),
                    username=connection_details['user'], password=connection_details['password'],
                    server_id=int(server_details['server_id']))

host_info = query.load_host_info()
print(host_info.virtual_servers_total_clients_online)

# client_list = query.load_client_list()
# for client in client_list:
#     print(client)

print('There are {}/{} users online'.format(host_info.virtual_servers_total_clients_online, host_info.virtual_servers_total_max_clients))

publish.single(mqtt_details['topic'], host_info.virtual_servers_total_clients_online, hostname=mqtt_details['host'],
               port=int(mqtt_details['port']),
               auth={'username': mqtt_details['username'], 'password': mqtt_details['password']})
