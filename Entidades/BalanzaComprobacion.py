from dataclasses import dataclass
from decimal import Decimal

@dataclass
class BalanzaComprobacion:
    idBalanza: int
    periodo: str
    debe: Decimal = Decimal("0,00") #El debe encontrado
    haber: Decimal = Decimal("0,00") #El haber encontrado
    totalDebe: Decimal = Decimal("0,00") #El total comprobado en el debe
    totalHaber: Decimal = Decimal("0,00") #El total comprobado en el haber

    def __post_init__(self):
        if not isinstance(self.debe, Decimal):
            self.debe = Decimal(str(self.debe))
        if not isinstance(self.haber, Decimal):
            self.haber = Decimal(str(self.haber))
        if not isinstance(self.totalDebe, Decimal):
            self.totalDebe = Decimal(str(self.totalDebe))
        if not isinstance(self.totalHaber, Decimal):
            self.totalHaber = Decimal(str(self.totalHaber))

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idBalanza=row[0],
            periodo=row[1],
            debe=row[2],
            haber=row[3],
            totalDebe=row[4],
            totalHaber=row[5]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.periodo,
            self.debe,
            self.haber,
            self.totalDebe,
            self.totalHaber
        )

        if es_update:
            return params + (self.idBalanza,)
        
        return (self.idBalanza,) + params
    
    def __repr__(self):
        return f"""
            Id de balanza de comprobacion: {self.idBalanza}
            Periodo: {self.periodo}
            Debe encontrado: {self.debe}
            Haber encontrado: {self.haber}
            Total comprobado en el debe: {self.totalDebe}
            Total comprobado en el haber: {self.totalHaber}       
        """