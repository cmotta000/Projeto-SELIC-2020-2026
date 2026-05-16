from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host="https://dbc-35d172ff-3c30.cloud.databricks.com",
    token="dapi29480f31ac017b05bbd87d6974c91cfb"
)

# Lista todos os catálogos
for catalog in w.catalogs.list():
    print(f"Catálogo: {catalog.name}")

# Lista todos os volumes (de todos os schemas)
for volume in w.volumes.list(catalog_name="main", schema_name="default"):  # ajuste se necessário
    print(f"Volume: {volume.full_name} -> /Volumes/{volume.catalog_name}/{volume.schema_name}/{volume.name}")