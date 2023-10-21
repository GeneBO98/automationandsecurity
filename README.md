# automationandsecurity
A general repository for light automation tasks as well as security implementations in a home lab or small business

These automation tasks assume a few things:

1. That the machine running the playbooks has SSH keys configured for these connections
2. That there is a user called **update** on each of the servers in the inventory file, which has *sudo* privileges


## Creating the update user
I created a user on each server I wanted to manage with the name of update:

```bash
sudo useradd -m update
```

I then set the password (the same for all servers, but make it damn secure)

```bash
sudo passwd update
```
Enter a very strong password, as it will be shared with multiple Linux boxes.

Then you can add to sudo group:

```bash
sudo usermod -aG sudo update
```

Now you can generate the SSH key used to connect.

## Generating SSH keys and transferring to target machines
### Generate Key
You really only have to do this once on the machine that will be the central point for management.
```bash
ssh-keygen -b 4096
```

Save that to the default location and set a password for it.

### Transfer keys
Transfer the keys to the servers that should be managed.
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server_ip
```
You will have to accept their key and authenticate to these servers. Then you can ssh to them without having to enter the password. As long as you don't lose that private id_rsa key. This will work out well with Ansible.
