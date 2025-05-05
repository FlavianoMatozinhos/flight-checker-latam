# ✈️ LATAM Flight Finder

Este projeto consulta a **API da Amadeus** para buscar ofertas de voos, filtra os que são operados pela **LATAM Airlines**, exibe o voo mais barato e grava as informações em um banco de dados **MySQL**.

## 📦 Requisitos

- Python 3.7+
- Conta na [Amadeus Developer](https://developers.amadeus.com/)
- Banco de dados MySQL
- `.env` configurado com as credenciais

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/latam-flight-finder.git
cd latam-flight-finder
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ⚙️ Arquivo `.env`

Crie um arquivo `.env` com o seguinte conteúdo:

```env
AMADEUS_CLIENT_ID=xxx
AMADEUS_CLIENT_SECRET=xxx

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=123456
DB_NAME=voos_db
```

## 🚀 Executando o projeto

```bash
python main.py
```

## 🧱 Criar banco de dados

Execute o seguinte SQL no seu banco MySQL:

```sql
CREATE TABLE voos_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origem VARCHAR(10),
    destino VARCHAR(10),
    data_ida DATE,
    data_volta DATE,
    preco DECIMAL(10,2),
    moeda VARCHAR(10),
    carrierCode VARCHAR(10),
    flightNumber VARCHAR(10),
    departureIATA VARCHAR(10),
    departureTime DATETIME,
    arrivalIATA VARCHAR(10),
    arrivalTime DATETIME
);
```

