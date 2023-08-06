"""RPC server that works as broker in the SHV network."""
import asyncio

from .rpcclient import RpcClient


class RpcBroker:
    """RPC broker functionality.

    The broker manages multiple RpcClient instances and exchanges messages
    between them.
    """

    class Client:
        """Internal info about broker client."""

        def __init__(self, client: RpcClient):
            self.client = client
            self.options: dict = {}

    def __init__(self):
        self.clients = []

    def add_client(self, client: RpcClient):
        """Add a new client to be handled by the broker.

        :param client: RPC client instance to be handled by broker.
        """
        c = self.Client(client)
        self.clients.append(c)
        asyncio.create_task(self._client_loop(c))

    async def _client_loop(self, client: Client):
        """Loop handling a single client."""
        while msg := client.client.read_rpc_message():
            pass
