from fabric.api import local, settings, abort, run, cd
from fabric.operations import get, sudo
from fabric.state import env

env.user = 'iptv'
env.hosts = ['213.159.56.188:24']
site_dir = '/opt/django/ldapsite'

IPTV_SERVICE_USER = 'iptv'
WEB_GRAB_URL = 'http://www.webgrabplus.com/sites/default/files/download/SW/V2.1.0/WebGrabPlus_V2.1_install.tar.gz'
GIT_REPO_URL = 'https://github.com/Povilas1/Skynet-IPTV-With-EPG.git'


def generate_epg():
    with run('cd /opt/iptv-epg'):
        run('cp ./guide.xml /opt/iptv-epg/epg-repo/')

    # cp guide.xml ../epg-repo/
    # cd /opt/iptv-epg/epg-repo/
        # git add guide.xml
        # git commit -m "epg update for {}"
        # git push origin master

def deploy_config():
    pass

def download_epg():
    pass


def download_webgrab():
    with run('wget {}'.format(WEB_GRAB_URL)):
        run('tar -zxvf *.tar.gz')
        run('mv .wg++ wgpp')
        run('rm *.tar.gz')
        run('git clone {} epg-repo'.format(GIT_REPO_URL))
        run('cp ./epg-repo/tools/WebGrab++.config.xml ./wgpp/')
        run('./wgpp/install.sh')


def install():
    run("sudo apt-get install -y mono-complete")

    with run('mkdir /opt/iptv-epg'):
        with cd('/opt/iptv-epg'):
            download_webgrab()


def connection_test():
    run('whoami')


