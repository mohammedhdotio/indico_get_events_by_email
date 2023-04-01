### Get events by email indico plugin
This Indico plugin will let you display events linked to/managed by a specific email. you can use the result to integrate it into your other online systems.
It supports token based authentication via Authorization header.

This is my first python code so please excuse my ignorance if any and please don't hesitate to make pull requests if you have any contribution .

### Install
```bash
su - indico
source ~/.venv/bin/activate
cd ~/tmp
git clone https://github.com/mohammedhdotio/indico_get_events_by_email.git
cd indico_get_events_by_email
pip install . 
```

### Config
- From Administration choose Plugins -> Get Events by Email
- Set your token and save settings

### Usage
```bash
curl -H "Authorization: TOKEN-HERE" https://events.yourdomain.com/get_events_by_email/email@yourdomain.com
```
- Don't forget to replace your token as well as the email of user you inquire on.

