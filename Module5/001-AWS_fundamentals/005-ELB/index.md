# Lesson
Elastic Load Balances (ELB) let you evenly distribute traffic for an app from a single ingress
Used to ensure web traffic is split between multiple nodes incase of increased traffic. Should prevent apps from crashing, but can still crash if all nodes are collapsed. Works like an nginx load balancer and created from within the AWS GUI

# Tutorial 
Create multiple EC2 all with same SG (Port 80 and 22 open)
Ensure EC2s are spread across 2x subnets 
Install nginx on each `sudo apt update` `sudo apt install nginx -y`
Modify the index to be displayed on each ec2 to something different (node 1 prints number 1 etc) 
`cd /var/www/html` 
`sudo nano index.nginx.debian.html` 

From EC2 create a new load balancer
- Application Load balancer
- Internet-facing
- IPv4
- Select all Subnets
- Select security group other EC2s belong to
- Create a target group with your instances 
- Tell load balancer to listen to target group

# Demo 
Create 2x EC2 machines from 2x AV Zones with ports 22 and 80 open. 
They should belong to the same Security group

Install nginx on each of them and modify the default html by going to /var/www/html

Go through the wizard to set up an elastic load balancer (application) for your instances and access the ARN of the ELB 