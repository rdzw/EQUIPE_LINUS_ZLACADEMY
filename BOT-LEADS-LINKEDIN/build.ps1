$exclude = @("venv", "BOT-LEADS-LINKEDIN.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BOT-LEADS-LINKEDIN.zip" -Force