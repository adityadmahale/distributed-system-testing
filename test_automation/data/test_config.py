# The "tests" dictionary holds the custom properties required for the test cluster.
# Each key in the "tests" dictionary should have the same name as the target test function.
tests = {
    "test_1": {
        "primary_db_props": {
            "max_replication_slots": "10"
        }
    },
    "test_2": {
        "standby_count": 2
    },
    "test_3": {
        "standby_count": 1
    },
    "test_4": {
        "standby_count": 2,
        "primary_db_props": {
            "max_replication_slots": "8",
        }
    }
}
