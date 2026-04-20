from dataclasses import dataclass

@dataclass
class TipoAsiento:
    idTipoAsiento: int
    tipoAsiento: str

    @classmethod
    def from_row(cls, row):
        if not row:
            return None
        return cls(
            idTipoAsiento=row[0],
            tipoAsiento=row[1]
        )
    
    def to_params(self, es_update=False):
        params = (
            self.tipoAsiento,
        )

        if es_update:
            return params + (self.idTipoAsiento,)
        
        return (self.idTipoAsiento,) + params
    
    def __repr__(self):
        return f"""
            Id de tipo de asiento: {self.idTipoAsiento}
            Tipo de asiento: {self.tipoAsiento}       
        """