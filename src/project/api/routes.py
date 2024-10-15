from fastapi import APIRouter


from project.infrastructure.postgres.repository.repo import (
    TypesOfMedicinesRepository,
    ReleaseFormsRepository,
    ManufacturersRepository,
    DosagesRepository
)
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.types_of_medicines import TypesOfMedicinesSchema
from project.schemas.release_forms import ReleaseFormsSchema
from project.schemas.manufacturers import ManufacturersSchema
from project.schemas.dosages import DosagesSchema


router = APIRouter()



# Эндпоинт для получения всех типов лекарств
@router.get("/all_types_of_medicines", response_model=list[TypesOfMedicinesSchema])
async def get_all_types_of_medicines() -> list[TypesOfMedicinesSchema]:
    types_repo = TypesOfMedicinesRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await types_repo.check_connection(session=session)
        all_types = await types_repo.get_all_types_of_medicines(session=session)

    return all_types

# Эндпоинт для получения всех форм выпуска
@router.get("/all_release_forms", response_model=list[ReleaseFormsSchema])
async def get_all_release_forms() -> list[ReleaseFormsSchema]:
    release_form_repo = ReleaseFormsRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await release_form_repo.check_connection(session=session)
        all_forms = await release_form_repo.get_all_release_forms(session=session)

    return all_forms

# Эндпоинт для получения всех производителей
@router.get("/all_manufacturers", response_model=list[ManufacturersSchema])
async def get_all_manufacturers() -> list[ManufacturersSchema]:
    manufacturers_repo = ManufacturersRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await manufacturers_repo.check_connection(session=session)
        all_manufacturers = await manufacturers_repo.get_all_manufacturers(session=session)

    return all_manufacturers

# Эндпоинт для получения всех дозировок
@router.get("/all_dosages", response_model=list[DosagesSchema])
async def get_all_dosages() -> list[DosagesSchema]:
    dosages_repo = DosagesRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await dosages_repo.check_connection(session=session)
        all_dosages = await dosages_repo.get_all_dosages(session=session)

    return all_dosages