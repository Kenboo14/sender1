from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
# Inisialisasi klien Pyrogram
api_id = 27486395
api_hash = 'af6f9c8666fca1f5da9b427904d8a015'
bot_token = '6071792533:AAEWhn6DTClCsDbNeFNgw6oopPlZ6LRWb04'
app = Client('my_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)
owner_id = [5721492036,1935806583]
# Fungsi untuk mengirim gambar dan mengedit caption ke channel
def send_image_with_caption(channel_id, image_path, text):
    try:
        # Mengunggah gambar
        media = app.send_photo(chat_id=channel_id, photo=image_path, caption='')
        # Mengedit caption dengan menambahkan teks
        media.edit_caption(text)
        print('Gambar terkirim ke channel', channel_id)
    except Exception as e:
        print('Gagal mengirim gambar ke channel', channel_id)
        print(str(e))
# Fungsi untuk mengirim gambar dan mengedit caption ke dua channel
def send_image_and_edit_caption_to_channels(channel_ids, text):
    image_path = 'IMG_20230525_043448_921.jpg'  # Ganti dengan path file gambar yang ingin Anda kirimkan
    for channel_id in channel_ids:
        send_image_with_caption(channel_id, image_path, text)
        
def send_image_and_edit_caption_to_channelss(channel_idc, text):
    image_patch = 'IMG_20230525_043509_774.jpg'
    
    for channel_id in channel_idc:
        send_image_with_caption(channel_id, image_patch, text)

@app.on_message(filters.command(['ch1']))
def handle_message(client, message):
            text = message.text
            channel_idc = [-1001809632005, -1001820086673]
            send_image_and_edit_caption_to_channelss(channel_idc, text)

@app.on_message(filters.private & filters.user(owner_id))
def handle_message(client, message):
            # Mendapatkan teks yang ingin ditambahkan dari pesan
            text = message.text
            # Daftar channel ID
            channel_ids = [-1001985436252, -1001891595565] # Ganti dengan channel ID yang sesuai
            send_image_and_edit_caption_to_channels(channel_ids, text)
# Contoh penggunaan
# Fungsi untuk menangani perintah "/start"
@app.on_message(filters.command(['start']))
def start_command(client, message):
    text = "Halo! Bot sedang aktif."
    client.send_message(chat_id=message.chat.id, text=text)
app.run()