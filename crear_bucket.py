from google.cloud import storage

cliente = storage.Client.from_service_account_json("clave.json")

#definimos nombre del bucket
bucket = cliente.bucket("data-bucket-py-1")

#definimos clase
bucket.storage_class = 'STANDARD'

#creamos bucket
bucket = cliente.create_bucket(bucket, location='us')

print(bucket.name)