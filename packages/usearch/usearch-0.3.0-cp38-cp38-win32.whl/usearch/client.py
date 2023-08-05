import numpy as np
from ucall.client import Client


class IndexClient:

    def __init__(self, uri: str = '127.0.0.1', port: int = 8545, use_http: bool = True) -> None:
        self.client = Client(uri=uri, port=port, use_http=use_http)

    def add(self, labels: np.array, vectors: np.array):
        if isinstance(labels, int):
            return self.client.add_one(label=labels, vectors=vectors)
        else:
            return self.client.add_many(labels=labels, vectors=vectors)

    def search(self, vectors: np.array, count: int) -> tuple[np.array, np.array, np.array]:
        matches = []
        distances = []
        counts = []
        # return self.client.search_one(vectors=vectors, count=count)
        return matches, distances, counts

    def __len__(self):
        return self.client.size()

    @property
    def ndim(self):
        return self.client.ndim()

    def capacity(self):
        return self.client.capacity()

    def connectivity(self):
        return self.client.connectivity()
