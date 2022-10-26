# Lesson 
Go through AWS Databases slides (Add section for MySQL)

# Demo
Create an AWS MySQL free RDS (IMPORTANT TO LOOK AT COSTS AT BOTTOM), keep note of the password and username. 

# Tutorial 
Get everyone else to create a MySQL RDS as well

# Demo 2
Modify the Security Group for the RDS to include SSH from anywhere
Create an EC2 connected to the same network and subnet group (AND SECURITY GROUP) and install mysql-client (8.0)
`sudo apt update`
`sudo apt install mysql-client`

login to your database
`mysql -h <rds endpoint> -P 3306 -u admin -p`

# Tutorial 
Everyone access your database via your EC2 machine

# Exercise
Using info from previous Linux modules add the sql file at this location https://gitlab.com/Reece-Elder/devops-m5-rds to your mysql db
and grab the following info from it:
All movies with a runtime over 100
All movies with more than 1000 votes
All movies in order of popularity
All people with an id between 10000 - 12000
All people in name ascending order (limit to 1000)

**solution** mysql -h <rds endpoint> -P 3306 -u admin -p > file.sql

# Tutorial
Completely deleting and stopping the RDS, make sure there are no snapshots left
