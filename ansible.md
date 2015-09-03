## Ansible Introduction


---

## What

<br/>

* Orchestration
* Application Deployment
* System Provisioning
* SSH based

---

## Setup

<br/>

<section>
    <pre>
        <code data-trim>

brew install python
easy_install pip
pip install ansible

        </code>
    </pre>
</section>

---

## Practice 1

<br/>

<section>
    <pre>
        <code data-trim>

ansible all -m ping
ansible all -m yum -a "name=nginx state=latest"
ansible all -m service -a "name=nginx state=started"

        </code>
    </pre>
</section>

---

## Playbook

<br/>

<section>
    <pre>
        <code data-trim>
- hosts: webservers
  vars:
    http_port: 80
  user: root
  tasks:
  - name: ensure apache is at the latest version
    yum: pkg=httpd state=latest
  - name: write the apache config file
    template: src=/srv/httpd.j2 dest=/etc/httpd.conf
    notify:
    - restart apache
  - name: ensure apache is running
    service: name=httpd state=started
  handlers:
    - name: restart apache
      service: name=httpd state=restarted
        </code>
    </pre>
</section>

---

## Inventory

<br/>

<section>
    <pre>
        <code data-trim>
file: production
[atlanta-webservers]
www-atl-1.example.com
www-atl-2.example.com

[boston-webservers]
www-bos-1.example.com
www-bos-2.example.com

[atlanta-dbservers]
db-atl-1.example.com
db-atl-2.example.com

[boston-dbservers]
db-bos-1.example.com
        </code>
    </pre>
</section>

---

## Practice 2

<br/>

<section>
    <pre>
        <code data-trim>
ansible-playbook webservers -i production
        </code>
    </pre>
</section>

---

## Inventory & Playbook

<br/>

* Playbook define How to deploy
* Inventory file define where to deploy

---

## Best Practice

---

## Q & A

<br/>

* http://www.ansibleworks.com/
* http://www.ansibleworks.com/docs/patterns.html
* http://www.ansibleworks.com/docs/bestpractices.html
