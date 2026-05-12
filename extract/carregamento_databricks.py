from databricks.sdk import WorkspaceClient
import pandas as pd
import requests

w = WorkspaceClient(
    host="https://dbc-35d172ff-3c30.cloud.databricks.com",
    token="SEU_TOKEN_AQUI"
)

arquivo=r"C:\Users\digi.luism.utic\OneDrive - SEBRAE\Documentos\Selic2020-2026\extract\selic.parquet"

with open(arquivo, "rb") as f:

    w.files.upload(
        "/FileStore/selic.parquet",
        f
    )

print("Upload concluído no Databricks!")