import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        file = path.split('.')[-1]
        with open(path) as pathReceived:
            if file == 'csv':
                value = list(csv.DictReader(pathReceived))
            elif file == 'json':
                value = json.load(pathReceived)
            if type == "simples":
                return SimpleReport.generate(value)
            return CompleteReport.generate(value)
# ref :
#  https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
