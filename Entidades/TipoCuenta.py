from dataclasses import dataclass
from typing import Optional

@dataclass
class TipoCuenta:
    idTipoCuenta: int
    tipoCuenta: str
    categoria: str
    subcategoria: Optional[str] = None

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idTipoCuenta=row[0],
            tipoCuenta=row[1],
            categoria=row[2],
            subcategoria=row[3]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.tipoCuenta,
            self.categoria,
            self.subcategoria
        )

        if es_update:
            return params + (self.idTipoCuenta,)
        
        return (self.idTipoCuenta,) + params
    
    def __repr__(self):
        return f"""
            Id de tipo: {self.idTipoCuenta}
            Tipo de cuenta: {self.tipoCuenta}
            Categoria: {self.categoria}
            Subcategoria: {self.subcategoria}       
        """
