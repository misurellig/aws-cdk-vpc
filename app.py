#!/usr/bin/env python3
import os
from aws_cdk import core

from aws_cdk_vpc.aws_cdk_vpc_stack import AwsCdkVpcStack

app = core.App()

AwsCdkVpcStack(app, "aws-cdk-vpc", env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]))
)

app.synth()
