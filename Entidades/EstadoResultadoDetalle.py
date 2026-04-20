from dataclasses import dataclass
from decimal import Decimal

@dataclass
class EstadoResultadoDetalle:
    idDetalleER: int
    idEstadoRes: int
    cuenta: int
    subtotal: Decimal = Decimal("0,00")
    idTipoCuenta: int

    def __post_init__(self):
        if not isinstance(self.subtotal, Decimal):
            self.subtotal = Decimal(str(self.subtotal))

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idDetalleER=row[0],
            idEstadoRes=row[1],
            cuenta=row[2],
            subtotal=row[3],
            idTipoCuenta=row[4]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.idEstadoRes,
            self.cuenta,
            self.subtotal,
            self.idTipoCuenta
        )

        if es_update:
            return params + (self.idDetalleER,)
        
        return (self.idDetalleER,) + params
    
    def __repr__(self):
        return f"""
            Id detalle de estado de resultado: {self.idDetalleER}
            Pertenece al estado de resultado: {self.idEstadoRes}
            Pertenece a la cuenta: {self.cuenta}
            Subtotal: {self.subtotal}
            En la categoria de la cuenta: {self.idTipoCuenta}       
        """