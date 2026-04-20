from dataclasses import dataclass
from decimal import Decimal

@dataclass
class EstadoResultado:
    idEstadoRes: int
    perioodo: str
    utilidad: Decimal = Decimal("0,00")

    def __post_init__(self):
        if not isinstance(self.utilidad, Decimal):
            self.utilidad = Decimal(str(self.utilidad))
    
    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idEstadoRes=row[0],
            perioodo=row[1],
            utilidad=row[2]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.perioodo,
            self.utilidad
        )

        if es_update:
            return params + (self.idEstadoRes,)
        
        return (self.idEstadoRes,) + params
    
    def __repr__(self):
        return f"""
            Id de estado de resultado: {self.idEstadoRes}
            Periodo: {self.perioodo}
            Utilidad: {self.utilidad}       
        """