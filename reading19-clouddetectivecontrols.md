# Reading 19: Cloud Detective Controls 

### [Article Links]
- [What is Amazon GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [AWS re:Inforce 2019: Threat Detection on AWS: and Introduction to Amazon GuardDuty (FND216)](https://www.youtube.com/watch?v=czsuZXQvD8E&ab_channel=AmazonWebServices)

### What are some of the IoCs that GuardDuty can detect? 
- Some of the IoCs that GuardDuty can detect are: Unauthorized Access, Malicious IP Addresses, Compromised EC2 Instances, and Data Exfiltration just to name a few. 

### What are some of the data sources which GuardDuty can use? 
- Some of the data sources that GuardDuty can use are VPC Flow Logs, DNS Logs, CloudTrail Logs, etc. 

### How does GuardDuty use access behavior to spot potential malicious activity? 
- GuardDuty analyzes sources to identify malicious, unauthorized, or unexpected behavior in your Amazon Web Services accounts and workloads. For example for VPC Flow Logs, GuardDuty analyzes the log for unusual patterns, connections to malicious IP address, etc. 

## Things I Want to Know More About 
- I think what I want to know more about is GuardDuty just another way to read the logs because after going through CloudTrail and CloudWatch yesterday and it didn't seem that hard to really see what was going on after downloading the JSON and CSV files, so I'm curious if GuardDuty is just another way to look at that. 

