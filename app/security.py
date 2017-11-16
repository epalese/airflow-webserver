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

from flask_appbuilder.security.sqla import models as sqla_models

from app import appbuilder
sm = appbuilder.sm

vms = [
    'HomeView',
    'Airflow',
    'DagModelView',
    'Browse',
    'Manage',
    'DAG Runs',
    'DagRunModelView',
    'Task Instances',
    'TaskInstanceModelView',
    'SLA Misses',
    'SlaMissModelView',
    'Jobs',
    'JobModelView',
    'Logs',
    'LogModelView',
    'Configurations',
    'ConfigurationView',
    'XComs',
    'XComModelView',
    'Connections',
    'ConnectionModelView',
    'Variables',
    'VariableModelView',
    'Pools',
    'PoolModelView',
    'Docs',
    'Documentation',
    'Github',
    'About',
    'Version',
    'VersionView',
]

security_vms = [
    'ResetPasswordView',
    'ResetMyPasswordView',
    'UserInfoEditView',
    'UserDBModelView',
    'List Users',
    'Security',
    'RoleModelView',
    'List Roles',
    'UserStatsChartView',
    'User\'s Statistics',
    'PermissionModelView',
    'Base Permissions',
    'ViewMenuModelView',
    'Views/Menus',
    'PermissionViewModelView',
    'Views/Menus',
]

viewer_perms = [
    'menu_access',
    'can_index',
    'can_list',
    'can_show',
    'can_chart',
    'can_dag_stats',
    'can_dag_details',
    'can_task_stats',
    'can_code',
    'can_log',
    'can_tries',
    'can_graph',
    'can_tree',
    'can_task',
    'can_task_instances',
    'can_xcom',
    'can_gantt',
    'can_landing_times',
    'can_duration',
    'can_blocked',
    'can_rendered',
    'can_pickle_info'
    'can_conf',
    'can_version',
    'can_refresh',
]

action_perms = [
    'this form post',
    'this form get',
    'can_dagrun_clear',
    'can_run',
    'can_dagrun',
    'can_trigger',
    'can_add',
    'can_edit',
    'can_delete',
    'can_varimport',
    'can_paused',
    'can_success',
    'can_muldelete',
    'set_failed',
    'set_running', 
    'set_success',
    'clear',

    # TODO: can_query is no longer safe since now db contains permission-related data.
    # Need to prevent certain tables from being queried.
    # 'can_query',
]

def is_viewer_pvm(pvm):
    return (pvm.view_menu.name in vms and
            pvm.permission.name in viewer_perms)

def is_user_pvm(pvm):
    return (pvm.view_menu.name in vms and
            pvm.permission.name in viewer_perms + action_perms)

def is_op_pvm(pvm):
    return (pvm.view_menu.name in vms + security_vms and
            pvm.permission.name in viewer_perms + action_perms)

def init_role(role_name, pvm_check):
    session = sm.get_session()
    pvms = session.query(sqla_models.PermissionView).all()
    pvms = [p for p in pvms if p.permission and p.view_menu]
    role = sm.add_role(role_name)
    role_pvms = [p for p in pvms if pvm_check(p)]
    role.permissions = role_pvms
    session.merge(role)
    session.commit()

def init_roles():
    init_role('Viewer', is_viewer_pvm)
    init_role('User', is_user_pvm)
    init_role('Op', is_op_pvm)

init_roles()
