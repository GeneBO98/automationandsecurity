#/usr/bin/env python3

import sys
import requests
import json
from requests.auth import HTTPBasicAuth

# Define the description of the alert you want to exclude
# exclude_alert_description = "Host-based anomaly detection event (rootcheck)"
# Define the name of the agent you want to exclude

# read configuration
alert_file = sys.argv[1]
user = sys.argv[2].split(":")[0]
hook_url = sys.argv[3]

# read alert file
with open(alert_file) as f:
    alert_json = json.loads(f.read())

# Extract alert fields
alert_level = alert_json["rule"]["level"]

# The rest of your code for sending alerts

# colors from https://gist.github.com/thomasbnt/b6f455e2c7d743b796917fa3c205f812
# Determine the color based on the alert level
if alert_level == 7:
    # DarkGreen
    color = "2067276"
elif alert_level == 8:
    # Green
    color = "5763719"
elif alert_level == 9:
    # Yellow
    color = "16705372"
elif alert_level == 10:
    # Gold
    color = "15844367"
elif alert_level == 11:
    # DarkGold
    color = "12745742"
elif alert_level == 12:
    # Orange
    color = "15105570"
elif alert_level == 13:
    # Dark Orange
    color = "11027200"
elif alert_level == 14:
    # Red
    color = "15548997"
else:
    # Dark red
    color = "10038562"

# Agent details
if "agentless" in alert_json:
    agent_ = "agentless"
else:
    agent_ = alert_json["agent"]["name"]

# Combine message details
payload = json.dumps({
    "content": "",
    "embeds": [
        {
            "title": f"Wazuh Alert - Rule {alert_json['rule']['id']}",
            "color": color,
            "description": alert_json["rule"]["description"],
            "fields": [
                {
                    "name": "Agent",
                    "value": agent_,
                    "inline": True
                },
                {
                    "name": "Product",
                    "value": alert_json.get("data", {}).get("win", {}).get("eventdata", {}).get("product", "N/A"),
                    "inline": True
                },
                {
                    "name": "Command Line",
                    "value": alert_json.get("data", {}).get("win", {}).get("eventdata", {}).get("commandLine", "N/A"),
                    "inline": True
                },
                {
                    "name": "Full Message",
                    "value": alert_json.get("data", {}).get("win", {}).get("system", {}).get("message", "N/A"),
                    "inline": True
                },
                {
                    "name": "Rule Level",
                    "value": alert_json.get("rule", {}).get("level", "N/A"),
                    "inline": True
                }

            ]
        }
    ]
})


# Send message to Discord
r = requests.post(hook_url, data=payload, headers={"content-type": "application/json"})
sys.exit(0)
