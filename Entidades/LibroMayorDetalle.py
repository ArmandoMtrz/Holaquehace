from dataclasses import dataclass
from decimal import Decimal

@dataclass
class LibroMayorDetalle:
    idDetalleLMD: int
    debe: Decimal = Decimal("0,00")
    haber: Decimal = Decimal("0,00")
    folioMayor: int = 0

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
            idDetalleLMD=row[0],
            debe=row[1],
            haber=row[2],
            folioMayor=row[3]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.debe,
            self.haber,
            self.folioMayor
        )

        if es_update:
            return params + (self.idDetalleLMD,)
        
        return (self.idDetalleLMD,) + params
    
    def __repr__(self):
        return f"""
            Id detalle de libro mayor: {self.idDetalleLMD}
            Pertenece al folio mayor: {self.folioMayor}
            Debe: {self.debe}
            Haber: {self.haber}       
        """