import os
import uuid
from google.cloud import storage
from google.oauth2 import service_account
from fastapi import UploadFile, HTTPException


class GCSStorageService:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.client = None
        self.bucket = None
        
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if credentials_path:
            credentials = service_account.Credentials.from_service_account_file(credentials_path)
            self.client = storage.Client(credentials=credentials)
            self.bucket = self.client.bucket(self.bucket_name)
        else:
            print("Aviso: GOOGLE_APPLICATION_CREDENTIALS não configurado. Upload de imagens falhará.")

    def upload_image(self, file: UploadFile) -> dict:
        allowed_types = {"image/png", "image/jpeg", "image/jpg", "image/webp"}
        if file.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail="Tipo de arquivo inválido")

        extension = file.filename.split(".")[-1].lower() if file.filename else "jpg"
        object_name = f"feed/{uuid.uuid4()}.{extension}"

        if self.bucket is None:
            raise HTTPException(status_code=500, detail="Serviço de upload não configurado (credenciais do GCS ausentes).")

        try:
            blob = self.bucket.blob(object_name)
            blob.upload_from_file(file.file, content_type=file.content_type)

            return {
                    "image_url": f"https://storage.googleapis.com/{self.bucket_name}/{object_name}",
                    "image_path": object_name,
            }
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Erro ao enviar imagem: {str(exc)}")
        
    def upload_logo(self, file: UploadFile) -> dict:
        allowed_types = {"image/png", "image/jpeg", "image/jpg", "image/webp", "image/svg+xml"}
        if file.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail="Tipo de arquivo inválido")
        
        extension = file.filename.split(".")[-1].lower() if file.filename else "png"
        object_name = f"logos/{uuid.uuid4()}.{extension}"  # <- pasta separada
        
        try:
            blob = self.bucket.blob(object_name)
            blob.upload_from_file(file.file, content_type=file.content_type)
            
            return {
                "logo_url": f"https://storage.googleapis.com/{self.bucket_name}/{object_name}",
                "logo_path": object_name,
            }
        
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Erro ao enviar logo: {str(exc)}")