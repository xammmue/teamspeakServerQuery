import telnetlib3
import asyncio

from Client import Client
from HostInfo import HostInfo


class ServerQuery:
    def __init__(self, host: str, port: int, username: str, password: str, server_id: int):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.server_id = server_id
        self.reader = None
        self.writer = None

    async def read_until_available(self, timeout=0.1) -> list:
        total_text = []
        while True:
            try:
                data = await asyncio.wait_for(self.reader.readuntil(separator=b'\n'), timeout)
                if data:
                    total_text.append(data.decode())
                else:
                    return total_text
            except asyncio.TimeoutError:
                return total_text

    async def execute_command(self, command: str):
        self.writer.write(command)
        await self.writer.drain()

    async def execute_commands(self, command_list: list) -> dict:
        results = {}
        for command in command_list:
            await self.execute_command('{}\r\n'.format(command))
            result = None
            if 'quit' != command:
                result = await self.read_until_available()
            if 'login' in command:
                command_name = 'login'
            else:
                command_name = command
            results[command_name] = result
        self.writer.close()
        return results

    async def query(self, query: str) -> dict:
        self.reader, self.writer = await telnetlib3.open_connection(self.host, self.port)

        command_list = [
            'login {} {}'.format(self.username, self.password),
            'use {}'.format(self.server_id),
            query,
            'quit'
        ]
        results = await self.execute_commands(command_list)

        self.reader = None
        self.writer = None
        return results

    def run_async_query(self, query: str) -> dict:
        return asyncio.run(self.query(query))

    def load_host_info(self) -> HostInfo:
        results = self.run_async_query('hostinfo')
        host_info = HostInfo.from_string(results['hostinfo'][0])
        return host_info

    def load_client_list(self) -> list[Client]:
        results = self.run_async_query('clientlist')
        raw_client_list = results['clientlist'][0:-1]
        # clid=24 cid=5 client_database_id=1825 client_nickname=Incredible_Max1 client_type=1
        # clid=23 cid=5 client_database_id=1825 client_nickname=Incredible_Max client_type=0

        client_list = []

        for client in raw_client_list:
            cleaned_list = client.replace('\r', '').replace('\n', '')
            for split_client in cleaned_list.split('|'):
                client = Client.from_string(split_client)
                client_list.append(client)
        return client_list
