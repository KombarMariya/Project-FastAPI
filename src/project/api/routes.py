from fastapi import APIRouter


from project.infrastructure.postgres.repository.repo import (
    TypesOfMedicinesRepository,
    ReleaseFormsRepository,
    ManufacturersRepository,
    DosagesRepository, RelatedProductsRepository, MedicinesRepository, ClientsRepository, PharmacistsRepository,
    PurchasesRepository, PurchasedMedicinesRepository, PurchasedRelatedProductsRepository, CouriersRepository,
    DeliveriesRepository
)
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.clients import ClientsSchema
from project.schemas.couriers import CouriersSchema
from project.schemas.deliveries import DeliveriesSchema
from project.schemas.medicines import MedicinesSchema
from project.schemas.pharmacists import PharmacistsSchema
from project.schemas.purchased_medicines import PurchasedMedicinesSchema
from project.schemas.purchased_related_products import PurchasedRelatedProductsSchema
from project.schemas.purchases import PurchasesSchema
from project.schemas.related_products import RelatedProductsSchema
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

# Эндпоинт для получения всех лекарств

@router.get("/all_medicines", response_model=list[MedicinesSchema])
async def get_all_medicines() -> list[MedicinesSchema]:
    medicines_repo = MedicinesRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await medicines_repo.check_connection(session=session)
        all_medicines = await medicines_repo.get_all_medicines(session=session)

    return all_medicines


# Эндпоинт для получения всех сопутствующих товаров
@router.get("/all_related_products", response_model=list[RelatedProductsSchema])
async def get_all_related_products() -> list[RelatedProductsSchema]:
    related_products_repo = RelatedProductsRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await related_products_repo.check_connection(session=session)
        all_related_products = await related_products_repo.get_all_related_products(session=session)

    return all_related_products


# Эндпоинт для получения всех клиентов
@router.get("/all_clients", response_model=list[ClientsSchema])
async def get_all_clients() -> list[ClientsSchema]:
    clients_repo = ClientsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await clients_repo.check_connection(session=session)
        all_clients = await clients_repo.get_all_clients(session=session)
    return all_clients

# Эндпоинт для получения всех фармацевтов
@router.get("/all_pharmacists", response_model=list[PharmacistsSchema])
async def get_all_pharmacists() -> list[PharmacistsSchema]:
    pharmacists_repo = PharmacistsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await pharmacists_repo.check_connection(session=session)
        all_pharmacists = await pharmacists_repo.get_all_pharmacists(session=session)
    return all_pharmacists

# Эндпоинт для получения всех покупок
@router.get("/all_purchases", response_model=list[PurchasesSchema])
async def get_all_purchases() -> list[PurchasesSchema]:
    purchases_repo = PurchasesRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await purchases_repo.check_connection(session=session)
        all_purchases = await purchases_repo.get_all_purchases(session=session)
    return all_purchases

# Эндпоинт для получения всех купленных лекарств
@router.get("/all_purchased_medicines", response_model=list[PurchasedMedicinesSchema])
async def get_all_purchased_medicines() -> list[PurchasedMedicinesSchema]:
    purchased_meds_repo = PurchasedMedicinesRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await purchased_meds_repo.check_connection(session=session)
        all_purchased_meds = await purchased_meds_repo.get_all_purchased_medicines(session=session)
    return all_purchased_meds

# Эндпоинт для получения всех купленных сопутствующих товаров
@router.get("/all_purchased_related_products", response_model=list[PurchasedRelatedProductsSchema])
async def get_all_purchased_related_products() -> list[PurchasedRelatedProductsSchema]:
    purchased_related_repo = PurchasedRelatedProductsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await purchased_related_repo.check_connection(session=session)
        all_purchased_related = await purchased_related_repo.get_all_purchased_related_products(session=session)
    return all_purchased_related

# Эндпоинт для получения всех курьеров
@router.get("/all_couriers", response_model=list[CouriersSchema])
async def get_all_couriers() -> list[CouriersSchema]:
    couriers_repo = CouriersRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await couriers_repo.check_connection(session=session)
        all_couriers = await couriers_repo.get_all_couriers(session=session)
    return all_couriers

# Эндпоинт для получения всех доставок
@router.get("/all_deliveries", response_model=list[DeliveriesSchema])
async def get_all_deliveries() -> list[DeliveriesSchema]:
    deliveries_repo = DeliveriesRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await deliveries_repo.check_connection(session=session)
        all_deliveries = await deliveries_repo.get_all_deliveries(session=session)
    return all_deliveries