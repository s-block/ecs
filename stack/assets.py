from troposphere import (
    Join,
    Output,
    GetAtt,
)

from troposphere.s3 import (
    Bucket,
    CorsConfiguration,
    CorsRules,
    PublicRead,
    VersioningConfiguration,
)

from .template import template
from .domain import domain_name


# Create an S3 bucket that holds statics and media
assets_bucket = template.add_resource(
    Bucket(
        "AssetsBucket",
        AccessControl=PublicRead,
        VersioningConfiguration=VersioningConfiguration(
            Status="Enabled"
        ),
        DeletionPolicy="Retain",
        CorsConfiguration=CorsConfiguration(
            CorsRules=[CorsRules(
                AllowedOrigins=[Join("", [
                    "https://*.",
                    domain_name,
                ])],
                AllowedMethods=["POST", "PUT", "HEAD", "GET", ],
                AllowedHeaders=[
                    "*",
                ]
            )]
        ),
    )
)


# Output S3 asset bucket name
template.add_output(Output(
    "AssetsBucketDomainName",
    Description="Assets bucket domain name",
    Value=GetAtt(assets_bucket, "DomainName")
))
