# ModelasService
This is a sample setup of how we can use an ML model as service using FLASK and docker

Model is housing median value prediction from : 
https://github.com/Harithac1991/DataScience_algorithms/tree/main/median_house_value_prediction

Model deployments steps  and  dockerization
https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf

test model using postman :
curl -X POST localhost/predict -H 'Content-Type: application/json'  -d  '{"input": [-1.17,0.65,-1.16,-0.90,-1.03,-0.99,-1.022,1.336,0.217,-0.03,1,0,0,0,0]}'

AWS EC2 deployement steps :
	1. SHELL : 
	chmod 400 key-file-name.pem	
	2. Shell :  do not work
	ssh -i keypair_hp1.pem publicDSN
	3. Shell :  worked
	ssh -i keypair_hp1.pem ec2-user@IP
	 actual :  ec2-user@Public IPv4 address
	Ec2-user is  <DefaultUserName>
  
GEt help from :
https://stackoverflow.com/questions/33991816/ec2-ssh-permission-denied-publickey-gssapi-keyex-gssapi-with-mic/49179792


