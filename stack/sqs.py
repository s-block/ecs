# -*- coding: utf-8 -*-
from troposphere import GetAtt, Output, Ref
from troposphere.sqs import Queue

from .template import template


queue = Queue(
    "DashboardQueue",
    template=template,
)


template.add_output([
    Output(
        "DashboardQueueURL",
        Description="URL of the source queue",
        Value=Ref(queue)
    ),
    Output(
        "DashboardQueueARN",
        Description="ARN of the source queue",
        Value=GetAtt(queue, "Arn")
    )
])
