*** Settings ***
Documetion.....cheak to be run releases.
......if you getting failures and doing branch testing,consider excluding the 'full-build' tag. we have no way
.....of working if your dev-branch is building all connectors so the only way to avoid false negatives is
....skip those tests.

Resource........${curdir}/${resourse}
Force Tags......Production....Smoke.....1-day...1-week....two-suites
Library..........ApplianceLib.....&{initialize}
*** Variables ***
${resourse}=appliance.txt
*** Test Cases ***
Check availble connectors
    [Tages]     full-build
    @{availble connectors}=     ensure all connectors are availble
    log     Availble connectors are ${availble connectors}      console=True

Check rpms
    [documentation]......Ensure there are no regression missing based rpms.
    ...act-68922 :rpm version check fresh install
    ...act-68956 : rpm version check patch upgrade
    Chech important rpms

Check component versions