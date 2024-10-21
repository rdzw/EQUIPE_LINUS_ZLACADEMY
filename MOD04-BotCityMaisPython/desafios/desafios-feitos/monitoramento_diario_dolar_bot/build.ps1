$exclude = @("venv", "monitoramento_diario_dolar_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "monitoramento_diario_dolar_bot.zip" -Force