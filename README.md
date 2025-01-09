# M5 - S1 - Kiosque

Esse projeto foi feito como entrega avaliativa no módulo 5 do curso de desenvolvedor Full Stack na Kenzie Academy Brasil. Nele, é desenvolvida uma aplicação para simular um sistema de pedidos para um quiosque.

No projeto foi utilizado somente Python, interagindo com uma base de dados em memória (uma lista em Python).

Foram criadas funções para adicionar produtos, listar cada produto, listar produtos por seus tipos, realizar a contagem de produtos no menu por categoria, além de uma função que calcula o total do pedido com os produtos selecionados. 

## Como rodar os testes localmente

1. Instalar o pacote `pytest-testdox`:
```shell
pip install pytest-testdox
```

2. Rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```


### Rodando os testes localmente para o extra (não contabiliza para a entrega)

```shell
pytest --testdox -vvs tests/test_management/extra_add_product.py
```

