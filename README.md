# Cotações de moedas

Um pequeno projeto desenvolvido para atender as necessidades de um cliente que, se baseava em obter dados das cotações de valores de moedas.

## Funcionalidade

- Executar parametro **"GET"**, na API do site https://docs.awesomeapi.com.br/api-de-moedas

## Tecnologias utilizadas
- **Python**: Linguagem de programação principal.
- **Requests**: Biblioteca do Python
- **Json**: Biblioteca do Python
- **Matplotlib**: Biblioteca do Python

## Estrutura do projeto

- `main.py`: Arquivo de execução principal.
- `README.md`: Documentação do projeto.
- `requirements.txt`: Lista de dependências do projeto.

## Pré-requisitos

![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

- Python 3.12+

## Instalação

1. Clone este repositório
```
git clone https://github.com/Alexandre17araujo/cotacoes_moedas.git
cd cotacoes_moedas
```

## Crie e ative um ambiente virtual (opcional, mas recomendado):
```
	python3.12 -m venv venv
	source venv/bin/activate  # Linux
	venv\Scripts\activate     # Windows
```
## Instale as dependências
```
pip install -r requirements.txt
```

## Execute aplicação

![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

```	
    python3.12 main.py 
```

## Avisos
Você pode substituir qual o modelo de moeda deseja usar para realizar as cotações.
Atenção. Na API de **Retorna cotações sequenciais de um período específico**, só está retornando apenas os últimos 90 dias.


## Documentação

- [Python](https://docs.python.org/pt-br/3.12/library/index.html)
- [Matplotlib](https://matplotlib.org/stable/index.html)
- [Requests](https://requests.readthedocs.io/projects/pt/pt-br/latest/user/quickstart.html)
- [Json](https://docs.python.org/pt-br/3/library/json.html)