import cloudinary
import cloudinary.uploader
import asyncio

cloudinary.config(
    cloud_name="dooqhkh5f",
    api_key="458527344132471",
    api_secret="vea5ad2orxqfrRK_t9TWVhe1IjM",
    secure=True
)


async def upload_image_to_cloudinary(image_path):
    try:
        upload_result = cloudinary.uploader.upload(image_path)
        return upload_result.get("secure_url")
    except Exception as e:
        print(f"Ошибка загрузки изображения: {e}")
        return None