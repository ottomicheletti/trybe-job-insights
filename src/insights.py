import csv


# Req 02 - Learning DictReader(), not in, and, len() and append
def get_unique_job_types(path: str):
    result = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["job_type"]
            if job not in result and len(job) != 0:
                result.append(job)
    return result


# Req 03
def get_unique_industries(path: str):
    result = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            industry = row["industry"]
            if industry not in result and len(industry) != 0:
                result.append(industry)
    return result


# Req 04 - Learning int(), isdigit() and max()
def get_max_salary(path: str):
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        salaries = [
            int(row["max_salary"])
            for row in reader
            if row["max_salary"].isdigit()
        ]
    return max(salaries)


# Req 05 - Learning min()
def get_min_salary(path: str):
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        salaries = [
            int(row["min_salary"])
            for row in reader
            if row["min_salary"].isdigit()
        ]
    return min(salaries)


# Req 06 - Learning filter(), lambda and list()
def filter_by_job_type(jobs: list, job_type: str):
    filtered_jobs = filter(lambda job: job["job_type"] == job_type, jobs)
    return list(filtered_jobs)


# Req 07
def filter_by_industry(jobs: list, industry: str):
    filtered_jobs = filter(lambda job: job["industry"] == industry, jobs)
    return list(filtered_jobs)


# Req 08 - Learning keys(), raise, isinstance(), .format()
def matches_salary_range(job: dict, salary: int):

    if ("min_salary" or "max_salary") not in job.keys():
        raise ValueError

    if (
        not isinstance(salary, int)
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
    ):
        raise ValueError

    print(
        "Min: {min}, Max: {max}, Salário: {salario}".format(
            max=job["max_salary"], min=job["min_salary"], salario=salary
        )
    )

    if job["min_salary"] > job["max_salary"]:
        raise ValueError

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


# Req 09 - Learning try, except and finally
def filter_by_salary_range(jobs: list, salary: int):
    filtered_jobs = []
    try:
        for job in jobs:
            if not (
                job["min_salary"] > job["max_salary"]
            ) and matches_salary_range(job, salary):
                filtered_jobs.append(job)
    except ValueError:
        pass
    finally:
        return filtered_jobs
