# Template para Aplicações Streamlit

Este é o template para aplicações Streamlit.

## Passos:

### Crie um novo repositório utilizando este como template.
1) Na página inicial do GitHub, clique em "New"
![image](https://github.com/user-attachments/assets/ad12f0f5-68f0-4e9a-81f2-2306bc930994)

---

2) No campo "Repository Template", escolha a opção "tesouro/template-streamlit" e marque a caixa "Include all branches".
![image](https://github.com/user-attachments/assets/bd788613-161d-4e26-9ebe-4891e0b7e87b)

---

3) Dê um nome para o seu repositório e clique em "Create Repository".
![image](https://github.com/user-attachments/assets/a529cc0b-01ec-4fb2-addb-d672aa0cb30d)

---

### Adicione a seguinte variável de ambiente ao seu novo repositório: `PROJECT_NAME`.
1) Dentro do seu projeto, vá em "Settings"
![image](https://github.com/user-attachments/assets/dc6af511-5e49-4fb8-bf74-c3994d90dd92)

---

2) Clique em "Secrets and variables" > "Actions" e "New repository variable"
![image](https://github.com/user-attachments/assets/f498c540-00c5-4ae3-bbdb-811b3ff1c1dc)

---

3) Na caixa "Name", escreva "PROJECT_NAME" e, na caixa "Value", escreva o nome do seu projeto (no caso, "dashboard-coint")
![image](https://github.com/user-attachments/assets/35d89e4c-be5b-4558-a2ee-4cb7e497c1b2)

---

### Para testar, implemente na branch `develop`.
1) Na página inicial do projeto, clique no botão da branch atual (no caso, "main")
![image](https://github.com/user-attachments/assets/e7c67d13-8db7-4c05-bf9e-956e271194e3)

---

2) Na busca, escreva "develop" e clique no botão "Create branch develop from main"
![image](https://github.com/user-attachments/assets/43eb71ff-b4c3-42c7-b804-c5e3f7d43f7e)

---

3) Você estará na branch "develop". Clique no botão "Deployments" para ver a implantação em andamento.
![image](https://github.com/user-attachments/assets/8938ad85-5a0a-41e2-9d0a-21b0fa0c8349)

---

### Para implantar em produção, faça um pull-request para `main`.
1) Clique na aba "Pull requests" e, em seguida, no botão "New pull request"
![image](https://github.com/user-attachments/assets/5929a8fb-6e40-4ab0-9459-09cf5345785f)

2) Selecione as opções "base: main > compare: develop" e clique em "Create pull request"
![image](https://github.com/user-attachments/assets/2c1c3bfc-73b6-4f00-b6bc-93255bf3a1ff)


3) Adicione um título e uma descrição, e clique em "Create pull request"
![image](https://github.com/user-attachments/assets/653cb22f-9712-4471-bde1-b01b0f362984)

### Para obter o link da aplicação, verifique nos logs da Job "deploy-prod" ou "deploy-develop"
1) Clique na implantação desejada na aba "Deployments"
![image](https://github.com/user-attachments/assets/8938ad85-5a0a-41e2-9d0a-21b0fa0c8349)

2) No seu commit, clique no botão "..." e, em seguida, "View logs"
![image](https://github.com/user-attachments/assets/a149eeec-a678-4bd1-bc25-e1a121c8c063)

3) Dentro de "Build and Deploy container app em Dev", procure por "Container app created. Access your app at"
![image](https://github.com/user-attachments/assets/3fc09ecf-3829-47ac-8923-9ae4eca53b58)

## Detalhes sobre os arquivos

### main.py
Este é o arquivo principal do aplicativo Streamlit. Ele configura uma interface de chatbot usando a biblioteca Streamlit e a API da OpenAI. Aqui estão alguns pontos importantes:
- Importa as bibliotecas openai e streamlit.
- Configura uma barra lateral para inserir a chave da API da OpenAI.
- Exibe o título e a legenda do chatbot.
- Gerencia o estado da sessão para armazenar mensagens.
- Envia mensagens do usuário para a API da OpenAI e exibe as respostas do chatbot.

### Dockerfile
Este arquivo define como criar uma imagem Docker para o seu aplicativo. Aqui estão os passos principais:
- Usa a imagem oficial do Python como base.
- Define o diretório de trabalho no contêiner.
- Copia o conteúdo do diretório atual para o contêiner.
- Instala as dependências listadas em requirements.txt.
- Expõe a porta 8501 para o Streamlit.
- Define o comando para iniciar o aplicativo Streamlit.

### azure-containerapp.yml
Este arquivo define um workflow do GitHub Actions para construir e implantar seu aplicativo em um Azure Container App. Aqui estão os pontos principais:
- O workflow é acionado em push para as branches `main` e `develop`, ou manualmente.
- Define dois jobs: `deploy-develop` e `deploy-prod`, para implantações em desenvolvimento e produção, respectivamente.
- Cada job faz login no Azure, constrói a imagem do contêiner e a implanta no Azure Container App.
- Utiliza variáveis e segredos do GitHub para configurar a implantação.

### requirements.txt
- Este arquivo lista as dependências do Python necessárias para o seu aplicativo.

### README.md
Este arquivo fornece informações sobre o projeto, incluindo instruções de configuração e implantação. Ele inclui:
- Descrição do projeto.
- Passos para criar um novo repositório a partir do template.
- Instruções para adicionar variáveis de ambiente.
- Passos para testar e implantar o aplicativo.
- Instruções para obter o link da aplicação nos logs de implantação.

## Quando procurar a COSIS
1. Se precisar utilizar algum recurso dos nossos sistemas internos;
2. Se precisar de controle de acesso;
3. Caso não consiga obter o link em que sua aplicação está rodando.
