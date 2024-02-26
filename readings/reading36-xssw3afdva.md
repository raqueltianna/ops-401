# Reading 36: XSS with w3af, DVWA

### Article Links
- [Cross-site scripting](https://portswigger.net/web-security/cross-site-scripting)

### Explain how a cross-site scripting attack works in non-technical terms.
- Cross-site scripting is like a website being the house and each room in the house is a webpage. XSS is when someone breaks into your house and then leaves a hidden message or leave graffiti on your wall. It also could be like a squatter who refuses to leave until you give them something in return.
### What are the three types of XSS attacks?
- Stored XSS: where malicious code is stored on the server and then executed when the user views the compromised page
- Reflected XSS: where malicious code is included in a URL or other input that is sent to the server then **reflected** back to the user.
- DOM-based XSS: where malicious code is executed on the client side instead of the server side
### If an attacker successfully exploits a XSS vulnerability, what malicious actions would they be able to perform?
- Deface the website, changing its content or layout 
- Redirect users to malware infected pages or phishing sites. 
- Infect the web page with malicious code 
### What are some security controls that can be implemented to prevent XSS attacks?
- Regular security updates
- Output encoding where it would encode user data before displaying it in HTML output
- Input validation and sanitization.

## Things I want to know more about: 
- I am curious about an example of malicious code that is injected into web page and specific vulnerabilities that make it possible for that code to work.
- I am also curious about how XSS differs from other vulnerabilities like SQL injection.