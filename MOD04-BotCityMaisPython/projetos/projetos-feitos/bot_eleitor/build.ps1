$exclude = @("venv", "bot_eleitor.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_eleitor.zip" -Force