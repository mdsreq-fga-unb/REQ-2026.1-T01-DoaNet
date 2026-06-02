import uuid
from google.cloud import storage
from fastapi import UploadFile, HTTPException


class GCSStorageService:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.client = storage.Client()
        self.bucket = self.client.bucket(self.bucket_name)

    def upload_image(self, file: UploadFile) -> dict:
        allowed_types = {"image/png", "image/jpeg", "image/jpg", "image/webp"}
        if file.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail="Tipo de arquivo inválido")

        extension = file.filename.split(".")[-1].lower() if file.filename else "jpg"
        object_name = f"feed/{uuid.uuid4()}.{extension}"

        try:
            blob = self.bucket.blob(object_name)
            blob.upload_from_file(file.file, content_type=file.content_type)

            return {
                    "image_url": f"https://storage.googleapis.com/{self.bucket_name}/{object_name}",
                    "image_path": object_name,
            }
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Erro ao enviar imagem: {str(exc)}")