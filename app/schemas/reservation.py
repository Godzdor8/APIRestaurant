from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReservationBase(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

class ReservationCreate(ReservationBase):
    pass

class ReservationRead(ReservationBase):
    id: int

    class Config:
        orm_mode = True