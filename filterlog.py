import re


def filter_log(file_path):
    jobs = []
    with open(file_path, "r", encoding="utf-8") as log:
        for line in log.readlines():
            # print(line)
            job = re.search(r"JOB: \w+", line)
            if job is not None:
                jobs.append(job)
    return jobs


if __name__ == "__main__":
    jobs = filter_log("log/system.log")
    print(jobs)
