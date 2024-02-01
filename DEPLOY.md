# CI/CD WORK FLOW

* Fabric is installed on the local machine, which can connect to the web servers via ssh
* Nginx configurations are done on the web servers
* On the local machine, run the following command. This command will the 3-deploy_web_static.py file:
 
```fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu```
