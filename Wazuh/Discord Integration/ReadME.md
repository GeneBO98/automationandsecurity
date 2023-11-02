# Purpose
I created this custom_discord.py file so that I could get good and reliable alerts from Wazuh into Discord. If you create this integration without these changes, you will get alerts for every single security event created in Wazuh. That may be what you want, but I don't think that makes much sense. I want to be alerted when there is actually something that I should pay attention to.

## Environment
I have this configured specifically to ignore some mundane and common alerts that I was getting with a Windows 2019 FS and DC. I also made some changes in my Sysmon configuration on these servers. Which I have included in the Wazuh folder.

## Ossec.conf
```
  <integration>
    <name>custom-discord</name>
    <hook_url>**webhook for lower-level alerts**</hook_url>
    <level>7</level>
    <alert_format>json</alert_format>
  </integration>
  
  <integration>
    <name>custom-discord</name>
    <hook_url>**webhook for critical alerts**</hook_url>
    <level>12</level>
    <alert_format>json</alert_format>
  </integration>
```
I created 2 different integration entries for Discord so that I could have one chat with muted alerts that will collect most of the alerts that I may want to look at. But then reserve a chat for things that are level 12 and higher.

## Location for discord files on Wazuh VM
/var/ossec/integrations/
