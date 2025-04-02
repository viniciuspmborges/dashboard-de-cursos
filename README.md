# Dashboard de Acompanhamento de Cursos Realizados

Este projeto é uma aplicação desenvolvida em Python utilizando as bibliotecas **Streamlit**, **Pandas** e **Plotly**. Ele permite criar um dashboard interativo para acompanhar os cursos realizados, fornecendo visualizações, filtros e exportação de dados.

## Funcionalidades

### 1. **Tabela de Cursos**
![image](https://github.com/user-attachments/assets/d5ab79f0-d9ff-49dc-bf94-ab0dff6d16ff)
- Exibe uma tabela interativa com os cursos realizados.
- Permite aplicar filtros por:
  - Intervalo de datas (início e conclusão).
  - Tipo de curso.
  - Instituição.
  - Área de conhecimento.
  - Status de envio.
- Exibe informações adicionais, como:
  - Total de cursos filtrados.
  - Carga horária total dos cursos.
- Possibilidade de exportar os dados filtrados para um arquivo `.txt`.

### 2. **Gráfico de Carga Horária por Área de Conhecimento**
![image](https://github.com/user-attachments/assets/e6274468-2fe6-4af7-a46c-921de1a0d7c0)
- Gera um gráfico de barras horizontal interativo.
- Mostra a carga horária total agrupada por área de conhecimento.
- Permite selecionar áreas específicas para análise.

### 3. **Gráfico de Cursos Concluídos**
![image](https://github.com/user-attachments/assets/73c776cb-6b82-4b32-860e-5ca673dab3c6)
![image](https://github.com/user-attachments/assets/74f25fb6-e837-418c-be10-da2c152d772a)

- Exibe gráficos interativos para acompanhar:
  - Número de cursos concluídos ao longo do tempo.
  - Carga horária total ao longo do tempo.
- Permite agrupar os dados por:
  - Diário.
  - Semanal.
  - Mensal.
- Inclui informações detalhadas sobre os cursos concluídos em cada período.

### 4. **Exportação de Arquivos**
![image](https://github.com/user-attachments/assets/9beea777-949c-41c9-b1c0-8a4160b4bef8)
- Filtra os cursos concluídos com base em um intervalo de datas.
- Exporta os certificados correspondentes para um diretório específico.
- Compacta os arquivos exportados em um arquivo `.zip` para facilitar o download.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Streamlit**: Framework para criação de interfaces web interativas.
- **Pandas**: Manipulação e análise de dados.
- **Plotly**: Criação de gráficos interativos.
- **OpenPyXL**: Leitura de arquivos Excel.
- **Shutil**: Manipulação de arquivos e diretórios.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.12 ou superior instalado.
- Dependências listadas no arquivo `requirements.txt`.

### Passos
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd dashboard-cursos
   ```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Execute a aplicação:
```bash
streamlit run dashboard.py
```

Acesse o dashboard no navegador pelo endereço:
```bash
http://localhost:8501
```

## Estrutura do Projeto
`dashboard.py`: Arquivo principal que implementa o dashboard.
`Cursos realizados.xlsx`: Arquivo Excel contendo os dados dos cursos realizados.
`Dockerfile`: Configuração para criar uma imagem Docker da aplicação.
`requirements.txt`: Lista de dependências do projeto.
`.github/workflows/azure-containerapp.yml`: Workflow para deploy automatizado no Azure Container Apps.

## Exemplos de Uso
- Acompanhar o progresso de cursos realizados em diferentes áreas de conhecimento.
- Gerar relatórios e gráficos para análise de carga horária e conclusão de cursos.
- Exportar certificados de cursos concluídos em um intervalo de datas.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
Este projeto está licenciado sob a MIT License.

## Contato
Para dúvidas ou sugestões, entre em contato com o desenvolvedor. 
