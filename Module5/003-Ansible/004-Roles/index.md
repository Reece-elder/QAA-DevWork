# Lesson
Go through slides

# Tutorial
Roles are executable collections of tasks for achieving objectives
They are used to containerise a collection of tasks to achieve one object (installing Docker?)
Roles have a lot of specific structure needed to work

directory structure can be created automatically through `ansible-galaxy init <role name>`

*create roles for nginx and docker*
``` yaml
# Put tasks in nginx tasks file
  - name: 'Copy nginx conf'
    copy: 
      src: nginx.conf
      dest: /etc/nginx/nginx.conf
    notify: "Restart nginx"

  - name: "Copy html files to where they will be served"
    copy:
      src: index.html
      dest: /usr/nginx/share/html/index.html
    notify: "Restart nginx"

# Add handler to handler file
  handlers:
  - name: "Restart nginx"
    service:
      name: nginx
      state: restarted
    

# Add tasks to docker tasks
  - name: 'Install aptitude'
    apt: 
      name: aptitude
      state: latest
      update_cache: true
      
  - name: 'Install required packages'
    apt: 
      pkg:
        - apt-transport-https
        - ca-certificates
        - curl
        - software-properties-common
        - python3-pip
        - virtualenv
        - python3-setuptools
      state: latest
      update_cache: true

  - name: 'Add docker GPG apt key'
    apt_key: 
      url: https://download.docker.com/linux/ubuntu/gpg
      state: present

  - name: 'Add Docker Repository'
    apt_repository: 
      repo: deb https://download.docker.com/linux/ubuntu focal stable
      state: present

  - name: 'Update apt and install docker -ce'
    apt: 
      name: docker-ce
      state: latest
      update_cache: true

  - name: 'Install docker module for python'
    pip:
      name: docker

# Add to main playbook.yaml
- hosts: all
  become: true
  roles:
  - nginx
  - docker
```

# Exercise 
Create roles for the following: 
- Create a group called developers and add a new user with your name, install zsh shell and curl
- Install Docker 
- Install jenkins 
- Using nginx to create a webserver which hosts a custom index.html
