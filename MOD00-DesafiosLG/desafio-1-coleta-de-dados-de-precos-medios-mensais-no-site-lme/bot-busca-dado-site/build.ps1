$exclude = @("venv", "bot-busca-dado-site.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-busca-dado-site.zip" -Force