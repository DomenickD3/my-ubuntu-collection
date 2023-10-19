# my-ubuntu-collection
<!-- Add CI and code coverage badges here. Samples included below. -->
![Molecule CI](https://github.com/domenickd3/my-ubuntu-collection/actions/workflows/molecule-ci.yml/badge.svg)

<!-- Describe the collection and why a user would want to use it. What does the collection do? -->
This is a collection that works with Ubuntu 22.04. I use this to set up my entire environment from scratch.

## Tested with Ansible

<!-- List the versions of Ansible the collection has been tested with. Must match what is in galaxy.yml. -->
molecule testing was performed with ansible 2.15.4

## Included content
<!-- Galaxy will eventually list the module docs within the UI, but until that is ready, you may need to either describe your plugins etc here, or point to an external docsite to cover that information. -->

This module contains an "install" role which installs all the packages which I use.

Additionally it contains a "configure" role which pulls down my dotfiles and uses stow to link them in my home directory.


## Using this collection

<!--Include some quick examples that cover the most common use cases for your collection content. It can include the following examples of installation and upgrade (change NAMESPACE.COLLECTION_NAME correspondingly):-->

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install domenickd3.my_ubuntu_collection
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: domenickd3.my_ubuntu_collection
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install domenickd3.my_ubuntu_collection --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```bash
ansible-galaxy collection install domenickd3.my_ubuntu_collection:==0.1.0
```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## More information

<!-- List out where the user can find additional information, such as working group meeting times, slack/IRC channels, or documentation for the product this collection automates. At a minimum, link to: -->

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible Collections Checklist](https://github.com/ansible-collections/overview/blob/main/collection_requirements.rst)

## Licensing
GNU General Public License v2.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-2.0.txt) to see the full text.
