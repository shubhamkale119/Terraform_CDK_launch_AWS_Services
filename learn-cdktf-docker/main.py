#!/usr/bin/env python
from constructs import Construct
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput, RemoteBackend
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str, access_key: str, secret_key: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="ap-south-1",
                    access_key=access_key,
                    secret_key=secret_key
                    )

        instance = Instance(self, "compute",
                            ami="ami-013168dc3850ef002",
                            instance_type="t2.micro",
                            )

        TerraformOutput(self, "public_ip",
                        value=instance.public_ip,
                        )


app = App()
stack = MyStack(app, "aws_instance", access_key="AKIATCKARTAA6SSTGIHJ", secret_key="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")

RemoteBackend(stack,
              hostname='app.terraform.io',
              organization='shubhamkale119',
              workspaces=NamedRemoteWorkspace('learn-cdktf')
              )

app.synth()
