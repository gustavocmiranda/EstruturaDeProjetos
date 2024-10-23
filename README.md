# Estruturação de Projetos de Dados: Pipeline de Concatenação de Arquivos

Este projeto tem como objetivo principal aprender a **estruturar projetos de dados** de forma organizada e eficiente, seguindo as melhores práticas da área. A pipeline desenvolvida é um exemplo prático, onde diversos arquivos de uma pasta são lidos, concatenados e gerados em um único arquivo de saída.

## Objetivos

- Aprender a estruturar projetos de dados com boas práticas de organização, testes e automação.
- Criar uma pipeline que lê arquivos de uma pasta, concatena os arquivos e retorna um único arquivo de saída.
- Aplicar ferramentas modernas para gerenciar dependências, automação de tarefas e conformidade com padrões de código.

## Tecnologias e Ferramentas

- **Python**: Linguagem principal do projeto.
- **Poetry**: Gerenciador de dependências e ambiente virtual, utilizado para garantir a consistência entre o desenvolvimento local e produção.
- **Taskipy**: Automação de tarefas recorrentes, como execução de testes e geração de documentação.
- **Sort** e **Blue**: Bibliotecas para garantir que o código siga os padrões de estilo **PEP8**.
- **MkDocs**: Utilizado para criar e manter a documentação do projeto, com deploy no **GitHub Pages**.
- **Pre-commits**: Automação para garantir que verificações e testes sejam executados antes de commits.
- **GitHub Actions**: Integração contínua para rodar testes e validações automaticamente a cada atualização do projeto.

## Funcionalidades

1. **Pipeline de Concatenação de Arquivos**:
   - Lê múltiplos arquivos de uma pasta, concatena todos eles em sequência e gera um arquivo consolidado.

2. **Estruturação e Organização**:
   - O foco do projeto está na correta **estruturação** e organização, utilizando práticas recomendadas de desenvolvimento.

3. **Ambiente Virtual com Poetry**:
   - **Poetry** gerencia as dependências e o ambiente virtual, facilitando o processo de instalação e configuração.

4. **Automação de Tarefas com Taskipy**:
   - **Taskipy** é utilizado para automatizar a execução de testes, formatação de código e outras tarefas recorrentes.

5. **Documentação com MkDocs**:
   - A documentação do projeto foi criada com **MkDocs**, acessível publicamente via GitHub Pages.
   - [Link para a documentação](https://gustavocmiranda.github.io/EstruturaDeProjetos/) (*O flowchart com Mermaid ainda não está funcionando.*)

6. **Pre-commits e GitHub Actions**:
   - Verificações automáticas são feitas em cada commit com **pre-commits**. Além disso, **GitHub Actions** são configuradas para rodar testes automatizados a cada pull request.

## Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/gustavocmiranda/EstruturaDeProjetos/
cd EstruturaDeProjetos
```

### 2. Instale as Dependências

Certifique-se de que o **Poetry** está instalado em sua máquina. Em seguida, execute:

```bash
poetry install
```

### 3. Ative o Ambiente Virtual

```bash
poetry shell
```

### 4. Execute as Tarefas

Para concatenar os arquivos de uma pasta, basta executar a tarefa principal:

```bash
poetry run task run
```


## Contribuições

Contribuições e sugestões são bem-vindas! Por favor, abra uma issue ou submeta um pull request. Certifique-se de rodar os testes e seguir as convenções de código antes de submeter suas mudanças.
