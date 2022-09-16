function getIP {
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = (getIP)

$USER = ($env:USERNAME)

$HOSTNAME = (hostname)

$PSVersion = ($PSVersionTable.PSVersion)

$DATE = (Get-Date -Format "dddd, MMMM d, yyyy")

$BODY=("This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version $PSVersion. Today's date is $DATE.")

Write-Output($BODY) | Out-File -FilePath C:\it3038c-scripts\powershell\Lab3.txt

notepad.exe C:\it3038c-scripts\powershell\Lab3.txt