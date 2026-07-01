import os
import json
import uuid
from datetime import datetime, timezone
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

    def upload_json(self, data: dict, prefix: str = "doacoes") -> dict:
        """Grava um registro JSON imutável no bucket (WORM storage).

        Usado para persistir o comprovante completo da doação (dados do
        formulário + dados retornados pelo Stripe) de forma auditável.
        """
        if self.bucket is None:
            raise HTTPException(
                status_code=500,
                detail="Serviço de armazenamento WORM não configurado (credenciais do GCS ausentes).",
            )

        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
        object_name = f"{prefix}/{timestamp}-{uuid.uuid4()}.json"

        try:
            blob = self.bucket.blob(object_name)
            blob.upload_from_string(
                json.dumps(data, ensure_ascii=False, indent=2, default=str),
                content_type="application/json",
            )
            return {
                "worm_url": f"https://storage.googleapis.com/{self.bucket_name}/{object_name}",
                "worm_path": object_name,
            }
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Erro ao gravar registro WORM: {str(exc)}")