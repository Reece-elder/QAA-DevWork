# Lesson 
Powerpoint Slides
Plus diagram talking about the structure
Module consists of the following: main.tf, variables.tf, output.tf 
Environment consists of main.tf, output.tf, variables.tf, modules, .tfvars

modules allow you to modulise your code
Example - In an environment you require 3x EC2s to be created each belonging to the same SG. Module for EC2 and module for SG


main.tf - stores the resources
variables.tf - stores the variables
output.tf - lets you output necessary information (required IDs etc.)

# Tutorial 
File structure look like below: 
- main.tf
- output.tf
- variables.tf
/ EC2
    - main.tf
    - output.tf
    - variables.tf
/ SG
    - main.tf
    - output.tf
    - variables.tf

Contents of /EC2
```t
# main.tf
resource "aws_instance" "vm" {
  ami                    = var.ami
  instance_type          = var.type
  vpc_security_group_ids = [var.sg_id]
}

# output.tf
output "public_ip"{
    value = aws_instance.vm.public_ip
}

# variables.tf
variable "ami" {
  default = "ami-0fb391cce7a602d1f"
}

variable "type" {
  default = "t2.micro"
}

variable "sg_id"{
    description = "placeholder for SG module ID"
}
```

Contents of /SG
```t
# main.tf
resource "aws_security_group" "allow_ssh" {

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.open_internet]
  }

}

# output.tf
output "sg_id"{
    value = aws_security_group.allow_ssh.id
}

# variables.tf
variable "open_internet" {
  default = "0.0.0.0/0"
}

```

Contents of root files
```t
# main.tf
provider "aws" {
  region     = var.region
  access_key = var.access_key
  secret_key = var.secret_key

  default_tags {
    tags = {
      project = "tf_demo"
    }
  }
}

module "sg" {
    source = "./SG"
}

module "ec2_1" {
    source = "./EC2"
    sg_id = module.sg.sg_id
}

module "ec2_2" {
    source = "./EC2"
    sg_id = module.sg.sg_id
}

# variables.tf
variable "region" {
  default = "eu-west-2"
}

variable "access_key" {
  sensitive = true
}

variable "secret_key" {
  sensitive = true
}


```
Run init, fmt, plan, apply

# Exercise 
1) Create a module for an EC2, use your root main.tf to create the EC2 resource
2) Modularise your VPC exercise, you should modularise all repeating resources and any other unique resources (up to you how you organise this)