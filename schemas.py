from pydantic import BaseModel
from datetime import date
from typing import Optional

#classe padrão para as operações
class BolsaBase(BaseModel):
    nome: str
    vertente: Optional[str] = None
    salario: Optional[float] = None
    remunerado: Optional[bool] = None
    horas_semanais: Optional[int] = None
    quantidade_vagas: Optional[int] = None
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    professor_id: Optional[int] = None

class BolsaResponse(BaseModel):
    id: int
    nome: str
    vertente: Optional[str] = None
    salario: Optional[float] = None
    remunerado: Optional[bool] = None
    horas_semanais: Optional[int] = None
    quantidade_vagas: Optional[int] = None
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    professor_id: Optional[int] = None

class UpdateBolsa(BaseModel):
    nome: Optional[str] = None
    vertente: Optional[str] = None
    salario: Optional[float] = None
    remunerado: Optional[bool] = None
    horas_semanais: Optional[int] = None
    quantidade_vagas: Optional[int] = None
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    professor_id: Optional[int] = None

class CursoBase(BaseModel):
    nome: str
    categoria: Optional[str] = None
    preco: Optional[float] = None
    plataforma_id: Optional[int] = None
    nivel: Optional[str] = None
    vertente: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None

class CursoResponse(BaseModel):
    id: int
    nome: str
    categoria: Optional[str] = None
    preco: Optional[float] = None
    plataforma_id: Optional[int] = None
    nivel: Optional[str] = None
    vertente: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None

class UpdateCurso(BaseModel):
    nome: Optional[str] = None
    categoria: Optional[str] = None
    preco: Optional[float] = None
    plataforma_id: Optional[int] = None
    nivel: Optional[str] = None
    vertente: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class EmpresaBase(BaseModel):
    nome: str
    vertente: Optional[str] = None
    CNPJ: Optional[str] = None
    endereco_id: Optional[int] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    status: Optional[bool] = None

class EmpresaResponse(BaseModel):
    id: int
    nome: str
    vertente: Optional[str] = None
    CNPJ: Optional[str] = None
    endereco_id: Optional[int] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    status: Optional[bool] = None

class UpdateEmpresa(BaseModel):
    nome: Optional[str] = None
    vertente: Optional[str] = None
    CNPJ: Optional[str] = None
    endereco_id: Optional[int] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    status: Optional[bool] = None

class EnderecoBase(BaseModel):
    rua: str
    numero: Optional[int] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None

class EnderecoResponse(BaseModel):
    id: int
    rua: str
    numero: Optional[int] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None

class UpdateEndereco(BaseModel):
    rua: Optional[str] = None
    numero: Optional[int] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None

class EstagioBase(BaseModel):
    nome: str
    vertente: Optional[str] = None
    salario: Optional[float] = None
    empresa_id: Optional[int] = None
    remunerado: Optional[bool] = None
    horas_semanais: Optional[int] = None
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None

class EstagioResponse(BaseModel):
    id: int
    nome: str
    vertente: Optional[str] = None
    salario: Optional[float] = None
    empresa_id: Optional[int] = None
    remunerado: Optional[bool] = None
    horas_semanais: Optional[int] = None
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None

class UpdateEstagio(BaseModel):
    nome: Optional[str] = None
    vertente: Optional[str] = None
    salario: Optional[float] = None
    empresa_id: Optional[int] = None
    remunerado: Optional[bool] = None
    horas_semanais: Optional[int] = None
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None

class PlataformaBase(BaseModel):
    nome: str
    email: Optional[str] = None
    website: Optional[str] = None
    tipo: Optional[bool] = None

class PlataformaResponse(BaseModel):
    id: int
    nome: str
    email: Optional[str] = None
    website: Optional[str] = None
    tipo: Optional[bool] = None

class UpdatePlataforma(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    tipo: Optional[bool] = None


# Modelo base
class ProfessorBase(BaseModel):
    nome: str
    vertente: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    formacao: Optional[str] = None

# Modelo base para resposta (com todos os campos)
class ProfessorResponse(BaseModel):
    id: int
    nome: str
    vertente: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    formacao: Optional[str] = None

# Modelo para update (pode ter campos opcionais)
class UpdateProfessor(BaseModel):
    nome: Optional[str] = None
    vertente: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    formacao: Optional[str] = None
    












