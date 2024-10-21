$exclude = @("venv", "clima_api_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "clima_api_bot.zip" -Force