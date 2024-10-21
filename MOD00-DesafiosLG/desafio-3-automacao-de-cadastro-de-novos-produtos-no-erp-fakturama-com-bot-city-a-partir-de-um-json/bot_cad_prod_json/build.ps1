$exclude = @("venv", "bot_cad_prod_json.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_cad_prod_json.zip" -Force