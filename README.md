# GoldenGate monitoring and sending notifications


The script (MonitorGoldenGate.py) check for all extracts and replicats if they are running if not send an email. If it is running, it checks the lag. Depending the value (in seconds) send an email. In the script I defined 10 seconds of lag to send an email.

GoldenGate APIs used in the script:

* List Extracts: /services/{version}/extracts
* Retrieve Extract Status: /services/{version}/extracts/{extract}/info/status
* Retrieve Extract Report: /services/{version}/extracts/{extract}/info/reports/{report}
* List Replicats: /services/{version}/replicats
* Retrieve Replicat Status: /services/{version}/replicats/{replicat}/info/status
* Retrieve Replicat Report: /services/{version}/replicats/{replicat}/info/reports/{report}

More info on: 

Check all GoldenGate REST APIs on [documentation](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oggra/rest-endpoints.html).
