from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from project.infrastructure.postgres.database import Base


class TypesOfMedicines(Base):
    __tablename__ = "types_of_medicines"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    medicines: Mapped[list["Medicines"]] = relationship("Medicines", back_populates="type_of_medicine")

class ReleaseForms(Base):
    __tablename__ = "release_forms"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    medicines: Mapped[list["Medicines"]] = relationship("Medicines", back_populates="release_form")

class Manufacturers(Base):
    __tablename__ = "manufacturers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=True)

    medicines: Mapped[list["Medicines"]] = relationship("Medicines", back_populates="manufacturer")

class Dosages(Base):
    __tablename__ = "dosages"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    medicines: Mapped[list["Medicines"]] = relationship("Medicines", back_populates="dosage")


class Medicines(Base):
    __tablename__ = "medicines"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    creation_date: Mapped[datetime] = mapped_column(nullable=False)
    expiration_period: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    release_condition: Mapped[str] = mapped_column(nullable=False)

    # Внешние ключи
    type_of_medicine_id: Mapped[int] = mapped_column(ForeignKey("types_of_medicines.id"), nullable=False)
    release_form_id: Mapped[int] = mapped_column(ForeignKey("release_forms.id"), nullable=False)
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id"), nullable=False)
    dosage_id: Mapped[int] = mapped_column(ForeignKey("dosages.id"), nullable=False)

    # Обратные отношения
    type_of_medicine: Mapped[TypesOfMedicines] = relationship("TypesOfMedicines", back_populates="medicines")
    release_form: Mapped[ReleaseForms] = relationship("ReleaseForms", back_populates="medicines")
    manufacturer: Mapped[Manufacturers] = relationship("Manufacturers", back_populates="medicines")
    dosage: Mapped[Dosages] = relationship("Dosages", back_populates="medicines")

class RelatedProducts(Base):
    __tablename__ = "related_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)