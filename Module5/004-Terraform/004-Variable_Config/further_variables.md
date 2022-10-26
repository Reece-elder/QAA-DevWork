# Tutorial
Within an environment there are plenty of times when confidential information is used and lots of variables are needed for management so there are more tools to cover

All .tf files are read when plan and apply are used, variables should be in a separate .tf file but with their values being used in a .tfvars file (terraform.tfvars / *.auto.tfvars by default)

Generally ALL .tf files contain source code and should be accessible, all values should be able to be quickly changed with variables (imagine changing 1000 instances manually to t3.micro from t2.micro) and some variables should be hidden.

Create the following files `variables.tf main.tf terraform.tfvars secret.auto.tfvars`

variables.tf
```t
variable

variable "ami"{
    type = "string"
    default = "ami-0fb391cce7a602d1f"
}

variable "vm_type" {
    type = "string"
    default = "t3.micro"
}

variable "subnet" {
    type = "string"
    default = "subnet-1664417f"
}

variable "name" {
    type = "name"
    default = "demo name"
}

variable "version" {
    type = "number"
}

variable "secret_key" {
  type = "string"
  sensitive = true
}

variable "access_key" {
  type = "string"
  sensitive = true
}
```

terraform.tfvars
```t
ami = "ami-0fb391cce7a602d1f"
vm_type = "t2.micro"
subnet = "subnet-1664417f"
name = "demo name"
```

secret.auto.tfvars contains your access and secret keys, occasionally will hold rds details 

main.tf
```t

provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  region     = "eu-west-2"
}

resource "aws_instance" "demovm"{
    ami = var.ami
    instance_type = var.vm_type
    subnet_id = var.subnet
    tags = {
        Name = var.name
        version = var.version
    }
}

```

tfvars files let you store the exact values of variables, you can also set variables with the -var flag and using environment variables

`terraform apply -var name="new name"` 

When using environment variables they must follow TF_VAR_<variable name>
`export TF_VAR_version=1.2`
`terraform apply`

variables follow a set of hierarchies to ensure the correct values are always used, they follow a structure of: 
1) Specified values using -var
2) tfvars files
3) Environment variables
4) Default Values 

# Exercise
Create an EC2, S3 bucket and security group, the security group should allow ssh access 
All of your resources should use a variables.tf and you should use a variety of -var, .tfvars, environment variables and default values