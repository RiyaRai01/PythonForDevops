import os

AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
if not AWS_REGION:
        raise RuntimeError("AWS_DEFAULT_REGION is not set")