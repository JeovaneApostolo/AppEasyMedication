import mysql.connector

# Configurações de conexão do banco de dados
config = {
    'user': 'diegobezerra',
    'password': 'Fatec@2023!',
    'host': '3306',
    'database': 'diegobezerra_AplicativoParaIdosos'
}

# Estabelece a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão estabelecida com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")
    exit()

# Executa uma consulta SQL
try:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicamento")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Erro ao executar a consulta SQL: {err}")

# Fecha a conexão com o banco de dados
cursor.close()
conn.close()