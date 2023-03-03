from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        response_simple_report = super().generate(inventory)
        empresa = Counter(item["nome_da_empresa"] for item in inventory)
        products = ''
        for key, value in empresa.items():
            products += f"- {key}: {value}\n"
        return (
            response_simple_report +
            "\n" +
            f"Produtos estocados por empresa:\n{products}"
        )
