import pytest
import re
import os

from packaging.version import Version

import testinfra.utils.ansible_runner

@pytest.fixture(scope='session')
def host(request):
    # TODO: change hardcoded value to pull from Molecule environment
    yield testinfra.get_host("docker://ubuntu")

def parse_version(output_version, version_regex):
    match = re.match(version_regex, output_version.split("\n")[0])
    if match is None:
        return -1
    return match.group(1)

@pytest.mark.parametrize("name", [
    ("ansible"),
    ("apt-transport-https"),
    ("ca-certificates"),
    ("containerd.io"),
    ("curl"),
    ("discord"),
    ("docker-buildx-plugin"),
    ("docker-ce"),
    ("docker-ce-cli"),
    ("docker-compose-plugin"),
    ("firefox-esr"),
    ("fuse"),
    ("g++"),
    ("gcc"),
    ("git"),
    ("gnupg"),
    ("golang-go"),
    ("google-chrome-stable"),
    ("nodejs"),
    ("openssl"),
    ("python3"),
    ("sqlite3"),
    ("software-properties-common"),
    ("stow"),
    ("telegram-desktop"),
    ("tmux"),
    ("wget"),
    ("vim")
])
def test_apt_packages(host, name):
    assert host.package(name).is_installed

@pytest.mark.parametrize("name, minimum_version, version_args, version_regex", [
    # ansible [core 2.15.4]
    ("ansible", "2.15.4", "--version", r"^ansible \[core (\d+[.]\d+[.]\d+)]$"),
    # OpenSSL 3.0.2 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)
    ("openssl", "3.0.2", "version", r"^OpenSSL (\d+[.]\d+[.]\d+).*$"),
    # v20.8.0
    ("nodejs", "20.8.0", "--version", r"^v(\d+[.]\d+[.]\d+)$"),
    # go version go1.18.1 linux/amd64
    ("go", "1.18.1", "version", r"^go version go(\d+[.]\d+[.]\d+).*$"),
    # Python 3.10.12
    ("python3", "3.10.12", "--version", r"^Python (\d+[.]\d+[.]\d+)$"),
    # VIM - Vi IMproved 8.2 (2019 Dec 12, compiled Oct 06 2023 07:49:43)
    ("vim", "8.2", "--version", r"^VIM - Vi IMproved (\d+[.]\d+).*$"),
    # NVIM v0.9.2
    ("nvim", "0.9.2", "--version", r"^NVIM v(\d+[.]\d+[.]\d+)$")
])
def test_package_versions(host, name, minimum_version, version_args, version_regex):
    output_version = host.check_output(f"{name} {version_args}")
    parsed_version = parse_version(output_version, version_regex)
    assert(parsed_version != -1)
    assert(Version(parsed_version) >= Version(minimum_version))
