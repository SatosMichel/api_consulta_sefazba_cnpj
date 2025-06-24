import re
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/consulta")

@app.get("/consulta", response_class=HTMLResponse)
def form_cnpj(request: Request):
    return templates.TemplateResponse("consulta.html", {
        "request": request,
        "mensagem": None,
        "cor_fundo": "#e8f5e9",  # verde claro
        "cor_texto": "#2ecc40"
    })

@app.post("/consulta", response_class=HTMLResponse)
def resultado_cnpj(request: Request, cnpj: str = Form(...)):
    url_result = "https://portal.sefaz.ba.gov.br/scripts/cadastro/cadastroBa/result.asp"
    cnpj_limpo = re.sub(r'\D', '', cnpj)
    payload = {
        "sefp": "1",
        "estado": "BA",
        "CGC": cnpj_limpo,
        "B1": "CNPJ  ->"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url_result, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrair Situação Cadastral Vigente
    status = None
    for b in soup.find_all('b'):
        if 'Situação Cadastral Vigente' in b.get_text():
            if b.next_sibling:
                status = str(b.next_sibling).strip()
            elif b.parent is not None:
                status = b.parent.get_text().replace('Situação Cadastral Vigente:', '').strip()
            else:
                status = None
            break

    # Extrair Razão Social
    razao_social = None
    for b in soup.find_all('b'):
        if 'Razão Social' in b.get_text():
            if b.next_sibling:
                razao_social = str(b.next_sibling).strip()
            elif b.parent is not None:
                razao_social = b.parent.get_text().replace('Razão Social:', '').strip()
            else:
                razao_social = None
            break

    if status and "ATIVO" in status.upper():
        mensagem = "CNPJ ATIVO NA SEFAZ. APTO PARA EMISSÃO DE NFe."
        cor_fundo = "#e8f5e9"  # verde claro
        cor_texto = "#2ecc40"
    elif status and "INAPTO" in status.upper():
        mensagem = "CNPJ INAPTO NA SEFAZ, IMPOSSÍVEL EMISSÃO DE NFe PARA ESSE CLIENTE"
        cor_fundo = "#ffebee"  # vermelho claro
        cor_texto = "#c0392b"
    elif status and "BAIXADO" in status.upper():
        mensagem = "CNPJ ATIVO, PODEMOS EMITIR NFe PARA O CLIENTE MAS ELE É ISENTO DE INSCRIÇÃO ESTADUAL."
        cor_fundo = "#e0f7fa"  # tom neutro/azul claro
        cor_texto = "#00796b"
    else:
        mensagem = f"Situação cadastral: {status or 'Não encontrada'}"
        cor_fundo = "#fffde7"  # amarelo claro
        cor_texto = "#f39c12"

    return templates.TemplateResponse("consulta.html", {
        "request": request,
        "mensagem": mensagem,
        "razao_social": razao_social,
        "cor_fundo": cor_fundo,
        "cor_texto": cor_texto
    })