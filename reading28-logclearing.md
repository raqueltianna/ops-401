# Reading 28: Log Clearing 

### Article Links
- [Log Tampering 101](https://resources.infosecinstitute.com/topic/ethical-hacking-log-tampering-101/)
- [NIST SP800-154 Guide to Data-Centric Threat Modeling](https://csrc.nist.gov/publications/detail/sp/800-154/draft#pubs-abstract-header)

### Explain some specifics of why a hacker might want to clear log files to a family member. Do not use the example from the article.
- My family is super into true crime stuff so a way I would describe it is like a diary or journal that a murder has. After they commit a crime and think that the police are on their trail they might tear out the pages and burn them so the police can't track what they were doing beforehand. Logs are like the diary of the computers so a hacker would do the same thing, try to get rid of their trail.
### What are three methods by which you can clear logs in a Windows system?
- You can use the clearlogs.exe file that can be used once the target Windows system is obtained and then run it to clear the security logs. 
- You can clear them in the Windows Event Viewer under Windows Logs in the folder tree. 
- You can also use Meterpreter which is an advanced payload that help to clear all logs in a Windows system.
### What are the four steps in the process of covering your tracks.
- The four steps are:
    - Disable auditing which eliminates the trail of evidence. 
    - Clearing logs which also remove evidence of hacking activities using some of the methods listed above. 
    - Modifying log to conceal their actions. 
    - Erasing command history which prevents admin from tracking activities. 