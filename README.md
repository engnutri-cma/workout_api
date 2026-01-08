
# Workout API - FastAPI Backend

API completa para gerenciamento de academia com CRUD completo para Atletas, Categorias, Centros de Treinamento e Workouts. Desenvolvida durante Bootcamp Backend Python DIO com estrutura profissional modular.


## Funcionalidades 

- CRUD Completo todos recursos  
- Validação Pydantic schemas  
- Documentação automática Swagger UI (/docs)  
- Windows Native (PYTHONPATH fix)  
- Estrutura modular enterprise  
- Ready para Deploy Render/Vercel



## Tecnologias

- FastAPI  # Framework API
- Pydantic # Validação dados
- Uvicorn  # ASGI Server
- Python 3.9+

## Como Executar (Windows)

1. Clone & Ambiente

2. PYTHONPATH Windows (Ajuste Crítico)

`
#FIX exclusivo Windows - módulo interno não resolve
$env:PYTHONPATH="$env:PYTHONPATH;."`

3. Rode API

`uvicorn workout_api.main:app --reload`

4. Swagger Docs
`
text
http://localhost:8000/docs`

## Aprendizado Bootcamp

- FastAPI estrutura profissional
- Pydantic schemas avançados
- Windows deployment (extra)
- Git workflow enterprise
- API documentation automática

Desafio superado: Transformei projeto Linux-centrado em Windows-native estudando sys.path, PowerShell $env, e FastAPI importlib!

## Contribuições

Windows PYTHONPATH fix

Estrutura modular limpa

### Feito com ❤️ durante Bootcamp Backend em Python - DIO LuizaLabs
Python Developer | FastAPI 
