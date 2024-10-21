$exclude = @("venv", "monitora_dolar_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "monitora_dolar_bot.zip" -Force