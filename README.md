# MasscanResultsParser

Reads masscan json results file and outputs the port/protocol and status per host.

# Usage example

python parser.py masscan_json_results_file_path

# Output example

Results:
	192.168.0.1
		port: 53/tcp is open
		port: 80/tcp is open
	192.168.0.12
		port: 8080/tcp is open
		port: 9989/tcp is open
	192.168.0.123
		port: 3389/tcp is open
