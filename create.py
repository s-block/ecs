# -*- coding: utf-8 -*-
import json
import yaml

from stack import (
    domain,
    certificates,
    vpc,
    database,
    assets,
    cluster,
    repository,
    sqs,
    cluster,
)

if __name__ == '__main__':
    data = json.loads(cluster.template.to_json())

    print(yaml.dump(data, allow_unicode=True))
