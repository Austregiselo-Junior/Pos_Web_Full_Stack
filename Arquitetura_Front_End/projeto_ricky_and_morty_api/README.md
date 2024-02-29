# RICK AND MORTY API

![alt imagem de capa](./.github/wallpaper.png)

Criação de um projeto de conclusão frontend do curso Pós Graduação em Desenvolvimento Web Fullstack pelo UNIPÊ.

# Objetivo

O objetivo desse desafio é medir o conhecimento do aluno em relação ao desenvolvimento de aplicativos Web com foco no front-end.

## Stack utilizada

### FRONT-END

- [TypeScript](https://www.typescriptlang.org/)
- [Vite.js](https://vitejs.dev/)
- [Axios](https://axios-http.com/)
- [React Router](https://reactrouter.com/en/main)

## Documentação da API

#### API utilizada:

```http
  https://rickandmortyapi.com/
```

## Deploy

Para fazer o deploy desse projeto rode

```bash
  npm run dev
```

## Requisitos do projeto

O desafio deverá conter um cabeçalho com um menu para a lista de Personagens, Episódios e Localização

#### Página de lista de personagens

**Cada card de personagem deve exibir:**

- Nome do personagem;
- Foto do personagem;
- Status do personagem;
- Espécie do personagem;
- Localização do personagem;
- schema: https://rickandmortyapi.com/documentation/#character-schema.

**Comportamento esperado:**

<p>Ao clicar em um card na listagem de personagens o usuário deve ser redirecionado para a página de detalhamento do persoagem clicado.</p>

#### Página de detalhamento do personagem

**Deve ser exibida as seguintes informações na página detalhamento:**

- Nome do personagem;
- Foto do personagem;
- Status do personagem;
- Espécie do personagem;
- Origem do personagem;
- Localização do personagem;
- lista com o nome dos episódios no qual o personagem aparece.
- schema: https://rickandmortyapi.com/documentation/#character-schema

**Comportamento esperado:**

<p>Ao clicar em qualquer item da lista episódios usuário deve ser redirecionado para a página de detalhamento do episódio clicado.</p>

#### Página de lista de episódios

**Cada card de episódios deve exibir:**

- Nome do Episódio
- Data de estreia
- schema:https://rickandmortyapi.com/documentation/#episode-schema

**Comportamento esperado:**

<p>Ao clicar em um card na listagem de espisódios o usuário deve ser redirecionado para a página de detalhamento do episódio clicado.</p>

#### Página de Detalhamento do episódio

**Deve ser exibida as seguintes informações no detalhamento de cada episódio:**

- Nome do Episódio;
- Data de estreia;
- Lista de personagens que estão no episódio;
- Para cada item da Lista de personagem deve ter nome, foto e link para o detalhamento do personagem.
- schema: https://rickandmortyapi.com/documentation/#episode-schema

**Comportamento esperado:**

<p>Ao clicar em qualquer item da lista personagens usuário deve ser redirecionado para a página de detalhamento do personagem clicado.</p>

#### Página de lista de localização

**Cada card de localização deve exibir:**

- Nome da localização
- Tipo da localização
- Dimensão da Localização
- schema: https://rickandmortyapi.com/documentation/#location-schema

**Comportamento esperado:**

<p>Ao clicar em um card na listagem de localização o usuário deve ser redirecionado para a página de detalhamento da localização clicada.</p>

#### Página de Detalhamento da localização

**Deve ser exibida as seguintes informações no detalhamento de cada localização:**

- Nome da localização
- Tipo da localização
- Dimensão da Localização
- Lista de personagens que residem nessa localização
- Para cada item da lista de personagem deve ter nome, foto e link para o detalhamento do personagem.
- schema: https://rickandmortyapi.com/documentation/#location-schema
**Comportamento esperado:**
<p>Ao clicar em qualquer item da lista personagens usuário deve ser redirecionado para a página de detalhamento do personagem clicado.</p>

## Autores e colaboradores

- [@neliofrazao](https://github.com/neliofrazao)
- [@Austregiselo-Junior](https://github.com/Austregiselo-Junior)
