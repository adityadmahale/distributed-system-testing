### Prerequisites:

    1. Install Docker
    1. Install Python 3.x
    2. pip install -r requirements.txt

### Running tests:
    
    The tests can be invoked using the Pytest command
    
    1. To run all tests:
        pytest .
        
    2. To run tests in parallel:
        pytest . -n 2
        where n = Number of processes
    
    3. To run a test with marker:
        pytest . -m marker_name
        
    4. Custom options:
        --os_type: Type of OS platform(centos)
        --os_version: Version of OS
        --db_type: Type of database(epas/pg)
        --db_version: Database version