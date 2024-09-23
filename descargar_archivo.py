from google.cloud import storage

client = storage.Client.from_service_account_json("clave.json")
bucket = client.get_bucket("data-bucket-py-1")

#defino nombre y ubicacion del archivo dentro del bucket
#este es el archivo que me quiero descargar
objeto_en_bucket = bucket.blob("hola_mundo1.txt")

#defino nombre y ruta donde lo quiero almacenar en mi disco
objeto_en_bucket.download_to_filename("hola.txt")
