# Lesson 
Go through powerpoint slide

# Tutorial
Global Vars - accessed everywhere and set by environment variables and command line
Playbook vars - accessed anywhere within the playbook
Host vars - associated with a host, such as IP addresses or private details

```yaml
- hosts: all
  become: true
  tasks:
  - name: 'Print variable'
    debug:
      msg: "{{ name }} 

```
`ansible-playbook -i inventory playbook.yaml -e name=reece`

vars can have a default value that will use this if the variable has not been defined in any other way
```yaml
- hosts: all
  become: true
  vars:
    var_package: wget
  tasks:
  - name: 'Install chosen package'
    apt:
      name: "{{ var_package }}"
      state: latest

```

handlers can be used to make code mo4re efficient by modulising, we can remove repeating commands by using the handle command and 'notifying' the handler. Typically used for restarting services

```yaml
- hosts: all
  become: true
  tasks:

  - name: 'Copy nginx conf'
    copy: 
      src: "{{ nginx_conf }}"
      dest: /etc/nginx/nginx.conf
    notify: "Restart nginx"

  - name: "Copy html files to where they will be served"
    copy:
      src: index.html
      dest: /usr/nginx/share/html/index.html
    notify: "Restart nginx"

  handlers:
  - name: "Restart nginx"
    service:
      name: nginx
      state: restarted

```

# Exercise
using variables create a playbook which does the following:
- prints your name to the console
- clones down a repo that can be set at the command line
- installs a package that can be set at command line
- installs nginx and uses handlers to restart the service
- creates a new file and appends a line of text (chosen at command line) to the file
