$exclude = @("venv", "BOT-SDOA.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BOT-SDOA.zip" -Force