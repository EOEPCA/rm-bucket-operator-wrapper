import logging

from http import HTTPStatus

from kubernetes import config as k8s_config, client as k8s_client
from pydantic import BaseModel

from bucket_wrapper import app, config


# TODO: fix logging output with gunicorn
logger = logging.getLogger(__name__)

CONTAINER_REGISTRY_SECRET_NAME = "container-registry"


@app.on_event("startup")
async def load_k8s_config():
    try:
        k8s_config.load_kube_config()
    except Exception:
        # load_kube_config might throw anything :/
        k8s_config.load_incluster_config()


class BucketCredentials(BaseModel):
    bucketName: str
    secretName: str
    secretNamespace: str


@app.post("/bucket", status_code=HTTPStatus.CREATED)
async def create_bucket(data: BucketCredentials) -> None:
    logger.info(f"Creating bucket in namespace {data.bucketName}")
    group = "epca.eo"
    version = "v1alpha1"
    k8s_client.CustomObjectsApi().create_namespaced_custom_object(
        group=group,
        version=version,
        plural="buckets",
        namespace=config.NAMESPACE_FOR_BUCKET_RESOURCE,
        body={
            "apiVersion": f"{group}/{version}",
            "kind": "Bucket",
            "metadata": {
                # TODO: better name for bucket resource?
                "name": data.bucketName,
                "namespace": config.NAMESPACE_FOR_BUCKET_RESOURCE,
            },
            "spec": {
                # we use the workspace name as bucket name since it's a good unique name
                "bucketName": data.bucketName,
                "secretName": data.secretName,
                "secretNamespace": data.secretNamespace,
            },
        },
    )
    return
