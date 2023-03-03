from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        old_data = min([date['data_de_fabricacao'] for date in inventory])
        expiration_date = min([date["data_de_validade"] for date in inventory
                              if (date["data_de_validade"] > datetime.now()
                               .strftime('%Y-%m-%d'))])
        empresa = Counter(name['nome_da_empresa'] for name in inventory)
        return (
            f"Data de fabricação mais antiga: {old_data}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {empresa.most_common()[0][0]}"
        )
