from fabric.api import local, settings, abort, run, cd
from fabric.operations import get, sudo, put
from fabric.state import env

env.user = 'iptv'
env.hosts = ['213.159.56.188:24']

IPTV_SERVICE_USER = 'iptv'
WEB_GRAB_URL = 'http://www.webgrabplus.com/sites/default/files/download/SW/V2.1.0/WebGrabPlus_V2.1_install.tar.gz'
GIT_REPO_URL = 'git@github.com:Povilas1/Skynet-IPTV-With-EPG.git'

BASE_DIR = '/opt/iptv-epg'  # arbitrary directory in which your store files
WG_DIR = '/opt/iptv-epg/wgpp'
REPO_DIR = '/opt/iptv-epg/epg-repo'


def generate_epg():
    pass


def deploy_config():
    """Deploys config edits to WG++ generator"""
    run('cp {}/tools/WebGrab++.config.xml {}'.format(REPO_DIR, WG_DIR))


def deploy():
    with cd('{}'.format(REPO_DIR)):
        run('git pull origin master')


def download_epg(local_path='/tmp'):
    """copies epg from the generator machine."""
    remote_path = "{}/guide.xml".format(WG_DIR)
    get(remote_path=remote_path, local_path=local_path, use_sudo=True)


def commit():
    local("git add -p && git commit")


def amend():
    local("git add -p && git commit --amend")


def push():
    local("git push origin dev")


def commit_master(do_deploy=True):
    local("git pull origin master")
    commit()
    local("git checkout master")
    local("git pull origin master")
    local("git merge dev")
    local("git push origin master")
    if do_deploy:
        deploy()
        deploy_config()


def commit_local():
    commit()
    push()


def connection_test():
    run('whoami')


# one time functions

def install_script(mod=751, install_dir='/usr/bin'):
    target_script = "{}/tools/make-epg.sh".format(REPO_DIR)
    run("chmod {} {}".format(mod, target_script))
    run("ln -s {} {}".format(target_script, install_dir))


def install_service(local_path='./make-epg.service'):
    put(local_path=local_path, remote_path='/etc/systemd/system', use_sudo=True)


def install_timer(local_path='./make-epg.timer'):
    put(local_path=local_path, remote_path='/etc/systemd/system', use_sudo=True)


def enable_service(service_name='make-epg.service'):
    sudo("systemctl enable {}".format(service_name))


def enable_timer(service_name='make-epg.timer'):
    sudo("systemctl enable {}".format(service_name))


def start_service(service_name='make-epg.service'):
    sudo("systemctl start {}".format(service_name))


def start_timer(service_name='make-epg.timer'):
    sudo("systemctl start {}".format(service_name))


def service_status(service_name='make-epg.service'):
    run('systemctl status {}'.format(service_name))


def service_log(service_name='make-epg.service'):
    run('journalctl -f -u {}'.format(service_name))


def timer_status(timer_name='make-epg.timer'):
    run('systemctl status {}'.format(timer_name))
    run('systemctl list-timers --all')


def install_timed_service(do_start_service=False, monitor=True):
    install_script()
    install_service()
    install_timer()
    enable_service()
    enable_timer()
    if do_start_service:
        start_service()
    start_timer()
    if monitor:
        service_status()
        timer_status()


def install_epg():
    run("sudo apt-get install -y mono-complete")

    with run('mkdir /opt/iptv-epg'):
        with cd('/opt/iptv-epg'):
            with run('wget {}'.format(WEB_GRAB_URL)):
                run('tar -zxvf *.tar.gz')
                run('mv .wg++ wgpp')
                run('rm *.tar.gz')
                run('git clone {} epg-repo'.format(GIT_REPO_URL))
                run('cp ./epg-repo/tools/WebGrab++.config.xml ./wgpp/')


