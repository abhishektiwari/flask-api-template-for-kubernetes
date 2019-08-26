"""
Validating user input before generation
"""
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
DNS_REGEX = r'^[-a-zA-Z][-a-zA-Z0-9]+$'
API_PRE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
TABLE_PRE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


module_name = '{{ cookiecutter.module_name}}'
dns_name = '{{ cookiecutter.dns_name}}'
api_prefix = '{{ cookiecutter.api_prefix}}'
table_prefix = '{{ cookiecutter.table_prefix}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is invalid Module name. Allowed a-z,A-Z, 0-9, _. No space' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

if not re.match(DNS_REGEX, dns_name):
    print('ERROR: %s is invalid DNS name. Allowed a-z,A-Z, 0-9, -. No space' % dns_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

if not re.match(API_PRE_REGEX, api_prefix):
    print('ERROR: %s is invalid API Prefix. Allowed a-z,A-Z, 0-9, _. No space.' % api_prefix)

    # exits with status 1 to indicate failure
    sys.exit(1)

if not re.match(TABLE_PRE_REGEX, table_prefix):
    print('ERROR: %s is invalid API Prefix. Allowed a-z,A-Z, _. No space.' % table_prefix)

    # exits with status 1 to indicate failure
    sys.exit(1)
