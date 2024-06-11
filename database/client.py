from dataclasses import dataclass
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()


@dataclass
class Client(Base):
    """Client Table"""

    __tablename__ = "client"
    client_id = mapped_column(Integer, primary_key=True)
    client_name = mapped_column(String)
    short_name = mapped_column(String)
    tax_id = mapped_column(String)
    address_line_1 = mapped_column(String)
    address_line_2 = mapped_column(String)
    pin_code = mapped_column(String)
    city = mapped_column(String)
    state = mapped_column(String)
    country_code = mapped_column(String)
    onboarding_date = mapped_column(Date, nullable=True)
    scope = mapped_column(Integer)
    email_report = mapped_column(Integer, nullable=True)
    is_active = mapped_column(Integer)
