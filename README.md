
# AWS CDK VPC

CDK stack example to create a new VPC with an Amazon EC2 instance as a bastion host to ssh-access via [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).

Note that VPC subnetting is based on the [Practical VPC Design](https://aws.amazon.com/blogs/startups/practical-vpc-design/) suggestions.

## Usage

Inside a CDK enabled environment (like [docker-aws-cdk](https://github.com/misurellig/docker-aws-cdk)), create the python3 virtual environment and install the required dependencies.

```
 python3 -m venv .env && source .env/bin/activate
```

```
$ pip3 install -r requirements.txt
```

Export CDK_DEFAULT_ACCOUNT, CDK_DEFAULT_REGION and CDK_DEPLOY_REGION env vars.
```
export CDK_DEFAULT_ACCOUNT=111111111111
export CDK_DEFAULT_REGION=eu-south-1
export CDK_DEPLOY_REGION=eu-south-1
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
Resources:
  VPCB9E5F0B4:
    Type: AWS::EC2::VPC
    Properties:
...
...
```

To install the bootstrap stack into an environment
```
$ cdk bootstrap
⏳  Bootstrapping environment 111111111111/eu-south-1...
```

To deploy the stack and create AWS resources
```
$ cdk deploy
cdk deploy
aws-cdk-vpc: deploying...
aws-cdk-vpc: creating CloudFormation changeset...
[██████████████████████████████████████████████████████████] (35/35)

 ✅  aws-cdk-vpc

Outputs:
aws-cdk-vpc.Output = vpc-XXXXXXXXX

Stack ARN:
arn:aws:cloudformation:eu-south-1:111111111111:stack/aws-cdk-vpc/78a992a84-234f-41tf-9dd2-06f9a6694a95
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
