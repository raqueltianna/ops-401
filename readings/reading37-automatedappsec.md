# Reading 37: Automated AppSec with ZAP

### Article Links
- [Getting Started with Zed Attack Proxy](https://www.zaproxy.org/getting-started/)
- [Python Tools for Cyber](https://hackersonlineclub.com/python-tools/)

### What are the three common stages of the Penetration Testing process and what tasks are performed at each one?
- Explore: Here the tester attempts to gather information about he target or application like identifying software version or patches. 
- Attack: Here the tester attempts to exploit known or possible vulnerabilities discovered during the explore phase. Different techniques are used like SQL inject or XSS as example.
- Report: This happens after the attack phase where the tester creates a report of their findings. They document things like vulnerabilities discovered and recommendations for fixing or mitigating said vulnerabilities
### Explain a “man-in-the-middle proxy” in non-technical terms.
- A man-in-the-middle proxy is like a security guard if you are in jail. If someone sends you a letter from outside of jail, a security guard can read the letter, cross out words and change the content before the letter ever got to you. MITM proxy is similar because it intercepts and and inspects the communication between your browser and website. 
### What are the 2 spiders available for use in ZAP?
- The 2 spiders available for in ZAP are a traditional ZAP spider and Zap's AJAX Spider. 
### What situations are they best suited for?
- Traditional ZAP spider: This is best suited for traditional web applications where the content is generated in server-side HTML response.
- ZAP's AJAX Spider: This is best suited for modern web apps that rely on JavaScript to generate content dynamically.