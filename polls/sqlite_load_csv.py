
import os
import sys
#sys.path.append('/Users/md761b/Documents/tutorial/github_job/mysite/')
import requests
import json
import pandas as pd
from polls.models import Job

def get_csv_file():
    repos = requests.get(
        "https://api.github.com/repos/awesome-jobs/vietnam/issues?per_page=200"
    )
    repos.json()
    issues = json.loads(repos.content)
    jobs = []   
    links = []
    for issue in issues:
        jobs.append(issue["title"])
        links.append(issue["html_url"])
    github_jobs = pd.DataFrame(zip(jobs, links), columns=["github_job", "link_website"])
    return github_jobs.to_csv("/Users/md761b/documents/vinh/CV_Vinh/test/github_job.csv")


def load_csv_file():
    column_name = ['github_job', 'link_website']
    csv_data = pd.read_csv(r"/Users/md761b/documents/vinh/CV_Vinh/test/github_job.csv", names=column_name, header=1)
    for i, row in csv_data.iterrows():
        file_sqlite = Job(github_job=row['github_job'] , link=row['link_website'])
        file_sqlite.save() 


if __name__ == '__main__':
    print(load_csv_file())