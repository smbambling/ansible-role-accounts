# Accounts

[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-smbambling.accounts-blue.svg)](https://galaxy.ansible.com/smbambling/accounts/)
[![Build Status](https://travis-ci.org/smbambling/ansible-role-accounts.svg?branch=master)](https://travis-ci.org/smbambling/ansible-role-accounts)
[![CodeClimate](https://codeclimate.com/github/smbambling/ansible-role-accounts/badges/gpa.svg)](https://codeclimate.com/github/smbambling/ansible-role-accounts)
[![IssueCount](https://codeclimate.com/github/smbambling/ansible-role-accounts/badges/issue_count.svg)](https://codeclimate.com/github/smbambling/ansible-role-accounts)

## Table of Contents

1. [Overview](#overview)
1. [Requirements](#requirements)
1. [Role Variables](#role-variables)
1. [Dependencies](#dependencies)
1. [Examples](#example-playbooks)
1. [Development / Contributing](#development--contributing)
1. [License](#license)
1. [Author Information](#author-information)

## Overview

Generic user account and group management

## Requirements

This role requires Ansible 2.1 or higher and platform requirements are
listed in the [metadata](meta/main.yml) file.

## Role Variables

The variables that can be passed to this role and a brief description about
them are as follows. (For all variables, take a look at defaults/main.yml)

| Name              | Default | Type        | Description         |
| ------------------|---------| ------------| --------------------|
| `accounts_groups` | -       | Array       | List of unix groups |
| `accounts_users`  | -       | Array       | List of unix users  |

### Accounts_Groups

All parameters for defining a group within the `accounts_group` array variable
are inline with parameters defined in the
[Group Module](http://docs.ansible.com/ansible/group_module.html)

### Accounts_Users

Parameters for defining a user within the `accounts_users` array variable
trend to the defaults listed in the
[User Module](http://docs.ansible.com/ansible/user_module.html)
unless stated below

| Name              | Default | Type        | Notes         |
| ------------------|---------| ------------| --------------------|
| create_home       | True        | Boolean     | A home directory is set to be created by default |
| group             | `item.name` | String  | The primary user group is set to be the same value as the user namee.  If a gropu that doesn't match the user name is desired it must be created within the `accounts_groups` array or be already available on the system.          |
| groups            | -           | Array   | A list of additional groups the user is a memeber of |
| password          | `item.password` | String/Hash | If a single crypted value is supplied it sets the users password to that value. There are different crypted methods for various operating systems, thus a hash can be created based on the `ansible_os_family`.  See the below example Playbooks
| uid               | -           | Int     | A UID value must be supplied to create a group with the same GID as the user UID |

## Dependencies

None

## Example Playbook(s)

The `accounts_groups` and `accounts_users` list varaiables can be
declared at any precedence level.
For the most flexibility my recomendation is to declare them at the
inventory group\_vars level

### Using in-line Playbook Variables

```yaml
---
- name: Accounts Testing Playbook
  hosts: all

  vars:
    accounts_groups:
      - name: monkeys
        gid: 2000
    accounts_users:
      - name: tmonkey1
        comment: 'Test Monkey 1'
        uid: 1006
        password:
          OpenBSD: "$2b$08$3eBhGgrLIXZP8Ewh8tqXtuh38M463K2rKYJSyUgATRKQNX70b2jyG"
          FreeBSD: "$1$N0JqVxf/$iSmuQ6lyKB/GJUe52DqFw/"
          RedHat: "$1$N0JqVxf/$iSmuQ6lyKB/GJUe52DqFw/"
        groups:
          - wheel
        authorized_keys:
          - key: 'ssh-dss FAKEKEYSUTFF== tmonkey1'
            state: present
      - name: tmonkey2
        comment: 'Test Monkey 2'
        uid: 1007
        password:
          OpenBSD: "$2b$08$3eBhGgrLIXZP8Ewh8tqXtuh38M463K2rKYJSyUgATRKQNX70b2jyG"
          FreeBSD: "$1$N0JqVxf/$iSmuQ6lyKB/GJUe52DqFw/"
          RedHat: "$1$N0JqVxf/$iSmuQ6lyKB/GJUe52DqFw/"
        groups:
          - wheel
        authorized_keys:
          - key: 'ssh-dss FAKEKEYSUTFF== tmonkey2'
            state: present
      - name: tmonkey3
        comment: 'Test Monkey 3'
        uid: 1008
        password: "$1$N0JqVxf/$iSmuQ6lyKB/GJUe52DqFw/"
        group: monkeys
        groups:
          - wheel
        authorized_keys:
          - key: 'ssh-dss FAKEKEYSUTFF== tmonkey3'
            state: present

  roles:
    - {role: ansible-role-accounts}
```

## Development / Contributing

See [Contributing](.github/CONTRIBUTING.md).

Note: This role is currently only tested against the following OS and Ansible versions:

### Operating Systems / version

- CentOS 6.x
- CentOS 7.x

### Ansible Versions

- 2.1.0
- 2.2.2
- latest

## License

Licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Author Information

- Steven Bambling
