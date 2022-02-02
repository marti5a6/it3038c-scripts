function getIP {
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}

$IP = getIP
$Date = (Get-Date -Format "dddd, MMMM d, yyyy")
$Name = $env:USERNAME
$Comp = $env:COMPUTERNAME
$Version = (Get-Host).Version

$From = "tonym123099@gmail.com"
$To = "marti5a6@mail.uc.edu"
$Cc = "botheaj@mail.uc.edu"
$Subject = "IT308C Windows SysInfo"
$SmtpServer = "smtp.gmail.com"
$SmtpPort = "587"

$Body = "This machine's IP address is $IP, the user is $Name, the hostname is $Comp, the BASH version is $Version, and today's date is $Date."

Write-Host $Body

Send-MailMessage -From $From -To $To -Cc $Cc -Subject $Subject -Body $Body -SmtpServer $SmtpServer -Port $SmtpPort -UseSsl -Credential (Get-Credential)