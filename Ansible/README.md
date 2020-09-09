*Usage of ansible playbooks*

Web.yml , rabbitmq.yml, postgresql is a ansible playbook for Creating HTTPD server, rabbit mq application, postgresql application respectively and making sure services up and running 

Below is the command used for running playbook for apache(httpd), Rabbitmq.yml, postgresql.yml
 1. ansible-playbook -i ansible.cfg web.yml -e "ansible_mounts=mount_name"
 2. ansible-playbook -i ansible.cfg rabbitmq.yml -e "ansible_mounts=mount_name"
 3. ansible-playbook -i ansible.cfg postgresqlstatuscheck.yml -e "ansible_mounts=mount_name"
  
  provide mount_name

*Assumptions*

1. All hosts (host1, host2, host3) are linux.
2. All three are running in three differnt machines
3. Requires mount_name mandatory


