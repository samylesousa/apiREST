from fastapi import FastAPI, HTTPException, status
from database_config import get_session
from models import Empresa, Curso, Estagio, Bolsa, Professor, Plataforma, Endereco
from sqlalchemy.future import select
from datetime import datetime
import os
from schemas import (
    BolsaBase, 
    BolsaResponse,
    UpdateBolsa,
    EstagioBase,
    EstagioResponse,
    UpdateEstagio, 
    ProfessorBase,
    ProfessorResponse,
    UpdateProfessor,
    CursoBase, 
    CursoResponse,
    UpdateCurso,
    PlataformaBase,
    PlataformaResponse,
    UpdatePlataforma, 
    EnderecoBase,
    EnderecoResponse,
    UpdateEndereco, 
    EmpresaBase,
    EmpresaResponse,
    UpdateEmpresa,
)
app = FastAPI()
print(f"API REST rodando com PID: {os.getpid()}")


async def delete_element(elemento_id: int, model_class):
    async with get_session() as session:
        try:
            resultado = await session.get(model_class, elemento_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item não encontrado"
                )

            await session.delete(resultado)
            await session.commit()

            return None
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao deletar item: {str(e)}"
            )


@app.get("/bolsas", status_code=status.HTTP_200_OK)
async def get_bolsas():
    async with get_session() as session:
        try:
            resultado = await session.execute(select(Bolsa))
            item = resultado.scalars().all()

            return [BolsaResponse(
                id=row.id,
                nome=row.nome,
                vertente=row.vertente,
                salario=row.salario,
                professor_id=row.professor_id,
                horas_semanais=row.horas_semanais,
                remunerado=row.remunerado,
                quantidade_vagas=row.quantidade_vagas,
                data_inicio=row.data_inicio,
                data_fim=row.data_fim,
                descricao=row.descricao
                ) for row in item]

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"As bolsas não foram encontradas: {str(e)}"
            )

@app.get("/bolsas/{bolsa_id}", status_code=status.HTTP_200_OK)
async def get_bolsa_id(bolsa_id: int):
    async with get_session() as session:
        try:
            resultado = await session.get(Bolsa, bolsa_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Bolsa não encontrada"
                )

            return BolsaResponse(
                id=resultado.id,
                nome=resultado.nome,
                vertente=resultado.vertente,
                salario=resultado.salario,
                remunerado=resultado.remunerado,
                horas_semanais=resultado.horas_semanais,
                quantidade_vagas=resultado.quantidade_vagas,
                descricao=resultado.descricao,
                data_inicio=resultado.data_inicio,
                data_fim=resultado.data_fim,
                professor_id=resultado.professor_id
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"A bolsa não foi encontrada: {str(e)}"
            )
    
@app.post("/bolsas", status_code=status.HTTP_201_CREATED)
async def create_bolsa(input: BolsaBase):
    async with get_session() as session:
        try:
            nova_bolsa = Bolsa(
                nome=input.nome,
                vertente=input.vertente,
                salario=input.salario,
                remunerado=input.remunerado,
                horas_semanais=input.horas_semanais,
                quantidade_vagas=input.quantidade_vagas,
                descricao=input.descricao,
                data_inicio=input.data_inicio,
                data_fim=input.data_fim,
                professor_id=input.professor_id
            )
            session.add(nova_bolsa)
            await session.commit()
            await session.refresh(nova_bolsa)

            return BolsaResponse(
                id=nova_bolsa.id,
                nome=nova_bolsa.nome,
                vertente=nova_bolsa.vertente,
                salario=nova_bolsa.salario,
                remunerado=nova_bolsa.remunerado,
                horas_semanais=nova_bolsa.horas_semanais,
                quantidade_vagas=nova_bolsa.quantidade_vagas,
                descricao=nova_bolsa.descricao,
                data_inicio=nova_bolsa.data_inicio,
                data_fim=nova_bolsa.data_fim,
                professor_id=nova_bolsa.professor_id
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar a bolsa: {str(e)}"
            )

