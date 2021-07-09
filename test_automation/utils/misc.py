import os
import ansible_runner

from test_automation.data import test_config

cluster_identifier = 0


def run_playbook(playbook, extravars=None, data_dir='setup'):
    ansible_runner.run(private_data_dir=data_dir, playbook=playbook, extravars=extravars)


def get_test_vars(test_name):
    if test_name not in test_config.tests:
        raise NameError("Test name {} not found in data/test_vars.".format(test_name))
    return test_config.tests[test_name]


def get_db_props(db_type):
    if db_type == "epas":
        return {
            "database_name": "edb",
            "database_user": "enterprisedb",
            "db_port": 5433
        }
    return {
        "database_name": "postgres",
        "database_user": "postgres",
        "db_port": 5433
    }


def get_node_names(standby_count):
    global cluster_identifier
    xdist_var = 'PYTEST_XDIST_WORKER'
    gw_number = ""
    if xdist_var in os.environ:
        gw_number = "_p{}".format(os.environ.get(xdist_var)[-1])
    cluster_identifier += 1
    primary_name = "primary_{}{}".format(cluster_identifier, gw_number)
    standby_names = ["replica{}_{}{}".format(cluster_identifier, i, gw_number) for i in range(1, standby_count + 1)]
    return primary_name, standby_names
