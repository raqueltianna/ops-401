# Script Name:                          lab01-powershell.bat
# Author name:                          Tianna Farrow
# Date of latest revision:              01/11/2024
# Purpose:                              Powershell script that automates CIS benchmarks for windows server.
# Execution:                            Write a PowerShell script that automates the configuration of the required settings: 1.1.5; 18.4.3 
# Additional resources:                 https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit; https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content?view=powershell-7.4;https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-content?view=powershell-7.4;https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit-configure; https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.4

# Specify paths and registry key
$SecurityOptionsPath = 'C:\Temp\SecurityOptions.inf'
$SMBv1RegistryPath = 'HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10'

# Configure Password Policy
$PasswordPolicy = @{
    'MinimumPasswordLength' = 6
    'MinimumPasswordCharacters' = 3
    'PasswordComplexity' = $true
    'PasswordHistoryCount' = 0
    'MaximumPasswordAge' = (New-TimeSpan -Days 90)
}

# Export Security Settings
secedit /export /cfg $SecurityOptionsPath /areas SECURITYPOLICY

# Modify SecurityOptions.inf
(Get-Content $SecurityOptionsPath) | ForEach-Object {
    $_ -replace 'MinimumPasswordLength = \d+', "MinimumPasswordLength = $($PasswordPolicy['MinimumPasswordLength'])" `
       -replace 'MinimumPasswordCharacters = \d+', "MinimumPasswordCharacters = $($PasswordPolicy['MinimumPasswordCharacters'])" `
       -replace 'PasswordComplexity = \d+', "PasswordComplexity = $($PasswordPolicy['PasswordComplexity'])" `
       -replace 'PasswordHistoryCount = \d+', "PasswordHistoryCount = $($PasswordPolicy['PasswordHistoryCount'])" `
       -replace 'MaximumPasswordAge = \d+', "MaximumPasswordAge = $($PasswordPolicy['MaximumPasswordAge'].Days)" `
} | Set-Content $SecurityOptionsPath

# Import and Apply Security Settings
secedit /configure /db C:\Windows\security\local.sdb /cfg $SecurityOptionsPath /areas SECURITYPOLICY

# Configure SMBv1 Client Driver Service
$SMBv1Setting = @{
    'Name' = 'Start'
    'Value' = 4 # 4 corresponds to 'Disabled'
}

# Set SMBv1 Client Driver Service setting
if (Test-Path $SMBv1RegistryPath) {
    Set-ItemProperty -Path $SMBv1RegistryPath -Name $SMBv1Setting['Name'] -Value $SMBv1Setting['Value']
} else {
    Write-Host "Registry path not found: $SMBv1RegistryPath"
}