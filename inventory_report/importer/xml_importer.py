from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        return Importer.import_data(self, path, 'xml')
