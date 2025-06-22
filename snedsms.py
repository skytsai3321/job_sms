import requests

def sned_sms(job_name, phones):
    url = 'https://examole.com'
    data = {
        'phone': phones,
        'job_name': job_name,
    }

    requests.post(url, data)

if __name__ == "__main__":
    sned_sms('HHHHH', '0926255351')