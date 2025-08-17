from random import randint
from fastapi import UploadFile, HTTPException, status


class ImageService:

    def upload_image(self, file: UploadFile) -> dict:
        if not file:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="No file provided"
            )

        file_path = f"media/{randint(1, 10000)}_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        return {"message": "Image uploaded successfully", "file_path": file_path}


"""
json
{
    "product_id": 123,
}

url
http://localhost:8000/{product_id}

http://localhost:8000?product_id={product_id}


multipart/form-data

// product_id: 123
// file: <image_file>




"""
