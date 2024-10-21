$exclude = @("venv", "kindle_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "kindle_bot.zip" -Force