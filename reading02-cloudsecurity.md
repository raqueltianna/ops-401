# Reading 02: Cloud Security Principles and Framework

### Article Links 
- [AWS Architecture Blog - Compute Abstractions on AWS: A Visual Story](https://aws.amazon.com/blogs/architecture/compute-abstractions-on-aws-a-visual-story/)

### Explain the levels of abstraction in AWS to someone without a technical background.
- The abstraction levels let users have control over the level of control and management they need for things they are doing. For example you have Virtual Servers (EC2) that let you have virtual computers in the cloud. 
### What are the control plane and data plane responsible for in container abstraction?
- The control plane is responsible for exposing API and interfaces to define, deploy, and lifecycle containers. The data plane is responsible for providing capacity so that the containers can actually run and connect to a network. 
### Where does AWS Lambda fall in the layers of abstraction and what makes it so special?
- Lambda falls under the function abstraction. What makes Lambda special is that its an event-driven model. Yolu can invoke Lambda directly or you cn trigger a function upon an event in another AWS service. With Lambda you don't have to manage the infrastructure underneath the function.

#### Additional Resources 
- [13 Compliance Frameworks for Cloud-based Orgs](https://www.horangi.com/blog/13-compliance-frameworks-for-cloud-based-organizations)
- [Cloud Security Alliance (CSA)](https://cloudsecurityalliance.org/)
    - [Cloud Controls Matrix (CCM)](https://cloudsecurityalliance.org/research/cloud-controls-matrix/)
    - [CSA Security Guidance for Cloud Computing](https://cloudsecurityalliance.org/research/guidance/) 