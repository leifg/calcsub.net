# CalcSub.net

## Description

This is the source code of the subnet calculator deployed at [http://calcsub.net](http://calcsub.net).

## Features

- calculation of ranges for IPv4 and IPv6 address
- automatic recognition of IP version
- colored representation to show net, mixed and host part of address
- auto refresh on text input (JavaScript required)
- backward compatibility for JavaScript disabled browser (Progressive Enhancement)
- RESTful web-service (all calculations done via GET request)
- HTML and JSON representation of calculation result

## Usage

You can either use the input field to calculate the values for an IP address or you can call the URL directly. 
The URL pattern always looks like this: http://<domain>/<ip-address>/<prefix> to get the result. The prefix is optional in the URL. If it is not specified the IP address will be interpreted as a single IP address (maximum prefix will be assumed).
	
## API

If you don't want an HTML representation, you can just append "/json" to any URL to get the according JSON object (e.g. http://<domain>/fe80::/10/json). The JSON will then look like this:

	{
		"address":"fe80:0000:0000:0000:0000:0000:0000:0000",
		"prefix":"10",
		"start_address":"fe80:0000:0000:0000:0000:0000:0000:0000",
		"end_address":"febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
		"splitted_address":
		{
			"net":"fe",
			"mixed":"8",
			"host":"0:0000:0000:0000:0000:0000:0000:0000"
		}
	}

## Requirements

In order to run the application you'll need:

- sinatra
- sinatra-reloader
- ipaddress
- haml
- sass

For development you'll need:

- rspec
- watchr
- rack-test

Or just use [bundler](http://gembundler.com/).
