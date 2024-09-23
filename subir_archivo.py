from google.cloud import storage

client = storage.Client.from_service_account_json("clave.json")
bucket = client.get_bucket("data-bucket-py-1")

#defino nombre y ubicacion dentro del bucket
objeto_en_bucket = bucket.blob("hola_mundo1.txt")

#subo bucket. defino path en filesystem local
#hola_mundo.txt esta en mi disco.
objeto_en_bucket.upload_from_filename("hola_mundo.txt")
