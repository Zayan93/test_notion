import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class ContentSheets:
    table = "sheets_content"
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    num: int = 0
    order_number: int = 0
    price_usd: int = 0
    price_rub: int = 0
    delivery_date: datetime = field(default_factory=datetime.now)