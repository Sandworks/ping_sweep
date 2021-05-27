# ping_sweep

**ping_sweep.py - ping test multiple devices listed in a JSON file**

_James Sanders ' <ciscoguru72' *at* 'yahoo' *dot* 'com' *dot 'au'_

A python script to ping test multiple devices that are listed in a JSON file. JSON file must have the following key:value pair - "name" for hostname and "ip" for ip address. The script read each of these and a perform ping test. The result displays success or failure. Other JSON key:value pair are ignored. Please see my "csv_json_convert" script to create a JSON file from CSV Spreadsheet.

I'm a network engineer who enjoys writing Python scripts to make life easy for myself and others. As a Python newbie, I'm always learning to improve my code. Therefore, I'm keen to hear your thoughts on my code and how I should improve. Also, I'm eager to hear new ideas and meet likewise people who write network-related Python scripts.

## Why?

I want to check a bunch of switches to see if they're alive or not. This is handy when running a script to change many switches, and I would like to know if they're up beforehand.

## Userguide

**./ping_sweep.py _[JSON file]_**

or 

**python3 ping_sweep.py _[JSON file]_**

The script will read a JSON file and using its data to ping test multiple devices. For example:

**JSON file format**

JSON file must include these two key:value pair to make this script work, and they are "name" and "ip". Other key:value pairs are ignored. Here's an example JSON file:

![JSON Format](https://github.com/Sandworks/ping_sweep/blob/6ff88c1128944e18e70baf692f9f56e7006aa6c2/json_format.png)

Using this json file, we can run the script as shown:

./ping_sweep.py device_list.json

Here an example output from this script:

![Output](https://github.com/Sandworks/ping_sweep/blob/6ff88c1128944e18e70baf692f9f56e7006aa6c2/output.png)

## Additional Notes:

You can change the names in key:value pair by changing these variables to your preferred variable.

![Change Variables](https://github.com/Sandworks/ping_sweep/blob/6ff88c1128944e18e70baf692f9f56e7006aa6c2/change.png)

Enjoy!

James.
