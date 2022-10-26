# Lesson 
Go through Playbook slides (add more detail here)
https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html

# Tutorial
Go through the following plays in our playbook yaml

```yaml
- hosts: all
  tasks:
  - name: 'Install wget'
    apt: 
      name: wget
      state: latest
      update_cache: true

- hosts: demo
  tasks:
  - name: 'Install unzip'
    apt:
      name: unzip
      state: latest
      update_cacheL: true
```
`ansible-playbook -i inventory.yaml playbook.yaml`

Explain state within ansible apt (absent, build-dep, latest, present, fixed)

# Exercise 
Create two fresh EC2 machines (A, B)
Using ansible install nginx on both machines
install unzip on machine A and wget on machine B


# Useful Commands Tutorial
Ansible has a number of command blocks that can be used to set up your environment:

service - set the desired state of a service
debug - print some message to the console
copy - copies a file to the host
script - runs a local script on a remote node after transferring it
register - A tasks JSON object can be 'registered' as a variable for use 

```yaml
- hosts: nginx
  become: true
  tasks:
  - name: 'Install nginx'
    apt:
      name: nginx
      state: latest
      update_cache: true

  - name: 'adding new nginx.conf'
    copy:
      src: nginx.conf
      dest: /etc/nginx/nginx.conf

  - name: 'Restarting nginx service'
    service:
      name: nginx
      state: started

  - name: 'sanity test'
    debug:
      msg: "nginx started"

  - name: 'running a script on remote machine'
    script: ./cool-script.sh
    register: script_output

  - name: 'printing variable'
    debug:
      msg: "{{ script_output }}
```

Useful - adding -v, -vv, -vvv during your playbook adds more information (verbose)

# Exercise 
Using ansible do the following: 
- Install nginx on a new machine and replace the default html with a new file 
- Restart the nginx service
- print out the JSON object of installing nginx 
- Uninstall nginx 
- install docker

