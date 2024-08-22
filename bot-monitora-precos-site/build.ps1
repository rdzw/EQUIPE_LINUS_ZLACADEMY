$exclude = @("venv", "bot-monitora-precos-site.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-monitora-precos-site.zip" -Force