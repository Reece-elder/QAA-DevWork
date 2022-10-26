# Lesson
Go through slides, diagram and more explanation of the role Terraform has and why its used
Important to show typical node structure for projects using Terraform, Ansible and cloud providers

# Tutorial 
Install and set up Terraform on an EC2 machine

Go to this link https://www.terraform.io/downloads and copy the commands it gives you
verify downloaded w/ `terraform --version`

# Create a simple EC2 instance demo
Make note of your access key and secret access key, they should be private though
`touch main.tf` 
In main.tf add the following, find out the ami number by going to aws and grabbing the exact ami id of the instance you want to create (22.04 Ubuntu in eu-west-2)


```t
provider "aws" {
    access_key = "WERF864FE8EFE8FEASE"
    secret_key = "864wef684ef646ewf8ew6f4684wef"
    region = "eu-west-2"
}

resource "aws_instance" "demo1" {
    ami = "ami-0fb391cce7a602d1f"
    instance_type = "t2.micro"
}
```

Run the following commands to start the terraform process
`terraform init`
`terraform plan`
`terraform apply`

# Exercise 
Create your own ec2 using terraform, and try to connect to it via ec2 connect