@app.patch("/bolsas/{bolsa_id}", status_code=status.HTTP_200_OK)
async def update_bolsa(input: UpdateBolsa, bolsa_id: int):
    async with get_session() as session:
        try:
            resultado = await session.get(Bolsa, bolsa_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Bolsa não encontrada"
                )
            else:
                resultado.nome=resultado.nome if input.nome is None else input.nome
                resultado.vertente=resultado.vertente if input.vertente is None else input.vertente
                resultado.salario=resultado.salario if input.salario is None else input.salario
                resultado.remunerado=resultado.remunerado if input.remunerado is None else input.remunerado
                resultado.horas_semanais=resultado.horas_semanais if input.horas_semanais is None else input.horas_semanais
                resultado.quantidade_vagas=resultado.quantidade_vagas if input.quantidade_vagas is None else input.quantidade_vagas
                resultado.descricao=resultado.descricao if input.descricao is None else input.descricao
                resultado.data_inicio=resultado.data_inicio if input.data_inicio is None else input.data_inicio,
                resultado.data_fim=resultado.data_fim if input.data_fim is None else input.data_fim,
                resultado.professor_id=resultado.professor_id if input.professor_id is None else input.professor_id
                await session.commit()
                await session.refresh(resultado)

                return BolsaResponse(
                    id=resultado.id,
                    nome=resultado.nome,
                    vertente=resultado.vertente,
                    salario=resultado.salario,
                    remunerado=resultado.remunerado,
                    horas_semanais=resultado.horas_semanais,
                    quantidade_vagas=resultado.quantidade_vagas,
                    descricao=resultado.descricao,
                    data_inicio=resultado.data_inicio,
                    data_fim=resultado.data_fim,
                    professor_id=resultado.professor_id
                )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar item parcialmente: {str(e)}"
            )

@app.delete("/bolsas/{bolsa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bolsa(bolsa_id: int):
    await delete_element(bolsa_id, Bolsa)


@app.get("/estagios")
async def get_estagios():
    async with get_session() as session:
        resultado = await session.execute(select(Estagio))
        item = resultado.scalars().all()

        return [EstagioResponse(
            id=row.id,
            nome=row.nome,
            vertente=row.vertente,
            salario=row.salario,
            empresa_id=row.empresa_id,
            horas_semanais=row.horas_semanais,
            remunerado=row.remunerado,
            descricao=row.descricao,
            data_inicio=row.data_inicio,
            data_fim=row.data_fim
            ) for row in item]

@app.get("/estagios/{estagio_id}")
async def get_estagio_id(estagio_id: int):
    async with get_session() as session:
        resultado = await session.get(Estagio, estagio_id)
        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Estágio não encontrado"
            )
        
        return EstagioResponse(
            id=resultado.id,
            nome=resultado.nome,
            vertente=resultado.vertente,
            salario=resultado.salario,
            empresa_id=resultado.empresa_id,
            remunerado=resultado.remunerado,
            horas_semanais=resultado.horas_semanais,
            descricao=resultado.descricao,
            data_inicio=resultado.data_inicio,
            data_fim=resultado.data_fim
        )

@app.post("/estagios", status_code=status.HTTP_201_CREATED)
async def create_estagio(input: EstagioBase):
    async with get_session() as session:
        try:
            novo_estagio = Estagio(
                nome=input.nome,
                vertente=input.vertente,
                salario=input.salario,
                empresa_id=input.empresa_id,
                remunerado=input.remunerado,
                horas_semanais=input.horas_semanais,
                descricao=input.descricao,
                data_inicio=input.data_inicio,
                data_fim=input.data_fim
            )
            session.add(novo_estagio)
            await session.commit()
            await session.refresh(novo_estagio)

            return EstagioResponse(
                id=novo_estagio.id,
                nome=novo_estagio.nome,
                vertente=novo_estagio.vertente,
                salario=novo_estagio.salario,
                empresa_id=novo_estagio.empresa_id,
                remunerado=novo_estagio.remunerado,
                horas_semanais=novo_estagio.horas_semanais,
                descricao=novo_estagio.descricao,
                data_inicio=novo_estagio.data_inicio,
                data_fim=novo_estagio.data_fim
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar o estágio: {str(e)}"
            )

