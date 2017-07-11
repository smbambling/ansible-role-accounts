import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_tmonkey1_user(host):
    myuser = host.user('tmonkey1')
    assert myuser.uid == 1006
    assert 'tmonkey1' in myuser.groups
    assert 'wheel' in myuser.groups
    assert myuser.gecos == 'Test Monkey 1'
    assert myuser.home == '/home/tmonkey1'


def test_tmonkey1_authkeys(host):
    file = host.file('/home/tmonkey1/.ssh/authorized_keys')
    assert file.contains("ssh-dss FAKEKEYSUTFF== tmonkey1")


def test_tmonkey2_user(host):
    myuser = host.user('tmonkey2')
    assert myuser.uid == 1007
    assert 'tmonkey2' in myuser.groups
    assert 'wheel' in myuser.groups
    assert myuser.gecos == 'Test Monkey 2'
    assert myuser.home == '/home/tmonkey2'


def test_tmonkey2_authkeys(host):
    file = host.file('/home/tmonkey2/.ssh/authorized_keys')
    assert file.contains("ssh-dss FAKEKEYSUTFF== tmonkey2")


def test_tmonkey3_user(host):
    myuser = host.user('tmonkey3')
    assert myuser.uid == 1008
    assert 'monkeys' in myuser.groups
    assert 'wheel' in myuser.groups
    assert myuser.gecos == 'Test Monkey 3'
    assert myuser.home == '/home/tmonkey3'


def test_tmonkey3_authkeys(host):
    file = host.file('/home/tmonkey3/.ssh/authorized_keys')
    assert file.contains("ssh-dss FAKEKEYSUTFF== tmonkey3")
