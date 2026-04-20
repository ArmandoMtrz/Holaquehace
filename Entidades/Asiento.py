from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Asiento:
    idAsiento: int
    fecha: str
    concepto: str
    debe: Decimal = Decimal("0,00")
    haber: Decimal = Decimal("0,00")
    tipoAsiento: int = 0

    def __post_init__(self):
        if not isinstance(self.debe, Decimal):
            self.saldo = Decimal(str(self.saldo))
        if not isinstance(self.haber, Decimal):
            self.haber = Decimal(str(self.haber))

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idAsiento=row[0],
            fecha=row[1],
            concepto=row[2],
            debe=row[3],
            haber=row[4],
            tipoAsiento=row[5]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.fecha,
            self.concepto,
            self.debe,
            self.haber,
            self.tipoAsiento
        )

        if es_update:
            return params + (self.idAsiento,)
        
        return (self.idAsiento,) + params
    
    def __repr__(self):
        return f"""
            Id de asiento: {self.idAsiento}
            Fecha: {self.fecha}
            Concepto: {self.concepto}
            Debe: {self.debe}
            Haber: {self.haber}
            Tipo de asiento: {self.tipoAsiento}       
        """