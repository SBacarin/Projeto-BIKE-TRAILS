## FUNÇÕES
# Menu
def exibe_menu():
    os.system('cls') or None
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
            opcao = int(input('Escolha uma Opção: '))
            if opcao >= 0 and opcao <= 5:
                return opcao
            else:
                print("Opção inválido, favor digitar entre 1 e 5")
        except ValueError:
            print("Opção inválido, favor digitar entre 1 e 5")


# Inclusão [1]
def inclusao():
    # gravando dados em variáveis
    v_apelido                       = input('Informe como a trilha é mais conhecida(Apelido).:')
    v_descricao                     = input('Descreva o trajeto..............................:')
    v_km_total                      = input('Informe a kilometragem total....................:')
    v_tempo_mov                     = input('Informe o tempo de movimentação.................:')
    v_elevacao                      = input('Informe o grau de elevação......................:')
    v_grau_dif                      = input('Informe o grau de dificuldade...................:')
    data_padrao        = datetime.now().strftime('%d/%m/%Y')
    v_dt_ultima_realiz = obter_data_valida(f'Informe a data da última realização (DD/MM/AAAA): ', data_padrao)

    comando_inclusao = """INSERT INTO trilhas (apelido, descricao, km_total, tempo_mov, elevacao, grau_dif, dt_ultima_realiz) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    valores_gravar = (v_apelido, v_descricao, v_km_total, v_tempo_mov, v_elevacao, v_grau_dif, v_dt_ultima_realiz)
    
    while True:
            SN = input('Confirma a inclusão (S/N)?').upper()[0]
            if SN in "SN":
               break
            else:
                print('Erro! Por favor Digite apenas S ou N')
    
    if SN == 'S':
        ## inicia a conexão
        cursor = bd_conexao.cursor()
    
        ## inclue E GRAVA
        cursor.execute(comando_inclusao, valores_gravar)
        bd_conexao.commit()            

        ## fecha o cursor
        cursor.close()
        print("Ok Trilha inclusa com sucesso!!!")
        input()


# Consulta [2]
def consulta():
    busca_2 = int(input('Informe o código da trilha:'))
    comando_consulta = f'SELECT * FROM TRILHAS WHERE codigo = {busca_2}'
    
    ## inicia a conexão
    cursor = bd_conexao.cursor()
    
    ## executa a busca e grava na variável
    cursor.execute(comando_consulta)
    result = cursor.fetchone()
    
    if result is None or len(result) == 0:
        print("Trilha não cadastrada! Tecle <Enter> para continuar!")
        input()
    else:
        print(f"Apelido..................: {result[1]}")
        print(f"Descrição................: {result[2]}")
        print(f"Kilometragem total.......: {result[3]}")
        print(f"Tempo de movimentação....: {result[4]}")
        print(f"Elevação.................: {result[5]}")
        print(f"Grau de dificuldade......: {result[6]}")
        print(f"Data da última realização: {result[7]}")
        input("Tecle <Enter> para continuar!")

    ## fecha o cursor
    cursor.close()


# Alteração [3]
def alteracao():
    busca_3 = int(input('Informe o código da trilha que deseja alterar:'))
    comando_consulta = f'SELECT * FROM TRILHAS WHERE codigo = {busca_3}'

    ## inicia a conexão
    cursor = bd_conexao.cursor()
    
    ## executa a busca e grava na variável fetchone uma unica linha
    cursor.execute(comando_consulta)
    result_3 = cursor.fetchone()  
    
    if result_3 is None or len(result_3) == 0:
        print("Trilha não cadastrada! Tecle <Enter> para continuar!")
        input()
    else:
        print("Dados atuais da trilha:")
        print(f"Apelido..................: {result_3[1]}")
        print(f"Descrição................: {result_3[2]}")
        print(f"Kilometragem total.......: {result_3[3]}")
        print(f"Tempo de movimentação....: {result_3[4]}")
        print(f"Elevação.................: {result_3[5]}")
        print(f"Grau de dificuldade......: {result_3[6]}")
        print(f"Data da última realização: {result_3[7]}")

        # Pedir novos valores ao usuário
        v_apelido          = input(f'Novo Apelido ..............................: ') or result_3[1]
        v_descricao        = input(f'Nova Descrição ............................: ') or result_3[2]
        v_km_total         = input(f'Nova Kilometragem total ...................: ') or result_3[3]
        v_tempo_mov        = input(f'Novo Tempo de movimentação ................: ') or result_3[4]
        v_elevacao         = input(f'Nova Elevação .............................: ') or result_3[5]
        v_grau_dif         = input(f'Novo Grau de dificuldade ..................: ') or result_3[6]
        v_dt_ultima_realiz = input(f'Nova Data da última realização (DD/MM/YYYY): ') or result_3[7]

        ## Convertendo a data para o formato correto (YYYY-MM-DD)
        try:
           v_dt_ultima_realiz = datetime.strptime(v_dt_ultima_realiz, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            print("Formato de data inválido! Usando a data original.")
            v_dt_ultima_realiz = result_3[7]
        
        while True:
             SN = input('Confirma Alteração (S/N)?').upper()[0]
             if SN in "SN":
                break
             else:
                print('Erro! Por favor Digite apenas S ou N')
   
        if SN == 'S':
           comando_alteracao = f'''
                UPDATE TRILHAS SET
                apelido = '{v_apelido}',
                descricao = '{v_descricao}',
                km_total = '{v_km_total}',
                tempo_mov = '{v_tempo_mov}',
                elevacao = '{v_elevacao}',
                grau_dif = '{v_grau_dif}',
                dt_ultima_realiz = '{v_dt_ultima_realiz}'
                WHERE codigo = {busca_3} '''

           cursor.execute(comando_alteracao)
           bd_conexao.commit()         
           
           print("Ok Alteração Realizada!!!")
           input()


# Exclusão [4]
def exclusao():
    busca_4 = int(input('Informe o código da trilha que deseja excluir:'))
    comando_consulta = f'SELECT * FROM TRILHAS WHERE codigo = {busca_4}'
    comando_exclusao = f'DELETE FROM TRILHAS WHERE codigo = {busca_4}'
    
    ## inicia a conexão
    cursor = bd_conexao.cursor()
    
    ## executa a busca e grava na variável
    cursor.execute(comando_consulta)
    result_4 = cursor.fetchone()
    
    if result_4 is None or len(result_4) == 0:
        print("Trilha não cadastrada! Tecle <Enter> para continuar!")
        input()
    else:
        print(f"Apelido..................: {result_4[1]}")
        print(f"Descrição................: {result_4[2]}")
        print(f"Kilometragem total.......: {result_4[3]}")
        print(f"Tempo de movimentação....: {result_4[4]}")
        print(f"Elevação.................: {result_4[5]}")
        print(f"Grau de dificuldade......: {result_4[6]}")
        print(f"Data da última realização: {result_4[7]}")
        while True:
             SN = input('Tem certeza que deseja excluir a trilha (S/N)?').upper()[0]
             if SN in "SN":
                break
             else:
                print('Erro! Por favor Digite apenas S ou N')
             
        if SN == 'S':
            cursor.execute(comando_exclusao)
            bd_conexao.commit()  
            print("Ok Trilha removida!!!")
            input()
    
    ## fecha o cursor
    cursor.close()


# Função para validar a data
def obter_data_valida(prompt, data_padrao):
    while True:
        data_entrada = input(prompt)
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
    
    # importando classe para validar a data
    from datetime import datetime

    # Importando biblioteca para conexão com o banco de dados
    import mysql.connector

    # criando conexao ao banco de dados
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
   
    os.system('cls') or None ## limpa a tela
    while True:
        opcao_menu = exibe_menu()
        if opcao_menu == 1:
            inclusao()
        elif opcao_menu == 2:
            consulta()
        elif opcao_menu == 3:
            alteracao()
        elif opcao_menu == 4:
            exclusao()
        elif opcao_menu == 5:
            print('Encerrando!!!')
            break


 # Fechando a conexao
if bd_conexao.is_connected():
   bd_conexao.close()
   print("Conexão encerrada.")