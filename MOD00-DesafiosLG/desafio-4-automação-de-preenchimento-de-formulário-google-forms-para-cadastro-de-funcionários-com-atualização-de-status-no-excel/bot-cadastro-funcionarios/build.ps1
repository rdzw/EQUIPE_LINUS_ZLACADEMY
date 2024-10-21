$exclude = @("venv", "Bot-PedidosdeEmprestimo(POC).zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Bot-PedidosdeEmprestimo(POC).zip" -Force