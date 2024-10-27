import fal_client
from cloud import upload_image_to_cloudinary  # Импортируем функцию загрузки в Cloudinary


def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(log["message"])


def process_images(state):
    human_image_url = state
    garment_image_url = "https://a.lmcdn.ru/product/M/P/MP002XM0BXD2_25176685_1_v1.jpg"
    print(human_image_url)
    response = fal_client.subscribe(
        "fal-ai/idm-vton",
        arguments={
            "human_image_url": human_image_url,
            "garment_image_url": garment_image_url,
            "description": ""
        },
        with_logs=True,
        on_queue_update=on_queue_update,
    )

    if response and isinstance(response, dict):
        return response.get('image', {}).get('url')
    return None