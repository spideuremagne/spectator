import json
from flask import Flask, render_template
import yaml


# import locals
import getstatus

app = Flask(__name__)


@app.route('/')
def render_status():


    with open("hosts.yaml", 'r') as hostStream:
        hosts_loaded = yaml.safe_load(hostStream)

        allstat = []
        for target in hosts_loaded['hosts']:
            status = getstatus.pollHostStatus(target)
            allstat.append(status)

        return render_template('status.html', result=allstat)


@app.route('/json')
def render_json():


    status = getstatus.pollHostStatus()
    status = json.dumps(status)

    return status



if __name__ == '__main__':
    app.run()
