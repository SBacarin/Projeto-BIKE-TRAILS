# Criação do Menu
def exibe_menu():
    print('-' * 21)
    print('**** BIKE TRAILS ****')
    print('-' * 21)
    print('[1] Inclusão')
    print('[2] Consulta')
    print('[3] Alteração')
    print('[4] Exclusão')
    print('[5] SAIR')
    print('-' * 21)
    while True:
        try:
            opcao = int(input('Escolha uma Opção:'))
            if opcao >= 0 and opcao <= 5:
                return opcao
            else:
                print("Opção inválido, favor digitar entre 1 e 5")
        except ValueError:
            print("Opção inválido, favor digitar entre 1 e 5")

# [1] Inclusão
def inclusao():
    ##os.system('cls') or None
    # gravando dados em variáveis
    v_apelido = input('Informe como a trilha é mais conhecida(Apelido):')
    v_descricao = input('Descreva o trajeto:')
    v_km_total = input('Informe a kilometragem total:')
    v_tempo_mov = input('Informe o tempo de movimentação:')
    v_elevacao = input('Informe o grau de elevação:')
    v_grau_dif = input('Informe o grau de dificuldade:')
    data_padrao = datetime.now().strftime('%d/%m/%Y')
    v_dt_ultima_realiz = obter_data_valida(f'Informe a data da última realização (DD/MM/AAAA) [padrão: {data_padrao}]: ', data_padrao)

    comando_inclusao = """INSERT INTO trilhas (apelido, descricao, km_total, tempo_mov, elevacao, grau_dif, dt_ultima_realiz)  VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    valores = (v_apelido, v_descricao, v_km_total, v_tempo_mov, v_elevacao, v_grau_dif, v_dt_ultima_realiz)
    
    while True:
            SN = input(
                'Confirma a inclusão (S/N)?').upper()[0]
            if SN in "SN":
               break
            else:
                print('Erro! Por favor Digite apenas S ou N')
    
    if SN == 'S':
        ## inicia a conexão
        cursor = bd_conexao.cursor()
    
        ## inclue E GRAVA
        cursor.execute(comando_inclusao, valores)
        bd_conexao.commit()            

        ## fecha o cursor
        cursor.close()
        print("Ok Trilha inclusa com sucesso!!!")

  
# [2] Consulta
def consulta():
    print('consulta')

# [3] Alteração
def alteracao():
     print('alteracao')

# [4] Exclusão 
def exclusao():
     print('exclusao')


## FUNÇOES COMPLEMENTARES
# Função para obter uma data válida diretamente no input
def obter_data_valida(prompt, data_padrao):
    while True:
        data_entrada = input(prompt)
        if not data_entrada:  # Se o usuário não inserir nada, usar a data padrão
            return data_padrao
        try:
            # Tentar converter a entrada para um objeto datetime
            data_valida = datetime.strptime(data_entrada, '%d/%m/%Y')
            return data_valida
        except ValueError:
            # Informar ao usuário que a entrada é inválida e pedir novamente
            print("Data inválida. Por favor, insira no formato DD/MM/AAAA.")


## INICIO 
if __name__ == "__main__":
    # Importando o método para limpar a tela
    import os
    os.system('cls') or None
    
    from datetime import datetime

    # Impotando biblioteca para conexão com o banco de dados
    import mysql.connector

    # Conectando ao banco de dados
    bd_conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ted1975',
        database='bike_trails'
    )

    # Verificando a conexão
    if bd_conexao.is_connected():
        print("Conexão bem-sucedida!")
    else:
        print("Falha na conexão.")
   
    while True:
        op = exibe_menu()
        if op == 1:
            inclusao()
        elif op == 2:
            consulta()
        elif op == 3:
            alteracao()
        elif op == 4:
            exclusao()
        elif op == 5:
            print('Encerrando!!!')
            break


 # Fechando a conexao
if bd_conexao.is_connected():
   bd_conexao.close()
   print("Conexão encerrada.")