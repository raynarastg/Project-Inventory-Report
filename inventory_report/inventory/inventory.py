import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path) as pathCsv:
            if type == "simples":
                return SimpleReport.generate(list(csv.DictReader(pathCsv)))
            return CompleteReport.generate(list(csv.DictReader(pathCsv)))