@app.patch("/estagios/{estagio_id}", status_code=status.HTTP_200_OK)
async def update_estagio(input: UpdateEstagio, estagio_id: int):
    async with get_session() as session:
        try:
            resultado = await session.get(Estagio, estagio_id)
            print(resultado)
            if resultado is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Estágio não encontrado"
                )
            else:
                resultado.nome=resultado.nome if input.nome is None else input.nome
                resultado.vertente=resultado.vertente if input.vertente is None else input.vertente
                resultado.salario=resultado.salario if input.salario is None else input.salario
                resultado.remunerado=resultado.remunerado if input.remunerado is None else input.remunerado
                resultado.horas_semanais=resultado.horas_semanais if input.horas_semanais is None else input.horas_semanais
                resultado.descricao=resultado.descricao if input.descricao is None else input.descricao
                resultado.data_inicio=resultado.data_inicio if input.data_inicio is None else input.data_inicio,
                resultado.data_fim=resultado.data_fim if input.data_fim is None else input.data_fim,
                resultado.empresa_id=resultado.empresa_id if input.empresa_id is None else input.empresa_id
                await session.commit()
                await session.refresh(resultado)

                return EstagioResponse(
                    id=resultado.id,
                    nome=resultado.nome,
                    vertente=resultado.vertente,
                    salario=resultado.salario,
                    empresa_id=resultado.empresa_id,
                    remunerado=resultado.remunerado,
                    horas_semanais=resultado.horas_semanais,
                    descricao=resultado.descricao,
                    data_inicio=resultado.data_inicio,
                    data_fim=resultado.data_fim
                )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar item parcialmente: {str(e)}"
            )

@app.delete("/estagios/{estagio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_estagio(estagio_id: int):
    await delete_element(estagio_id, Estagio)

@app.get("/professores")
async def get_professores():
    async with get_session() as session:
        resultado = await session.execute(select(Professor))
        item = resultado.scalars().all()

        return [ProfessorResponse(
            id=row.id,
            nome=row.nome,
            vertente=row.vertente,
            telefone=row.telefone,
            email=row.email,
            website=row.website,
            formacao=row.formacao,
            ) for row in item]


@app.get("/professores/{professor_id}")
async def get_professor_id(professor_id: int):
    async with get_session() as session:
        resultado = await session.get(Professor, professor_id)
        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Professor não encontrado"
            )

        return ProfessorResponse(
            id=resultado.id,
            nome=resultado.nome,
            vertente=resultado.vertente,
            telefone=resultado.telefone,
            email=resultado.email,
            website=resultado.website,
            formacao=resultado.formacao
        )

@app.post("/professores", status_code=status.HTTP_201_CREATED)
async def create_professor(input: ProfessorBase):
    async with get_session() as session:
        try:
            novo_professor = Professor(
                nome=input.nome,
                vertente=input.vertente,
                telefone=input.telefone,
                email=input.email,
                website=input.website,
                formacao=input.formacao
            )
            session.add(novo_professor)
            await session.commit()
            await session.refresh(novo_professor)

            return ProfessorResponse(
                id=novo_professor.id,
                nome=novo_professor.nome,
                vertente=novo_professor.vertente,
                telefone=novo_professor.telefone,
                email=novo_professor.email,
                website=novo_professor.website,
                formacao=novo_professor.formacao
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar o professor: {str(e)}"
            )

@app.patch("/professores/{professor_id}", status_code=status.HTTP_200_OK)
async def update_professor(input: UpdateProfessor, professor_id):
    async with get_session() as session:
        try:
            resultado = await session.get(Professor, professor_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Professor não encontrado"
                )
            else:
                resultado.nome=resultado.nome if input.nome is None else input.nome
                resultado.vertente=resultado.vertente if input.vertente is None else input.vertente
                resultado.telefone=resultado.telefone if input.telefone is None else input.telefone
                resultado.email=resultado.email if input.email is None else input.email
                resultado.website=resultado.website if input.website is None else input.website
                resultado.formacao=resultado.formacao if input.formacao is None else input.formacao
                await session.commit()
                await session.refresh(resultado)

                return ProfessorResponse(
                    id=resultado.id,
                    nome=resultado.nome,
                    vertente=resultado.vertente,
                    telefone=resultado.telefone,
                    email=resultado.email,
                    website=resultado.website,
                    formacao=resultado.formacao
                )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar item parcialmente: {str(e)}"
            )

