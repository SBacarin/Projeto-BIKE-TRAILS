<h1> CRUD – PYTHON – MYSQL (BIKE TRAILS) </h1>

<p>Este projeto consiste em um software simples de cadastro de Trilhas de Bike (Bike Trails).</p>
<p>O mesmo contém os campos Apelido, Descrição do trajeto, Kilometragem total, Tempo de movimentação, Elevação, Grau de dificuldade e Data da última realização.</p>
<p>O objetivo é que o ciclista possa, em seus treinos ou lazer, pesquisar e não repetir a mesma trilha, além de ao iniciar uma nova, já ter o conhecimento de informações como a Kilometragem total, tempo , grau de dificuldade, etc.  É para uso pessoal e também para disponibilizar para amigos ciclistas.</p>

<h3>Ambiente de desenvolvimento</h3>
  <p>IDE - Visual Studio Code</p>
	<p>Linguagem - Python 3.12.3 </p>
	<p>Banco de Dados - MySQL Workbench 8.0 CE</p>

<h3>Instalação</h3>
<h4>Banco de Dados e Tabela </h4>
<p>1.	Instale o MySQL Workbench e configure com usuário e senha de sua preferência;</p>
<p>2.	Faça download aqui no GitHub do arquivo “ScriptCriaçãoBancoDadoseTabelas.sql”;</p>
<p>3.	Abra o MySql e execute o mesmo para a criação do Banco de Dados e Tabela;</p>
<h4>Software</h4>
<p>1.	Baixe e Instale Visual Studio Code e extensões Python;</p>
<p>2.	No terminal instale a biblioteca mysql.connector para conexão com o Banco de Dados </p>
<p>“pip install mysql.connector”</p>
<p>3.	Faça download do arquivo Bike Trails.py, localize a conexão com o banco de dados e altere com suas credenciais de conexão</p>
<p>   	“bd_conexao = mysql.connector.connect(</p>
<p>      		host='localhost',</p>
<p>        		user=’*****’,</p>
<p>       		password='*****',</p>
<p>        		database='bike_trails')”</p>

<h3>Execução</h3>
<p>Para execução abra o VsCode execute o script Bike Trails.py. Isso iniciará o aplicativo Python que permite incluir, consultar, alterar e excluir trilhas no banco de dados.</p>

<h3>Requisitos do Sistema</h3>
<p>Sistema Operacional Windows, MacOs ou Linux.</p>

<h3>Como contribuir</h3>
<p>1.	Faça um Fork do repositório clicando no botão “Fork” no topo da página;</p>
<p>2.	Em seguida clone o repositório para sua máquina local;</p>
<p>3.	Crie uma nova “Branch” para a sua contribuição;</p>
<p>4.	Efetue as mudanças e testes necessários;</p>
<p>5.	Faça “commit” das suas alterações com uma mensagem clara do que foi feito;</p>
<p>6.	Faça um “push” para o repositório Forked;</p>
<p>7.	Abra uma “pull request” no repositório original e descreva as mudanças feitas;</p>
<p>Contribuições são sempre bem vindas, agradeço.</p>

<h3>Práticas de código limpo</h3>
<p>1.	busquei sempre utilizar nomes nas variáveis (snake_case) que descrevam claramente o seu propósito;</p>
<p>2.	fiz inclusão de comentários explicativos para ajudar a entender o funcionamento do código;</p>
<p>3.	fiz a divisão do código em funções pequenas e específicas para facilitar a manutenção e testes;</p>
<p>4.	criei funções reutilizáveis;</p>
<p>5.	a conexão com o banco de dados sempre que aberta possui posteriormente um fechamento, garantindo a segurança;</p>

<h3>Testes Automatizados</h3>
<p>Para a criação de testes automatizados é preciso:</p>
<p>1.	Importar a extensão do Python “Test Explorer para VsCode” que automatiza testes;</p>
<p>2.	Criar uma cópia do Banco de dados para os testes;</p>
<p>3.	Criar um script para executar estes testes; </p>


