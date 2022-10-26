# Lesson 
VPC - Virtual Private Cloud 

VPCs are a foundation of AWS and how all networked services can intract and talk with eachother  
Isolated section of AWS cloud where you can launch AWS resources in a custom network where you define *everything*
- Subnets
- IP Address Range
- Route Tables
- Network Gateways
- IPv4 OR IPv6

*Diagram to show this*

All resources to this point have been done with a default VPC with little configuration or changes made

Resources we need: 
- VPC
- CIDR Block
- Subnet
- Subnet Group
- Network Gateway
- Route table 
- Security Group

# Complex Tutorial (Creating each part)
1) VPC > Create VPC (VPC Only) to start the process
2) Decide on a CIDR Block (10.2.0.0/20) No IPv6 CIDR
3) Click Create VPC
4) Subnets > Create Subnet
5) Make a public subnet a and assign it to AV Zone eu-west-2a with a CIDR block of 10.2.0.0/24
6) Make public subnet b, assign to AV Zone 2b and CIDR 10.2.2.0/24
7) Make both subnets produce public IP, right click and go to subnet settings and auto assign the public IPs
8) Create your internet gateway, give it a name and just click create
8.5) Select your IGW and click 'Attach to VPC'
9) Create a route table for the vpc, make sure you specify what vpc to use
10) Edit the Route Table Subnet Associations and select all available subnets
11) Edit the routes of your route table to include the IGW, set the destination to be 0.0.0.0/0
12) Create a new ec2 connecting to this VPC, make a new SG allowing you to SSH in 
13) Connect to your EC2

# Exercise
Create your own VPC with 2x public subnets. Create an ec2 in one of the subnets and ssh into it 

# Easy Tutorial
1) Create VPC (using the wizard) set the VPC Endpoints to None and ssh to ec2

# Exercise
Create your own VPC with 2x public subnets. Create an ec2 in one of the subnets and ssh into it 