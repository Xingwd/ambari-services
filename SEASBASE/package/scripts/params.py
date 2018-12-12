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

service_packagedir = os.path.realpath(__file__).split('/scripts')[0]

seasbase_dirname = 'seasbase'
install_dir = os.path.join(stack_root, "current")


# New Cluster Stack Version that is defined during the RESTART of a Rolling Upgrade
version = default("/commandParams/version", None)
stack_name = default("/hostLevelParams/stack_name", None)


# params for env
seasbase_user = 'hdfs'
seasbase_group = 'hdfs'
seasbase_log_dir = '/var/log/seasbase'
seasbase_pid_dir = '/var/run/seasbase'

mlsql_pid_file = os.path.join(seasbase_pid_dir, 'mlsql.pid')
mlsql_log_file = os.path.join(seasbase_log_dir, 'mlsql.log')
redis_pid_file = os.path.join(seasbase_pid_dir, 'redis.pid')
redis_log_file = os.path.join(seasbase_log_dir, 'redis.log')
seasbase_pid_file = os.path.join(seasbase_pid_dir, 'seasbase.pid')
seasbase_log_file = os.path.join(seasbase_log_dir, 'seasbase.log')


seasbase_dir = os.path.join(*[install_dir, seasbase_dirname])



# node hostname
hostname = config["hostname"]
