# Tutorial

Terraform files use a syntax similar to JSON, with key value pairs.
They can use variables, inputs, outputs and a number of data types and follow a set structure

<type of resource> "<label 1 (almost always used)>" "<label 2 (not always used)>" {
    # Block Body
    <key> = <value>
    <key2> = [<value2>, <value3>, <value4>]
}

```t
resource "aws_instance" "demo1" {
    ami = "ami-0fb391cce7a602d1f"
    instance_type = "t2.micro"
}
```

Variables can be used in a number of ways with the common being local and input, local variables are local to the file whereas input variables come from other files. One specific time when 'global' variables are better to use due to extra functionality

```t
locals {
    version = 1.2
    name = "instancey_mcinstancey_face"
}

resource "aws_instance" "demo2" {
    ami = "ami-0fb391cce7a602d1f"
    instance_type = "t2.micro"
    tags = {
        Name = "${local_vars.name}"
    }
}
```

Input variables let us INPUT variables, generally as separate files, such as in a file calle variables.tf (what piece of info SHOULD I be adding as a variable in my computer right now??) DO NOT PUSH SECRET_KEYS UP TO GITHUB!!!

make a new file called `variables.tf` and add the following
```t
variable "secret_key" {
    default = "684FE8F4EFW68FWEF684EFW"
    sensitive = true
}

variable "access_key" {
    default = "nregrg6g84erg864gre684erg6erg"
    sensitive = true
}

# Change the provider block to the following
provider "aws" {
    access_key = var.access_key
    secret_key = var.secret_key
}


```

Now our variables are in a seperate file we want to ignore this file from github, best practice would be to have a credentials.tf or use a terraform secrets file

# Exercise
Replace your secret and access key with variables and create a .gitignore to ignore variables
