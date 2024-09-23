from google.cloud import storage

client = storage.Client.from_service_account_json("clave.json")
bucket = client.get_bucket("data-bucket-py-1")

#obtenemos lista de objetos
objetos = client.list_blobs(bucket)
for archivo in objetos:
    print(archivo.name)