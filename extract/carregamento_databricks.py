from databricks.sdk import WorkspaceClient
import os

w = WorkspaceClient(
    host="https://dbc-35d172ff-3c30.cloud.databricks.com",
    token="DATABRICKS_TOKEN"
)

arquivo = os.path.join(
    os.path.expanduser("~"),
    "OneDrive", "Documentos", "pratica_pyspark",
    "Projeto-SELIC-2020-2026", "extract", "selic.parquet"
)

destino = "/Volumes/main/default/selic/selic.parquet"

if not os.path.exists(arquivo):
    print(f"Arquivo não encontrado: {arquivo}")
else:
    with open(arquivo, "rb") as f:
        w.files.upload(destino, f, overwrite=True)
    print(f"Upload concluído: {destino}")