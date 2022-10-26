# Tutorial 

Resources created in Terraform have *attributes* (ip addresses, subnet groups, names etc.) that will be useful for further scripting and automation

Without accessing AWS we can't tell the public IP of the ec2 we have just created

Create a new file called `output.tf` and add the following
```t
output "vm_public_ip" {
    # value = <type of resource>.<name of resource>.<name of attribute>
    value = aws_instance.demo2.public_ip
}

```

# Exercise 
Destroy the old resources, use the docs to see how to create a private s3 bucket and output the bucket domain