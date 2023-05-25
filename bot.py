from pyrogram import Client
from pyrogram.types import InputMediaPhoto

# Inisialisasi klien Pyrogram
api_id = 27486395
api_hash = 'af6f9c8666fca1f5da9b427904d8a015'
bot_token = '5914178815:AAFZYOWz-0KEgVhRNlpE0dkhVHyTJy9FXSM'

app = Client('my_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Fungsi untuk mengirim gambar dan mengedit caption ke channel
def send_image_with_caption(channel_id, image_path, text):
    try:
        # Mengunggah gambar
        media = app.send_photo(chat_id=channel_id, photo=image_path, text = message.text)

        # Mengedit caption dengan menambahkan teks
        media.edit_caption(text)

        print('Gambar terkirim ke channel', channel_id)
    except Exception as e:
        print('Gagal mengirim gambar ke channel', channel_id)
        print(str(e))

# Fungsi untuk mengirim gambar dan mengedit caption ke dua channel
def send_image_and_edit_caption_to_channels(channel_ids):
    image_path = 'path/to/image.jpg'  # Ganti dengan path file gambar yang ingin Anda kirimkan

    text = message.text
    for channel_id in channel_ids:
        send_image_with_caption(channel_id, image_path, text)

# Contoh penggunaan
def main():
    # Daftar channel ID
    channel_ids = ['-1001838616960', '-1001912391280']  # Ganti dengan channel ID yang sesuai

    send_image_and_edit_caption_to_channels(channel_ids)

# Menjalankan program
if __name__ == '__main__':
    with app:
        main()