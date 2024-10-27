from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.clients import ClientsSchema
from project.schemas.medicines import MedicinesSchema
from project.schemas.pharmacists import PharmacistsSchema
from project.schemas.purchases import PurchasesSchema
from project.schemas.related_products import RelatedProductsSchema
from project.schemas.types_of_medicines import TypesOfMedicinesSchema
from project.schemas.release_forms import ReleaseFormsSchema
from project.schemas.manufacturers import ManufacturersSchema
from project.schemas.dosages import DosagesSchema
from project.infrastructure.postgres.models import TypesOfMedicines, ReleaseForms, Manufacturers, Dosages, \
    RelatedProducts, Medicines, Clients, Pharmacists, Purchases

from project.core.config import settings



class TypesOfMedicinesRepository:
    _collection: Type[TypesOfMedicines] = TypesOfMedicines

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_types_of_medicines(self, session: AsyncSession) -> list[TypesOfMedicinesSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.types_of_medicines;"
        result = await session.execute(text(query))
        return [TypesOfMedicinesSchema.model_validate(obj=record) for record in result.mappings().all()]


class ReleaseFormsRepository:
    _collection: Type[ReleaseForms] = ReleaseForms

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_release_forms(self, session: AsyncSession) -> list[ReleaseFormsSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.release_forms;"
        result = await session.execute(text(query))
        return [ReleaseFormsSchema.model_validate(obj=record) for record in result.mappings().all()]


class ManufacturersRepository:
    _collection: Type[Manufacturers] = Manufacturers

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_manufacturers(self, session: AsyncSession) -> list[ManufacturersSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.manufacturers;"
        result = await session.execute(text(query))
        return [ManufacturersSchema.model_validate(obj=record) for record in result.mappings().all()]


class DosagesRepository:
    _collection: Type[Dosages] = Dosages

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_dosages(self, session: AsyncSession) -> list[DosagesSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.dosages;"
        result = await session.execute(text(query))
        return [DosagesSchema.model_validate(obj=record) for record in result.mappings().all()]

class MedicinesRepository:
    _collection: Type[Medicines] = Medicines

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_medicines(self, session: AsyncSession) -> list[MedicinesSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.medicines;"
        result = await session.execute(text(query))
        return [MedicinesSchema.model_validate(obj=record) for record in result.mappings().all()]


class RelatedProductsRepository:
    _collection: Type[RelatedProducts] = RelatedProducts

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_related_products(self, session: AsyncSession) -> list[RelatedProductsSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.related_products;"
        result = await session.execute(text(query))
        return [RelatedProductsSchema.model_validate(obj=record) for record in result.mappings().all()]


class ClientsRepository:
    _collection: Type[Clients] = Clients

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_clients(self, session: AsyncSession) -> list[ClientsSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.clients;"
        result = await session.execute(text(query))
        return [ClientsSchema.model_validate(obj=record) for record in result.mappings().all()]


class PharmacistsRepository:
    _collection: Type[Pharmacists] = Pharmacists

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_pharmacists(self, session: AsyncSession) -> list[PharmacistsSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.pharmacists;"
        result = await session.execute(text(query))
        return [PharmacistsSchema.model_validate(obj=record) for record in result.mappings().all()]


class PurchasesRepository:
    _collection: Type[Purchases] = Purchases

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_purchases(self, session: AsyncSession) -> list[PurchasesSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.purchases;"
        result = await session.execute(text(query))
        return [PurchasesSchema.model_validate(obj=record) for record in result.mappings().all()]