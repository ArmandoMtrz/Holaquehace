from dataclasses import dataclass
from decimal import Decimal

@dataclass
class EstadoFinancieroDetalle:
    idDetalleEF: int
    idEstadoF: int
    idCuenta: int
    monto: Decimal = Decimal("0,00")
    idTipoCuenta: int

    def __post_init__(self):
        if not isinstance(self.monto, Decimal):
            self.monto = Decimal(str(self.monto))

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idDetalleEF=row[0],
            idEstadoF=row[1],
            idCuenta=row[2],
            monto=row[3],
            idTipoCuenta=row[4]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.idEstadoF,
            self.idCuenta,
            self.monto,
            self.idTipoCuenta
        )

        if es_update:
            return params + (self.idDetalleEF,)
        
        return (self.idDetalleEF,) + params
    
    def __repr__(self):
        return f"""
            Id detalle de estado financiero: {self.idDetalleEF}
            Pertenece al estado financiero: {self.idEstadoF}
            Pertenece a la cuenta: {self.idCuenta}
            Monto: {self.monto}
            En la categoria de la cuenta: {self.idTipoCuenta}       
        """