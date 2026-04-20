from dataclasses import dataclass
from decimal import Decimal

@dataclass
class EstadoFinanciero:
    idEstadoF: int
    periodo: str
    totalActivo: Decimal = Decimal("0,00")
    totalPasivo: Decimal = Decimal("0,00")
    totalCapital: Decimal = Decimal("0,00")

    def __post_init__(self):
        if not isinstance(self.totalActivo, Decimal):
            self.totalActivo = Decimal(str(self.totalActivo))
        if not isinstance(self.totalPasivo, Decimal):
            self.totalPasivo = Decimal(str(self.totalPasivo))
        if not isinstance(self.totalCapital, Decimal):
            self.totalCapital = Decimal(str(self.totalCapital))
    
    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idEstadoF=row[0],
            periodo=row[1],
            totalActivo=row[2],
            totalPasivo=row[3],
            totalCapital=row[4]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.periodo,
            self.totalActivo,
            self.totalPasivo,
            self.totalCapital
        )

        if es_update:
            return params + (self.idEstadoF,)
        
        return (self.idEstadoF,) + params
    
    def __repr__(self):
        return f"""
            Id de estado financiero: {self.idEstadoF}
            Periodo: {self.periodo}
            Total activo: {self.totalActivo}
            Total pasivo: {self.totalPasivo}
            Total capital: {self.totalCapital}       
        """