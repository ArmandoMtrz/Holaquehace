from dataclasses import dataclass
from decimal import Decimal

@dataclass
class LibroMayor:
    folioMayor: int
    periodo: str
    saldo: Decimal = Decimal("0,00")
    cuenta: int

    def __post_init__(self):
        if not isinstance(self.saldo, Decimal):
            self.saldo = Decimal(str(self.saldo))

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            folioMayor=row[0],
            periodo=row[1],
            saldo=row[2],
            cuenta=row[3]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.periodo,
            self.saldo,
            self.cuenta
        )

        if es_update:
            return params + (self.folioMayor,)
        
        return (self.folioMayor,) + params
    
    def __repr__(self):
        return f"""
            Folio mayor: {self.folioMayor}
            Pertenece a la cuenta: {self.cuenta}
            Periodo: {self.periodo}
            Saldo: {self.saldo}       
        """