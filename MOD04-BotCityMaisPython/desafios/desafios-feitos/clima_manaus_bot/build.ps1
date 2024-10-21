$exclude = @("venv", "clima_manaus_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "clima_manaus_bot.zip" -Force