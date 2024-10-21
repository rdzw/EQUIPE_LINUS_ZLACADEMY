$exclude = @("venv", "botproduto.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botproduto.zip" -Force