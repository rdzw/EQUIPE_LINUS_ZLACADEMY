$exclude = @("venv", "bot_PDF_Extractor_e_Envio.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_PDF_Extractor_e_Envio.zip" -Force