@app.delete("/professores/{professor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_professor(professor_id: int):
    await delete_element(professor_id, Professor)

@app.get("/empresas")
async def get_empresas():
    async with get_session() as session:
        resultado = await session.execute(select(Empresa))
        item = resultado.scalars().all()

        return [EmpresaResponse(
            id=row.id,
            nome=row.nome,
            vertente=row.vertente,
            telefone=row.telefone,
            email=row.email,
            website=row.website,
            CNPJ=row.CNPJ,
            status=row.status,
            endereco_id=row.endereco_id
            ) for row in item]

@app.get("/empresas/{empresa_id}")
async def get_empresa_id(empresa_id: int):
    async with get_session() as session:
        resultado = await session.get(Empresa, empresa_id)
        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Empresa não encontrada"
            )

        await session.commit()
        await session.refresh(resultado)
        return EmpresaResponse(
            id=resultado.id,
            nome=resultado.nome,
            vertente=resultado.vertente,
            CNPJ=resultado.CNPJ,
            endereco_id=resultado.endereco_id,
            telefone=resultado.telefone,
            email=resultado.email,
            website=resultado.website,
            status=resultado.status,
        )

@app.post("/empresas", status_code=status.HTTP_201_CREATED)
async def create_empresa(input: EmpresaBase):
    async with get_session() as session:
        try:
            nova_empresa = Empresa(
                nome=input.nome,
                vertente=input.vertente,
                CNPJ=input.CNPJ,
                endereco_id=input.endereco_id,
                telefone=input.telefone,
                email=input.email,
                website=input.website,
                status=input.status,
            )
            session.add(nova_empresa)
            await session.commit()
            await session.refresh(nova_empresa)

            return EmpresaResponse(
                id=nova_empresa.id,
                nome=nova_empresa.nome,
                vertente=nova_empresa.vertente,
                CNPJ=nova_empresa.CNPJ,
                endereco_id=nova_empresa.endereco_id,
                telefone=nova_empresa.telefone,
                email=nova_empresa.email,
                website=nova_empresa.website,
                status=nova_empresa.status,
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar a empresa: {str(e)}"
            )

@app.patch("/empresas/{empresa_id}", status_code=status.HTTP_200_OK)
async def update_empresa(input: UpdateEmpresa, empresa_id):
    async with get_session() as session:
        try:
            resultado = await session.get(Empresa, empresa_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Empresa não encontrada"
                )
            else:
                resultado.nome=resultado.nome if input.nome is None else input.nome
                resultado.vertente=resultado.vertente if input.vertente is None else input.vertente
                resultado.CNPJ=resultado.CNPJ if input.CNPJ is None else input.CNPJ
                resultado.endereco_id=resultado.endereco_id if input.endereco_id is None else input.endereco_id
                resultado.telefone=resultado.telefone if input.telefone is None else input.telefone
                resultado.email=resultado.email if input.email is None else input.email
                resultado.website=resultado.website if input.website is None else input.website
                resultado.status=resultado.status if input.status is None else input.status
                await session.commit()
                await session.refresh(resultado)

                return EmpresaResponse(
                    id=resultado.id,
                    nome=resultado.nome,
                    vertente=resultado.vertente,
                    CNPJ=resultado.CNPJ,
                    endereco_id=resultado.endereco_id,
                    telefone=resultado.telefone,
                    email=resultado.email,
                    website=resultado.website,
                    status=resultado.status,
                )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar item parcialmente: {str(e)}"
            )

@app.delete("/empresas/{empresa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_empresa(empresa_id: int):
    await delete_element(empresa_id, Empresa)


@app.get("/enderecos")
async def get_endereco():
    async with get_session() as session:
        resultado = await session.execute(select(Endereco))
        item = resultado.scalars().all()

        return [EnderecoResponse(
            id=row.id,
            rua=row.rua,
            numero=row.numero,
            bairro=row.bairro,
            cidade=row.cidade,
            estado=row.estado,
            cep=row.cep,
            ) for row in item]

@app.get("/enderecos/{endereco_id}")
async def get_endereco_id(endereco_id: int):
    async with get_session() as session:
        resultado = await session.get(Endereco, endereco_id)
        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Endereço não encontrado"
            )

        return EnderecoResponse(
            id=resultado.id,
            rua=resultado.rua,
            numero=resultado.numero,
            bairro=resultado.bairro,
            cidade=resultado.cidade,
            estado=resultado.estado,
            cep=resultado.cep
        )

