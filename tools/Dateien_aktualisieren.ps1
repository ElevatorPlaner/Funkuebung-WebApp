# Holt die aktuellen Dateien aus dem Repo in den Drive-Ordner der Funkuebung.
# Aufruf: Doppelklick auf Dateien_aktualisieren.bat (liegt daneben).
$ErrorActionPreference = 'Stop'
$ziel  = Join-Path $env:USERPROFILE 'Insync\goerlich88@gmail.com\Google Drive\7 FEUERWEHR\4 ELW-Team\WebApp Funkübung'
$basis = 'https://raw.githubusercontent.com/ElevatorPlaner/Funkuebung-WebApp/claude/new-session-o2eqi2/'
$dateien = @(
  @('funkuebung.html',     'Funkuebung_ELW_V2.html'),
  @('standalone.html',     'Funkuebung_ELW_Standalone\Funkuebung_ELW_Standalone.html'),
  @('uebungsleiter.html',  'Funkuebung_Uebungsleiter_Tablet.html')
)
if (-not (Test-Path -LiteralPath $ziel)) { Write-Host "Ordner nicht gefunden: $ziel"; Read-Host 'Mit Enter beenden'; exit 1 }
foreach ($d in $dateien) {
  $url = $basis + $d[0]; $pfad = Join-Path $ziel $d[1]
  $ordner = Split-Path $pfad -Parent; if (-not (Test-Path -LiteralPath $ordner)) { New-Item -ItemType Directory -Path $ordner | Out-Null }
  $tmp = [System.IO.Path]::GetTempFileName()
  Invoke-WebRequest -Uri $url -OutFile $tmp -UseBasicParsing
  if ((Get-Item $tmp).Length -lt 10000) { Write-Host "Download zu klein, nichts ersetzt: $($d[0])"; Remove-Item $tmp; continue }
  Move-Item -LiteralPath $tmp -Destination $pfad -Force
  Write-Host ("Aktualisiert: " + $d[1] + " (" + [math]::Round((Get-Item -LiteralPath $pfad).Length / 1024) + " KB)")
}
Write-Host ''
Write-Host 'Fertig. Insync laedt die Dateien jetzt in das Google Drive hoch.'
Read-Host 'Mit Enter beenden'
