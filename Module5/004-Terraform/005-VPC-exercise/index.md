# Tutorial
Often your resources will need to be associated with other resources you are trying to create. This can be done by setting the value of an attribute to the atribute of a different resource. 

E.g an EC2 should have a SG associated with it, we won't know the ID of the SG we are creating so we have to use variable association

```t

resource "aws_security_group" "allow_sql" {
    name = "allow_sql"

    ingress {
        from_port = 3306
        to_port = 3306
        protocol = "tcp"
    }
}

resource "aws_instance" "demo2" {
    ami = var.ami
    instance_type = var.type
    # [] only used because the value is an array of SGs to be associated
    vpc_security_group_ids = [aws_security_group.allow_sql.id]
}

```

# Exercise

Using the Terraform docs and information from creating an AWS VPC from scratch you should use terraform to provision a complete VPC with an EC2
- VPC
- 2x public subnets
- 1x security group (SSH, HTTP, MSQL ports)
- Route table (and routes)
- Route table associations
- IGW 
- EC2

Stretch goal - SSH into your EC2 without having to access AWS GUI at all or using any prebuilt resources 

