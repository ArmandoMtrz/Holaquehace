from dataclasses import dataclass
from typing import Optional

@dataclass
class Catalogo:
    correlativo: int
    nombreCuenta: str
    descripcion: str
    cuentaPadre: Optional[int] = None
    tipoCuenta: int = 0

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            correlativo=row[0],
            nombreCuenta=row[1],
            descripcion=row[2],
            cuentaPadre=row[3],
            tipoCuenta=row[4]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.nombreCuenta,
            self.descripcion,
            self.cuentaPadre,
            self.tipoCuenta
        )

        if es_update:
            return params + (self.correlativo,)
        
        return (self.correlativo,) + params