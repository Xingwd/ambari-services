#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import functools
import os
import re
import socket

from resource_management import *


# server configurations
config = Script.get_config()
stack_root = Script.get_stack_root()

# e.g. /var/lib/ambari-agent/cache/stacks/HDP/2.6/services/presto/package
service_packagedir = os.path.realpath(__file__).split('/scripts')[0]

presto_dirname = 'presto'
install_dir = os.path.join(stack_root, "current")


# New Cluster Stack Version that is defined during the RESTART of a Rolling Upgrade
version = default("/commandParams/version", None)
stack_name = default("/hostLevelParams/stack_name", None)


# params from presto-env
presto_user = config['configurations']['presto-env']['presto_user']
presto_group = config['configurations']['presto-env']['presto_group']
presto_log_dir = config['configurations']['presto-env']['presto_log_dir']
presto_pid_dir = config['configurations']['presto-env']['presto_pid_dir']
presto_log_file = os.path.join(presto_log_dir, 'presto.log')
presto_etc_catalog_dir = config['configurations']['presto-env']['presto_etc_catalog_dir']

presto_dir = os.path.join(*[install_dir, presto_dirname])
conf_dir = "/etc/presto/conf"

# launcher options
launcher_coordinator_options = " --etc-dir=/etc/presto/conf --config=/etc/presto/conf/coordinator.properties --data-dir=/var/presto/data --pid-file=/var/run/presto/coordinator.pid --launcher-log-file=/var/log/presto/coordinator-launcher.log --server-log-file=/var/log/presto/coordinator.log"
launcher_worker_options = " --etc-dir=/etc/presto/conf --config=/etc/presto/conf/worker.properties --data-dir=/var/presto/data --pid-file=/var/run/presto/worker.pid --launcher-log-file=/var/log/presto/worker-launcher.log --server-log-file=/var/log/presto/worker.log"



# node.properties
presto_node_properties_content = config['configurations']['node-properties']['node_properties_content']

# jvm.config
jvm_config_content = config['configurations']['jvm-config']['jvm_config_content']

# log.properties
log_properties_content = config['configurations']['log-properties']['log_properties_content']

# coordinator.properties
coordinator_properties_content = config['configurations']['coordinator-properties']['coordinator_properties_content']

# worker.properties
worker_properties_content = config['configurations']['worker-properties']['worker_properties_content']

# hive.properties
presto_hive_properties_content = config['configurations']['hive-properties']['hive_properties_content']

# node hostname
hostname = config["hostname"]

# coordinator host
presto_coordinator_hosts = default('/clusterHostInfo/presto_coordinator_host', [])
presto_coordinator_host = presto_coordinator_hosts[0] if len(presto_coordinator_hosts) > 0 else None 

# hive metastore uris
hive_metastore_uris = config['configurations']['hive-site']['hive.metastore.uris']

# detect configs
master_configs = config['clusterHostInfo']
ambari_host = str(master_configs['ambari_server_host'][0])

# e.g. 2.3
stack_version_unformatted = config['hostLevelParams']['stack_version']

# e.g. 2.3.0.0
stack_version_formatted = format_stack_version(stack_version_unformatted)
major_stack_version = get_major_version(stack_version_formatted)

# e.g. 2.3.0.0-2130
full_stack_version = default("/commandParams/version", None)
