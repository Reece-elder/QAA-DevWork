# Lesson 
Go through Ansible Slides up to Playbook 
go through diagram of what Ansible is

# Tutorial
Create an EC2 with ssh and http ports open and ssh into it
Run the following linux commands to install ansible 
```bash
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

using ansible install nginx
`ansible 127.0.0.1 -m apt -a "name=nginx state=present update_cache=true" --become`

check if nginx is installed by curling localhost. Then run the ansible command again and it should be a LOT QUICKER (why??)

# Exercise
Install ansible on your machine with the command 
`ansible 127.0.0.1 -m apt -a "name=nginx state=present update_cache=true" --become`
# Stretch Exercise
install mysql client using ansible
