from fabric.api import local, settings, abort, run, cd
from fabric.operations import get, sudo
from fabric.state import env

env.user = 'iptv'
env.hosts = ['213.159.56.188:24']
site_dir = '/opt/django/ldapsite'

IPTV_SERVICE_USER = 'iptv'
WEB_GRAB_URL = 'http://www.webgrabplus.com/sites/default/files/download/SW/V2.1.0/WebGrabPlus_V2.1_install.tar.gz'
GIT_REPO_URL = 'https://github.com/Povilas1/Skynet-IPTV-With-EPG.git'


def deploy_conf():
    pass


def setup_on_webgrab():
    pass


def generate_epg():
    pass


def download_epg():
    pass


def install():
    run("sudo apt-get install -y mono-complete")
    #run('chmod g+w /opt/')

    with run('mkdir /opt/iptv-epg'):

        with cd('/opt/iptv-epg'):
            run('chown {}: -R /opt/iptv-epg'.format(IPTV_SERVICE_USER))

            with run('wget {}'.format(WEB_GRAB_URL)):
                run('tar -zxvf *.tar.gz')
                run('mv .wg++ wgpp')
                run('rm *.tar.gz')
                run('git clone https://github.com/Povilas1/Skynet-IPTV-With-EPG.git epg-repo')
                run('cp ./epg-repo/tools/WebGrab++.config.xml ./wgpp/')
                #run('./wgpp/run.sh')




def connection_test():
    run('whoami')


