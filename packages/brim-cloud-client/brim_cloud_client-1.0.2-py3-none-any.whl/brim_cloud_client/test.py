from BRIM import TMB


tmb_client = TMB(cm=0.9, cb=0.6, p='tmb', Rc=31000,
                 C=49e-15, anneal=0.00011, seed=0, repititions=2)

job_id = tmb_client.enqueue(
    '../../example/cust-u500-01.cnf', email="lianlongsun@gmail.com")
print(job_id)

# tmb_client.fetch("53f7aa18-dd6c-4f93-8f41-c0d17e7ede0f")
