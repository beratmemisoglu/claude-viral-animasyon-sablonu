# qa.ps1 — type-check, list compositions, render key-frame stills for visual inspection (PowerShell 5.1 safe)
# usage (from the studio root):  powershell -File scripts\qa.ps1 -Film loneliness -Frames "15,90,240,420,600,1500,1800,3300,4110,4400"
param(
  [Parameter(Mandatory = $true)][string]$Film,
  [string]$Frames = '15,90,240,420,600,1200,1500,1800,2160,2700,3300,3750,4110,4400',
  [double]$Scale = 0.5
)
$ErrorActionPreference = 'Stop'

Write-Output '== tsc'
npx.cmd tsc --noEmit
if ($LASTEXITCODE -ne 0) { throw 'tsc failed' }

Write-Output '== compositions'
npx.cmd remotion compositions src/index.ts
if ($LASTEXITCODE -ne 0) { throw 'compositions failed (validateScript?)' }

$out = "out/qa/$Film"
New-Item -ItemType Directory -Force $out | Out-Null
Write-Output "== stills -> $out"
npx.cmd remotion render src/index.ts "$Film-film" $out "--frames=$Frames" "--scale=$Scale" --image-format=jpeg
if ($LASTEXITCODE -ne 0) { throw 'still render failed' }

Write-Output "Done. Open every image in $out and check it against references/03-visual-canon.md before the draft render."