@app.post("/enderecos", status_code=status.HTTP_201_CREATED)
async def create_endereco(input: EnderecoBase):
    async with get_session() as session:
        try:
            novo_endereco = Endereco(
                rua=input.rua,
                numero=input.numero,
                bairro=input.bairro,
                cidade=input.cidade,
                estado=input.estado,
                cep=input.cep
            )
            session.add(novo_endereco)
            await session.commit()
            await session.refresh(novo_endereco)

            return EnderecoResponse(
                id=novo_endereco.id,
                rua=novo_endereco.rua,
                numero=novo_endereco.numero,
                bairro=novo_endereco.bairro,
                cidade=novo_endereco.cidade,
                estado=novo_endereco.estado,
                cep=novo_endereco.cep
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar o endereço: {str(e)}"
            )

@app.patch("/enderecos/{endereco_id}", status_code=status.HTTP_200_OK)
async def update_endereco(input: UpdateEndereco, endereco_id: int):
    async with get_session() as session:
        try:
            resultado = await session.get(Endereco, endereco_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Endereço não encontrado"
                )
            else:
                resultado.rua=resultado.rua if input.rua is None else input.rua
                resultado.numero=resultado.numero if input.numero is None else input.numero
                resultado.bairro=resultado.bairro if input.bairro is None else input.bairro
                resultado.cidade=resultado.cidade if input.cidade is None else input.cidade
                resultado.estado=resultado.estado if input.estado is None else input.estado
                resultado.cep=resultado.cep if input.cep is None else input.cep
                await session.commit()
                await session.refresh(resultado)
                
                return EnderecoResponse(
                    id=resultado.id,
                    rua=resultado.rua,
                    numero=resultado.numero,
                    bairro=resultado.bairro,
                    cidade=resultado.cidade,
                    estado=resultado.estado,
                    cep=resultado.cep
                )

        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar item parcialmente: {str(e)}"
            )

@app.delete("/enderecos/{endereco_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_endereco(endereco_id: int):
    await delete_element(endereco_id, Endereco)

@app.get("/plataformas")
async def get_plataforma():
    async with get_session() as session:
        resultado = await session.execute(select(Plataforma))
        item = resultado.scalars().all()

        return [PlataformaResponse(
            id=row.id,
            nome=row.nome,
            email=row.email,
            website=row.website,
            tipo=row.tipo,
            ) for row in item]

@app.get("/plataformas/{plataforma_id}")
async def get_plataforma_id(plataforma_id: int):
    async with get_session() as session:
        resultado = await session.get(Plataforma, plataforma_id)
        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plataforma não encontrada"
            )

        return PlataformaResponse(
            id=resultado.id,
            nome=resultado.nome,
            email=resultado.email,
            website=resultado.website,
            tipo=resultado.tipo
        )

@app.post("/plataformas", status_code=status.HTTP_201_CREATED)
async def create_plataforma(input: PlataformaBase):
    async with get_session() as session:
        try:
            nova_plataforma = Plataforma(
                nome=input.nome,
                email=input.email,
                website=input.website,
                tipo=input.tipo
            )
            session.add(nova_plataforma)
            await session.commit()
            await session.refresh(nova_plataforma)

            return PlataformaResponse(
                id=nova_plataforma.id,
                nome=nova_plataforma.nome,
                email=nova_plataforma.email,
                website=nova_plataforma.website,
                tipo=nova_plataforma.tipo
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar a plataforma: {str(e)}"
            )

