# Lesson
Show the Inventory and Playbook slides, explain the purpose of the two types of files
inventory - Used for the hosts and configuration of the hosts
playbook - Used for the instructions and state management

# Tutorial
Have two EC2 machines both with port 22 completely open. 
Generate a key pair on one of the machines and ensure the public key is installed in the .ssh key in the second machine

in the inventory.yaml add the following 
```yaml
all:
  children:
    demo:
      hosts:
        <IP of second machine>
      vars:
        ansible_user: ubuntu
        ansible_ssh_private_key_file: ~/.ssh/ansible_id_rsa
```

Create a playbook.yaml with the following content
```yaml
- hosts: demo
  tasks:
  - name: "Ping"
    ping:
```

Run your playbook and inventory with 
`ansible-playbook -v -i inventory.yaml playbook.yaml`

# Exercise 
Create two EC2 machines, generate an ssh key pair in machine 1 and get the public ssh key to the 2nd machine. Test you can connect to the 2nd machine by doing an ssh test `ssh -i<private key name> ubuntu@<public ip>`

Create an inventory.yaml that contains the following:
```yaml 
all:
  children:
    demo:
      hosts:
        <IP of second machine>
      vars:
        ansible_user: ubuntu
        ansible_ssh_private_key_file=~/.ssh/ansible_id_rsa
```
Create a playbook.yaml that contains the following: 
```yaml
- hosts: demo
  tasks:
  - name: "Ping"
    ping:
```

Run your playbook with `ansible-playbook -v -i inventory.yaml playbook.yaml`

# Stretch goal
Modify the playbook to install nginx, look at how we installed nginx locally in the previous section