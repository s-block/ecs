# -*- coding: utf-8 -*-
from troposphere import Ref
from troposphere.ec2 import SecurityGroupRule, SecurityGroup
from troposphere.elasticache import CacheCluster, SubnetGroup

from .template import template
from .vpc import container_a_subnet, container_b_subnet, \
    container_a_subnet_cidr, container_b_subnet_cidr, vpc


db_security_group = SecurityGroup(
    'CacheSecurityGroup',
    template=template,
    GroupDescription="Cache security group.",
    VpcId=Ref(vpc),
    SecurityGroupIngress=[
        # Redis in from web clusters
        SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="6379",
            ToPort="6379",
            CidrIp=container_a_subnet_cidr,
        ),
        SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="6379",
            ToPort="6379",
            CidrIp=container_b_subnet_cidr,
        ),
    ],
)


cache_subnet_group = SubnetGroup(
    "CacheSubnetGroup",
    template=template,
    Description="Subnets available for the Cache Cluster",
    SubnetIds=[Ref(container_a_subnet), Ref(container_b_subnet)],
)


cache_cluster = CacheCluster(
    "RedisCacheCluster",
    template=template,
    CacheNodeType='cache.t2.micro',
    CacheSubnetGroupName=Ref(cache_subnet_group),
    Engine='redis',
    NumCacheNodes=1,
    Port="6379",
    PreferredAvailabilityZone="eu-west-1a",
    VpcSecurityGroupIds=[Ref(db_security_group)],
)
