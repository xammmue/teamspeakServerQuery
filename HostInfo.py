from __future__ import annotations


class HostInfo:
    def __init__(
            self,
            instance_uptime: int,
            host_timestamp_utc: int,
            virtual_servers_running_total: int,
            virtual_servers_total_max_clients: int,
            virtual_servers_total_clients_online: int,
            virtual_servers_total_channels_online: int,
            connection_filetransfer_bandwidth_sent: int,
            connection_filetransfer_bandwidth_received: int,
            connection_filetransfer_bytes_sent_total: int,
            connection_filetransfer_bytes_received_total: int,
            connection_packets_sent_total: int,
            connection_bytes_sent_total: int,
            connection_packets_received_total: int,
            connection_bytes_received_total: int,
            connection_bandwidth_sent_last_second_total: int,
            connection_bandwidth_sent_last_minute_total: int,
            connection_bandwidth_received_last_second_total: int,
            connection_bandwidth_received_last_minute_total: int
    ):
        self.connection_bandwidth_received_last_minute_total = connection_bandwidth_received_last_minute_total
        self.connection_bandwidth_received_last_second_total = connection_bandwidth_received_last_second_total
        self.connection_bandwidth_sent_last_minute_total = connection_bandwidth_sent_last_minute_total
        self.connection_bandwidth_sent_last_second_total = connection_bandwidth_sent_last_second_total
        self.connection_bytes_received_total = connection_bytes_received_total
        self.connection_packets_received_total = connection_packets_received_total
        self.connection_bytes_sent_total = connection_bytes_sent_total
        self.connection_packets_sent_total = connection_packets_sent_total
        self.connection_filetransfer_bytes_received_total = connection_filetransfer_bytes_received_total
        self.connection_filetransfer_bytes_sent_total = connection_filetransfer_bytes_sent_total
        self.connection_filetransfer_bandwidth_received = connection_filetransfer_bandwidth_received
        self.connection_filetransfer_bandwidth_sent = connection_filetransfer_bandwidth_sent
        self.virtual_servers_total_channels_online = virtual_servers_total_channels_online
        self.virtual_servers_total_clients_online = virtual_servers_total_clients_online
        self.virtual_servers_total_max_clients = virtual_servers_total_max_clients
        self.virtual_servers_running_total = virtual_servers_running_total
        self.host_timestamp_utc = host_timestamp_utc
        self.instance_uptime = instance_uptime

    @staticmethod
    def from_string(host_info_str: str) -> HostInfo:
        host_info_properties = host_info_str.split()
        host_info = {}
        for host_info_property in host_info_properties:
            [name, value] = host_info_property.split('=')
            host_info[name] = value
        return HostInfo(
            instance_uptime = int(host_info['instance_uptime']),
            host_timestamp_utc = int(host_info['host_timestamp_utc']),
            virtual_servers_running_total = int(host_info['virtualservers_running_total']),
            virtual_servers_total_max_clients = int(host_info['virtualservers_total_maxclients']),
            virtual_servers_total_clients_online = int(host_info['virtualservers_total_clients_online']),
            virtual_servers_total_channels_online = int(host_info['virtualservers_total_channels_online']),
            connection_filetransfer_bandwidth_sent = int(host_info['connection_filetransfer_bandwidth_sent']),
            connection_filetransfer_bandwidth_received = int(host_info['connection_filetransfer_bandwidth_received']),
            connection_filetransfer_bytes_sent_total = int(host_info['connection_filetransfer_bytes_sent_total']),
            connection_filetransfer_bytes_received_total = int(host_info['connection_filetransfer_bytes_received_total']),
            connection_packets_sent_total = int(host_info['connection_packets_sent_total']),
            connection_bytes_sent_total = int(host_info['connection_bytes_sent_total']),
            connection_packets_received_total = int(host_info['connection_packets_received_total']),
            connection_bytes_received_total = int(host_info['connection_bytes_received_total']),
            connection_bandwidth_sent_last_second_total = int(host_info['connection_bandwidth_sent_last_second_total']),
            connection_bandwidth_sent_last_minute_total = int(host_info['connection_bandwidth_sent_last_minute_total']),
            connection_bandwidth_received_last_second_total = int(host_info['connection_bandwidth_received_last_second_total']),
            connection_bandwidth_received_last_minute_total = int(host_info['connection_bandwidth_received_last_minute_total']),
        )