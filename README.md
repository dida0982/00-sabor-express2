# 🍽️ API de Restaurantes

<img width="760" height="595" alt="Screenshot 2026-07-13 203201" src="https://github.com/user-attachments/assets/1e258ebe-1923-4097-b316-f5bbe2877bf7" />


<img width="1919" height="1034" alt="Screenshot 2026-07-13 202958" src="https://github.com/user-attachments/assets/a056cce8-98dd-4313-9c19-933d51de9c47" />


API REST desenvolvida com **FastAPI** para consulta de dados de restaurantes e seus respectivos cardápios, consumindo uma base de dados externa e disponibilizando endpoints organizados para consulta geral ou filtrada por restaurante.

## ✅ Funcionalidades

- ✅ Endpoint de status/boas-vindas da API
- ✅ Listagem completa de todos os restaurantes e itens de cardápio
- ✅ Filtro de cardápio por nome de restaurante específico
- ✅ Consumo de dados via requisição HTTP a uma API externa
- ✅ Tratamento de erros de requisição (status code diferente de 200)
- ✅ Script auxiliar para exportação dos dados em arquivos `.json` individuais por restaurante

## 🚀 Tecnologias utilizadas

- Python 3.13
- FastAPI
- Requests
- JSON

## 📂 Estrutura do projeto

```
├── main.py     # Aplicação FastAPI com os endpoints da API
├── app.py      # Script para consumir a API externa e gerar arquivos .json por restaurante
```

## 📌 Endpoints

### `GET /api/hello`
Retorna uma mensagem simples de boas-vindas.

**Resposta:**
```json
{ "message": "Hello, World!" }
```

### `GET /api/restaurants/`
Retorna o cardápio de um restaurante específico ou de todos, caso nenhum parâmetro seja informado.

**Parâmetro (opcional):**
- `restaurant` — nome do restaurante para filtrar o cardápio

**Exemplo sem filtro:**
```
GET /api/restaurants/
```

**Exemplo com filtro:**
```
GET /api/restaurants/?restaurant=Nome do Restaurante
```

**Resposta:**
```json
{
  "Restaurant": "Nome do Restaurante",
  "Menu": [
    {
      "item": "Nome do item",
      "price": "Preço",
      "description": "Descrição do item"
    }
  ]
}
```

## ▶️ Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/dida0982/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Instale as dependências:
```bash
pip install fastapi uvicorn requests
```

3. Execute a aplicação:
```bash
uvicorn main:app --reload
```

4. Acesse a documentação interativa (Swagger) em:
```
http://localhost:8000/docs
```

## 🧠 Aprendizados técnicos

Este projeto reforça conceitos importantes de desenvolvimento back-end com Python, como a criação de rotas REST com FastAPI, o consumo de APIs externas via `requests`, o tratamento de respostas HTTP e a manipulação de dados em formato JSON para consultas dinâmicas e exportação em arquivos.

## 🔗 Contato e redes

- 💼 [LinkedIn](https://www.linkedin.com/in/guilherme-barros-6a0369209/)
- 💻 [GitHub](https://github.com/dida0982)
- 📸 [Instagram](https://www.instagram.com/guilherme_barros_jr/)
- 🌐 [Portfólio](https://developerguilhermebarros.netlify.app/)

#Python #FastAPI #API #BackEnd #DesenvolvimentoDeSoftware #Programação

**Instrutores:**

**Guilherme Lima**

<img src="https://media.licdn.com/dms/image/v2/D4E03AQFodSTnO1qe9w/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1727180159904?e=1784764800&v=beta&t=r83QSJOEmBXirzSl8Ta2Jjw_9f_yPYTL8kmpj0xfiwE" width="150" alt="Foto de perfil">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-lima-developer/)

**Laís Urano**

<img src="https://github.com/uranolais.png" width="150" alt="Foto de perfil">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/la%C3%ADs-urano-9a41451b3/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/uranolais)

## 👤 Autor

**Guilherme Barros**

<img src="https://github.com/dida0982.png" width="150" alt="Foto de perfil">

Desenvolvedor Full Stack | Brasília, DF - Brasil

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-barros-6a0369209/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dida0982)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/guilherme_barros_jr/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://developerguilhermebarros.netlify.app/)

---

<p align="center">⭐ Se este projeto te ajudou de alguma forma, deixe uma estrela no repositório!</p>

**Certificado Alura**

<img width="760" height="595" alt="Screenshot 2026-07-13 203201" src="https://github.com/user-attachments/assets/bb6828f6-769b-4d3c-9423-3c11b6957830" />

**Plataforma  Alura**

<img width="1898" height="907" alt="Screenshot 2026-07-13 202720" src="https://github.com/user-attachments/assets/ba50ec0e-3e6b-4c23-b5fa-de637c08a371" />

**Vídeo Aula**

<img width="1900" height="894" alt="Screenshot 2026-07-13 202814" src="https://github.com/user-attachments/assets/093bf7da-f241-48d7-beee-2a7dfdba7d43" />

**Projeto**

<img width="1919" height="1034" alt="Screenshot 2026-07-13 202958" src="https://github.com/user-attachments/assets/91b3de30-1f41-496d-b176-fa778117a45e" />

