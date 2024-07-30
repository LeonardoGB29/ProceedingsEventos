from models.documentos.Documento import Documento

class FabricaDocumento:
    def __init__(self):
        return
        
    def crear_documento(self, resumen, datos, conclusion, num_pag, evento_id):
        return Documento(resumen, datos, conclusion, num_pag, evento_id)
