# Reading 42: Pass the Hash with Mimikatz

### Article Links: 
- [What is Mimikatz?](https://www.varonis.com/blog/what-is-mimikatz/)

### Name the six credential-gathering techniques which Mimikatz is able to perform and explain how two of them work.
- Pass-the-hash: Mimikatz uses stored NTLM hash strings to log in without needing to crack the password.
- Pass-the-ticket: Mimikatz allows passing Kerberos tickets to log in as another user
- Overpass-the-hash (pass-the-key): Mimikatz passes unique keys from a domain controller to impersonate a user.
- Kerberoast golden tickets: Mimikatz creates non-expiring domain admin credentials.
- Kerberoast silver tickets: Mimikatz exploits Window feature to use service accounts on the network.
- Pass-the-cache: Mimikatz exploits saved and encrypted login data on non-Windows systems. 
### What are four ways we can defend against Mimikatz attacks. Explain how two of the mitigations can stop Mimikatz.
- Restrict admin privileges 
- Disable password caching: Prevent Mimikatz from accessing recently used password hashes by setting cache to zero recent passwords. 
- Turn off debug privileges
- Configure additional LSA protection: Upgrade to windows 10 or utilize additional LSA configuration items to mitigate authentication attacks enabled by Mimikatz. 