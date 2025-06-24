# Consulta de CNPJ SEFAZ BA

Este projeto é uma API e interface web desenvolvida em **Python** com **FastAPI** para consultar a situação cadastral de um CNPJ na SEFAZ Bahia.  
A aplicação retorna a situação cadastral (ATIVO, INAPTO ou BAIXADO), exibe a razão social e apresenta o resultado de forma visual e amigável.

## Funcionalidades

- Consulta automática da situação cadastral do CNPJ na SEFAZ BA.
- Interface web simples, responsiva e colorida.
- Exibe a razão social do CNPJ consultado.
- Mensagens e cores diferentes para cada situação cadastral.
- Rodapé com contato do desenvolvedor (WhatsApp e Instagram).

## Como executar localmente

1. **Clone o repositório:**
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```
   Ou, se não houver o arquivo, instale manualmente:
   ```
   pip install fastapi uvicorn requests beautifulsoup4 jinja2 python-multipart
   ```

4. **Execute a aplicação:**
   ```
   uvicorn main:app --reload
   ```

5. **Acesse no navegador:**
   ```
   http://localhost:8000/consulta
   ```

## Estrutura do Projeto

```
.
├── main.py
├── templates
│   └── consulta.html
├── requirements.txt
└── README.md
```

## Contato

Desenvolvido por Michel Rebouças.  
[WhatsApp](https://web.whatsapp.com/send/?phone=5571987364775&text&type=phone_number&app_absent=0) | [Instagram](https://www.instagram.com/satosmichel_oficial/)

---

**Observação:**  
Este projeto é apenas para fins de estudo e demonstração.  
O uso em produção depende da disponibilidade e estabilidade do site da SEFAZ BA.