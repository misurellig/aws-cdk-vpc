from aws_cdk import core
import aws_cdk.aws_ec2 as ec2

class AwsCdkVpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        self.vpc = ec2.Vpc(self, "VPC",
            cidr='10.10.0.0/16',
            max_azs=6,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE,
                    name='Private',
                    cidr_mask=19
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Public',
                    cidr_mask=20
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE,
                    name='Spare',
                    cidr_mask=20,
                    reserved=True
                )
            ])
        core.CfnOutput(self, "Output", value=self.vpc.vpc_id)

        self.bastion = ec2.BastionHostLinux(self, id,
            vpc = self.vpc,
            instance_name = 'bastione',
            instance_type = ec2.InstanceType('t3.micro'),
            machine_image = ec2.AmazonLinuxImage(),
            subnet_selection = ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )
        core.CfnOutput(self, 'bastion-id', value=self.bastion.instance_id)



        

    