@app.patch("/plataformas/{plataforma_id}", status_code=status.HTTP_200_OK)
async def update_plataforma(input: UpdatePlataforma, plataforma_id: int):
    async with get_session() as session:
        try:
            resultado = await session.get(Plataforma, plataforma_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Plataforma não encontrada"
                )
            else:
                resultado.nome=resultado.nome if input.nome is None else input.nome
                resultado.email=resultado.email if input.email is None else input.email
                resultado.website=resultado.website if input.website is None else input.website
                resultado.tipo=resultado.tipo if input.tipo is None else input.tipo
                await session.commit()
                await session.refresh(resultado)

                return PlataformaResponse(
                    id=resultado.id,
                    nome=resultado.nome,
                    email=resultado.email,
                    website=resultado.website,
                    tipo=resultado.tipo
                )

        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar item parcialmente: {str(e)}"
            )

@app.delete("/plataformas/{plataforma_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_plataforma(plataforma_id: int):
    await delete_element(plataforma_id, Plataforma)


@app.get("/cursos")
async def get_courses():
    async with get_session() as session:
        resultado = await session.execute(select(Curso))
        item = resultado.scalars().all()
        return [CursoResponse(
                id=row.id,
                nome=row.nome,
                categoria=row.categoria,
                preco= row.preco,
                plataforma_id=row.plataforma_id,
                nivel=row.nivel,
                vertente=row.vertente,
                data_inicio=row.data_inicio,
                data_fim=row.data_fim
                ) for row in item]
        
@app.get("/cursos/{curso_id}")
async def get_curso_id(curso_id: int):
    async with get_session() as session:
        resultado = await session.get(Curso, curso_id)
        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Curso não encontrado"
            )

        return CursoResponse(
            id=resultado.id,
            nome=resultado.nome,
            categoria=resultado.categoria,
            preco=resultado.preco,
            plataforma_id=resultado.plataforma_id,
            nivel=resultado.nivel,
            vertente=resultado.vertente,
            data_inicio=resultado.data_inicio,
            data_fim=resultado.data_fim,
        )

@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def create_curso(input: CursoBase):
    async with get_session() as session:
        try:
            novo_curso = Curso(
                nome=input.nome,
                categoria=input.categoria,
                preco=input.preco,
                plataforma_id=input.plataforma_id,
                nivel=input.nivel,
                vertente=input.vertente,
                data_inicio=input.data_inicio,
                data_fim=input.data_fim,
            )
            session.add(novo_curso)
            await session.commit()
            await session.refresh(novo_curso)

            return CursoResponse(
                id=novo_curso.id,
                nome=novo_curso.nome,
                categoria=novo_curso.categoria,
                preco=novo_curso.preco,
                plataforma_id=novo_curso.plataforma_id,
                nivel=novo_curso.nivel,
                vertente=novo_curso.vertente,
                data_inicio=novo_curso.data_inicio,
                data_fim=novo_curso.data_fim,
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar o curso: {str(e)}"
            )

@app.patch("/cursos/{curso_id}", status_code=status.HTTP_200_OK)
async def update_curso(input: UpdateCurso, curso_id: int):
    async with get_session() as session:
        try:
            resultado = await session.get(Curso, curso_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Curso não encontrada"
                )
            else:
                resultado.nome=resultado.nome if input.nome is None else input.nome
                resultado.categoria=resultado.categoria if input.categoria is None else input.categoria
                resultado.preco=resultado.preco if input.preco is None else input.preco
                resultado.plataforma_id=resultado.plataforma_id if input.plataforma_id is None else input.plataforma_id
                resultado.nivel=resultado.nivel if input.nivel is None else input.nivel
                resultado.vertente=resultado.vertente if input.vertente is None else input.vertente
                resultado.data_inicio=resultado.data_inicio if input.data_inicio is None else input.data_inicio,
                resultado.data_fim=resultado.data_fim if input.data_fim is None else input.data_fim,
                await session.commit()
                await session.refresh(resultado)

                return CursoResponse(
                    id=resultado.id,
                    nome=resultado.nome,
                    categoria=resultado.categoria,
                    preco=resultado.preco,
                    plataforma_id=resultado.plataforma_id,
                    nivel=resultado.nivel,
                    vertente=resultado.vertente,
                    data_inicio=resultado.data_inicio,
                    data_fim=resultado.data_fim,
                )

        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao atualizar item parcialmente: {str(e)}"
            )

@app.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int):
    await delete_element(curso_id, Curso)