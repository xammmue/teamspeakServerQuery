from __future__ import annotations


class Client:
    def __init__(self, clid: int, cid: int, client_database_id: int, client_nickname: str, client_type: int):
        self.clid = clid
        self.cid = cid
        self.client_database_id = client_database_id
        self.client_nickname = client_nickname
        self.client_type = client_type

    @staticmethod
    def from_string(raw_client: str) -> Client:
        client_dict = {}
        properties = raw_client.split()
        for client_property in properties:
            [name, value] = client_property.split('=')
            client_dict[name] = value

        return Client._from_dict(client_dict)

    @staticmethod
    def _from_dict(client: dict[str, str]) -> Client:
        return Client(
            int(client['clid']),
            int(client['cid']),
            int(client['client_database_id']),
            client['client_nickname'],
            int(client['client_type'])
        )

    def __str__(self):
        return self.client_nickname