from threading import Lock
import json
from typing import Any


global_appi_mutex = Lock()
volatile_documents = {}


class Transaction:
    def __init__(self, document, tsx, parent=None):
        self.__document = document
        self.__parent = parent
        self.__tsx = tsx

    def __update(self, tsx):
        self.__document["_vmt"] = self.__tsx
        self.__parent.__update(self.__tsx)

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__document[__name] = __value
        self.__update(self.tsx)

    def __getattr__(self, key):
        
        return self.get(key)


class Document():
    def __init__(self, name):
        self.name = name
        self.document = {}

    def __update(self, tsx):
        self.__document["_vmt"] = tsx

    def __getattr__(self, key):
        return Transaction(self.document).__getattr__(key)

    def __enter__(self):
        global_appi_mutex.acquire()

        try:
            with open(f'{self.name}.json') as document_handle:
                self.document = json.load(document_handle)
        except Exception as e:
            self.document = {}

        return self
    
    def __exit__(self, type, value, traceback):
        global_appi_mutex.release()




class VolatileDocument:
    def __init__(self, name):
        self.name = name
        self.document = {}

    def __getattr__(self, key):
        return self.get(key)

    def __enter__(self):
        global_appi_mutex.acquire()

        return self
    
    def __exit__(self, type, value, traceback):
        global_appi_mutex.release()