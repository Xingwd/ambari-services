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

import glob
import os

from resource_management import *


class MlSql(Script):
  def install(self, env):
    pass


  def create_seasbase_log_dir(self, env):
    import params
    env.set_params(params)
    Directory([params.seasbase_log_dir],
              owner=params.seasbase_user,
              group=params.seasbase_group,
              cd_access="a",
              create_parents=True,
              mode=0755
              )
			  
			  
  def create_seasbase_pid_dir(self, env):
    import params
    env.set_params(params)
    Directory([params.seasbase_pid_dir],
              owner=params.seasbase_user,
              group=params.seasbase_group,
              cd_access="a",
              create_parents=True,
              mode=0755
            )

    Execute(("chown", "-R", format("{seasbase_user}") + ":" + format("{seasbase_group}"), params.seasbase_pid_dir),
            sudo=True)			

  
  def configure(self, env):
    self.create_seasbase_log_dir(env)
    self.create_seasbase_pid_dir(env)


  def stop(self, env):
    import params
    self.create_seasbase_log_dir(env)
    self.create_seasbase_pid_dir(env)
    Execute(params.seasbase_dir + '/bin/mlsql stop', user=params.seasbase_user)


  def start(self, env):
    import params
    self.configure(env)
    
    Execute(params.seasbase_dir + '/bin/mlsql start', user=params.seasbase_user)

    pidfile = glob.glob(os.path.join(params.mlsql_pid_file))[0]
    Logger.info(format("Pid file is: {pidfile}"))


  def status(self, env):
    import params
    env.set_params(params)

    try:
        pid_file = glob.glob(params.mlsql_pid_file)[0]
    except IndexError:
        pid_file = ''
    check_process_status(pid_file)

if __name__ == "__main__":
  MlSql().execute()
