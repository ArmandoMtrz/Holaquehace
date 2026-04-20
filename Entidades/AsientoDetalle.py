from dataclasses import dataclass
from decimal import Decimal

@dataclass
class AsientoDetalle:
    idDetalleA: int
    cuenta: int
    debe: Decimal = Decimal("0,00")
    haber: Decimal = Decimal("0,00")
    asiento: int = 0

    def __post_init__(self):
        if not isinstance(self.debe, Decimal):
            self.debe = Decimal(str(self.debe))
        if not isinstance(self.haber, Decimal):
            self.haber = Decimal(str(self.haber))

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idDetalleA=row[0],
            cuenta=row[1],
            debe=row[2],
            haber=row[3],
            asiento=row[4]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.cuenta,
            self.debe,
            self.haber,
            self.asiento
        )

        if es_update:
            return params + (self.idDetalleA,)
        
        return (self.idDetalleA,) + params
    
    def __repr__(self):
        return f"""
            Id de detalle de asiento: {self.idDetalleA}
            Pertenece a la cuenta: {self.cuenta}
            Debe: {self.debe}
            Haber: {self.haber}
            Pertenece al asiento: {self.asiento}       
        """