from inventory_report.inventory.product import Product


def test_relatorio_produto():
    params_value = Product(
        8,
        'Aspirin',
        'Galena Biopha',
        '2021-02-22',
        '2024-03-14',
        'KZ63 800H NM4B ZOWB YYUI',
        'instrucao 8').__repr__()
    assert params_value == (
            "O produto Aspirin fabricado em 2021-02-22 por "
            "Galena Biopha com validade até 2024-03-14 "
            "precisa ser armazenado instrucao 8."
        )
