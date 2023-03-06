from abc import ABC, abstractmethod
import csv
import json
import xml.etree.ElementTree as ET

class Importer(ABC):
    @abstractmethod
    def import_data(self, path, extension):
        file = path.split('.')[-1]
        if file != extension:
            raise ValueError('Arquivo inválido')
        with open(path) as pathReceived:
            if extension == 'csv':
                value = list(csv.DictReader(pathReceived))
            elif extension == 'json':
                value = json.load(pathReceived)
            elif extension == 'xml':
                valuesXml = ET.parse(pathReceived).getroot()
                value = [{x.tag: x.text for x in line} for line in valuesXml]
            return value
