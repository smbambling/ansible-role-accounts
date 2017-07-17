import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_tmonkey1_user(host):
    myuser = host.group('monkeys')
    assert myuser.gid == 2000
