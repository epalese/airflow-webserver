# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages, Command
from setuptools.command.test import test as TestCommand

import imp
import logging
import os
import pip
import sys


class Tox(TestCommand):
    user_options = [('tox-args=', None, "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = ''
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(args=self.tox_args.split())
        sys.exit(errno)


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


async = [
    'greenlet>=0.4.9',
    'eventlet>= 0.9.7',
    'gevent>=0.13'
]
azure = ['azure-storage>=0.34.0']
sendgrid = ['sendgrid>=5.2.0']
celery = [
    'celery>=4.0.0',
    'flower>=0.7.3'
]
cgroups = [
    'cgroupspy>=0.1.4',
]
crypto = ['cryptography>=0.9.3']
dask = [
    'distributed>=1.15.2, <2'
    ]
databricks = ['requests>=2.5.1, <3']
datadog = ['datadog>=0.14.0']
doc = [
    'sphinx>=1.2.3',
    'sphinx-argparse>=0.1.13',
    'sphinx-rtd-theme>=0.1.6',
    'Sphinx-PyPI-upload>=0.2.1'
]
docker = ['docker-py>=1.6.0']
emr = ['boto3>=1.0.0']
gcp_api = [
    'httplib2',
    'google-api-python-client>=1.5.0, <1.6.0',
    'oauth2client>=2.0.2, <2.1.0',
    'PyOpenSSL',
    'google-cloud-dataflow',
    'pandas-gbq'
]
hdfs = ['snakebite>=2.7.8']
webhdfs = ['hdfs[dataframe,avro,kerberos]>=2.0.4']
jira = ['JIRA>1.0.7']
hive = [
    'hive-thrift-py>=0.0.1',
    'pyhive>=0.1.3',
    'impyla>=0.13.3',
    'unicodecsv>=0.14.1'
]
jdbc = ['jaydebeapi>=1.1.1']
mssql = ['pymssql>=2.1.1', 'unicodecsv>=0.14.1']
mysql = ['mysqlclient>=1.3.6']
rabbitmq = ['librabbitmq>=1.6.1']
oracle = ['cx_Oracle>=5.1.2']
postgres = ['psycopg2>=2.7.1']
ssh = ['paramiko>=2.1.1']
salesforce = ['simple-salesforce>=0.72']
s3 = [
    'boto>=2.36.0',
    'filechunkio>=1.6',
]
samba = ['pysmbclient>=0.1.3']
slack = ['slackclient>=1.0.0']
statsd = ['statsd>=3.0.1, <4.0']
vertica = ['vertica-python>=0.5.1']
ldap = ['ldap3>=0.9.9.1']
kerberos = ['pykerberos>=1.1.13',
            'requests_kerberos>=0.10.0',
            'thrift_sasl>=0.2.0',
            'snakebite[kerberos]>=2.7.8',
            'kerberos>=1.2.5']
password = [
    'bcrypt>=2.0.0',
    'flask-bcrypt>=0.7.1',
]
github_enterprise = ['Flask-OAuthlib>=0.9.1']
qds = ['qds-sdk>=1.9.6']
cloudant = ['cloudant>=0.5.9,<2.0'] # major update coming soon, clamp to 0.x
redis = ['redis>=2.10.5']

all_dbs = postgres + mysql + hive + mssql + hdfs + vertica + cloudant
devel = [
    'click',
    'freezegun',
    'jira',
    'lxml>=3.3.4',
    'mock',
    'moto',
    'nose',
    'nose-ignore-docstring==0.2',
    'nose-timer',
    'parameterized',
    'qds-sdk>=1.9.6',
    'rednose',
    'paramiko',
    'requests_mock'
]
devel_minreq = devel + mysql + doc + password + s3 + cgroups
devel_hadoop = devel_minreq + hive + hdfs + webhdfs + kerberos
devel_all = devel + all_dbs + doc + samba + s3 + slack + crypto + oracle + docker + ssh

version = imp.load_source('airflow-webserver.version', 'version.py').version

def do_setup():
	setup(
		name='airflow-webserver',
		description='Airflow Webserver',
		version=version,
		packages=find_packages(exclude=['tests*']),
		zip_safe=False,
		url='https://github.com/wepay/airflow-webserver.git',
		install_requires=[
            'airflow>=1.9.0'
            'alembic>=0.8.3, <0.9',
            'bleach==2.0.0',
            'configparser>=3.5.0, <3.6.0',
            'croniter>=0.3.17, <0.4',
            'dill>=0.2.2, <0.3',
            'flask>=0.11, <0.12',
            'flask-admin==1.4.1',
            'flask-cache>=0.13.1, <0.14',
            'flask-login==0.2.11',
            'flask-swagger==0.2.13',
            'flask-wtf==0.14',
            'funcsigs==1.0.0',
            'future>=0.16.0, <0.17',
            'gitpython>=2.0.2',
            'gunicorn>=19.3.0, <19.4.0',  # 19.4.? seemed to have issues
            'jinja2>=2.7.3, <2.9.0',
            'lxml>=3.6.0, <4.0',
            'markdown>=2.5.2, <3.0',
            'pandas>=0.17.1, <1.0.0',
            'psutil>=4.2.0, <5.0.0',
            'pygments>=2.0.1, <3.0',
            'python-daemon>=2.1.1, <2.2',
            'python-dateutil>=2.3, <3',
            'python-nvd3==0.14.2',
            'requests>=2.5.1, <3',
            'setproctitle>=1.1.8, <2',
            'sqlalchemy>=0.9.8',
            'tabulate>=0.7.5, <0.8.0',
            'thrift>=0.9.2',
            'zope.deprecation>=4.0, <5.0',
        ],
        extras_require={
            'all': devel_all,
            'all_dbs': all_dbs,
            'async': async,
            'azure': azure,
            'celery': celery,
            'cgroups': cgroups,
            'cloudant': cloudant,
            'crypto': crypto,
            'dask': dask,
            'databricks': databricks,
            'datadog': datadog,
            'devel': devel_minreq,
            'devel_hadoop': devel_hadoop,
            'doc': doc,
            'docker': docker,
            'emr': emr,
            'gcp_api': gcp_api,
            'github_enterprise': github_enterprise,
            'hdfs': hdfs,
            'hive': hive,
            'jdbc': jdbc,
            'kerberos': kerberos,
            'ldap': ldap,
            'mssql': mssql,
            'mysql': mysql,
            'oracle': oracle,
            'password': password,
            'postgres': postgres,
            'qds': qds,
            'rabbitmq': rabbitmq,
            's3': s3,
            'salesforce': salesforce,
            'samba': samba,
            'sendgrid' : sendgrid,
            'slack': slack,
            'ssh': ssh,
            'statsd': statsd,
            'vertica': vertica,
            'webhdfs': webhdfs,
            'jira': jira,
            'redis': redis,
        },
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Topic :: System :: Monitoring',
        ],
        cmdclass={
            'test': Tox,
            'extra_clean': CleanCommand,
        },
	)

if __name__ == "__main__":
	do_setup()