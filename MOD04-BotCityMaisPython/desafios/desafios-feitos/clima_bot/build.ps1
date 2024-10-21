$exclude = @("venv", "clima_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "clima_bot.zip" -Force