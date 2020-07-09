from sagemaker import Session, get_execution_role

sm_session = Session()

bucket = sm_session.default_bucket()
prefix = 'dc19-rx-sm'
role = get_execution_role()
