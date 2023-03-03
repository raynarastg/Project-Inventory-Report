from inventory_report.inventory.product import Product

def test_cria_produto():
    values = Product(8,
                   'Aspirin',
                   'Galena Biopha',
                   '2021-02-22',
                   '2024-03-14',
                   'KZ63 800H NM4B ZOWB YYUI',
                   'instrucao 8')

    assert values.id == 8
    assert values.nome_do_produto == 'Aspirin'
    assert values.nome_da_empresa == 'Galena Biopha'
    assert values.data_de_fabricacao == '2021-02-22'
    assert values.data_de_validade == '2024-03-14'
    assert values.numero_de_serie == 'KZ63 800H NM4B ZOWB YYUI'
    assert values.instrucoes_de_armazenamento == 'instrucao 8'
