#!/bin/bash

### bracelet.py CLI
### Yes I wrote all of this in bash :sob:
### Created: November 26th, 2026 (Wow 11/26/26)
### Author: LeAndre C.

function help-cmd() {
	echo """
	bracelet.py CLI

	-h, --help - Returns this help prompt.
	-e, --endpoint - Returns the current saved endpoint.
	-v, --version - Returns the version of bracelet.py you're on
	"""
}

function version-cmd() {
python3 -c """
try:
    import bracelet
    print('Bracelet Version:', bracelet.__version__)
except Exception as e:
    print('Failed to get version:', e)
    pass
""" | cat
}

function endpoint-cmd() {
python3 -c """
try:
    import bracelet
    print('Bracelet Endpoint:', bracelet.__endpoint__)
except Exception as e:
    print('Failed to get endpoint:', e)
    pass
""" | cat
}

function main() {
	local arg1=$1
	if [[ $arg1 == "-v" || $arg1 == "--version" ]]; then {
		version-cmd
	} elif [[ $arg1 == "-h" || $arg1 == "--help" ]]; then {
		help-cmd
	} elif [[ $arg1 == "-e" || $arg1 == "--endpoint" ]]; then {
		endpoint-cmd
	} else {
		help-cmd
	}
	fi
}

main "$@"
