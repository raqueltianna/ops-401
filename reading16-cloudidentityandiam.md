# Reading 16: Cloud Identity and Access Management (IAM) with AWS 

### Article Links: 
[ Lessons Learned from the Capital One Data Breach (PDF)](https://www.zscaler.com/resources/white-papers/capital-one-data-breach.pdf)

### What were the three commands used for the attack?
- **Get Credentials** : First command when executed it obtained security credentials 
- **List Buckets** : Second command when executed it used the security credentials 
- **Download Files** : Third command, when executed used the account to download files that were accessible by the credentials. 

### What misconfiguration of AWS components allowed the attacker to access sensitive data? 
- The misconfiguration error at the application layer of a firewall installed by the Financial Institution. The permissions set were also broader than likely intended which exacerbated the misconfiguration further. 

### What are two of the AWS Governance practices that could have prevented such attack? 
- Use CloudTrail, CloudWatch, and/or AWS lambda services to review and automate specific actions taken on S3 resources. 
- Don't allow EC2 instances to have IAM roles that allow attaching or replacing role policies in any production environment. 

### Things I want to know more about: 
- I understand that you have a lot of power in setting everything up on AWS for yourself but I don't understand how there isn't things in place in AWS automatically that prevents this but maybe I'm just looking at that part wrong. 