from abc import ABC, abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def test_connection(self):
        pass

    @abstractmethod
    def create_nodes(self, count):
        pass

    @abstractmethod
    def point_lookup(self):
        pass

    @abstractmethod
    def aggregation_query(self):
        pass

    @abstractmethod
    def hop1_query(self):
        pass

    @abstractmethod
    def hop2_query(self):
        pass

    @abstractmethod
    def hop3_query(self):
        pass

    @abstractmethod
    def update_nodes(self):
        pass

    @abstractmethod
    def shortest_path(self):
        pass