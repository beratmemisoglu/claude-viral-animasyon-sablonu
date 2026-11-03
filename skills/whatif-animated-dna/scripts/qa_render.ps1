# qa_render.ps1 — render sonrası QA: kare çekme (shot başlangıçları) + kesme ritmi QA (lowbudgetstories rhythm_qa.py)
# usage:  powershell -File qa_render.ps1 -Project C:\dev\whatif-projects\<slug> [-Studio C:\dev\the-other-self] [-Final] [-Montage]
#   -Final yoksa render/<slug>-draft.mp4 kullanılır. Çıktı: <proje>/qa/frames/*.jpg (ffmpeg, shot start+0.2 s) + <proje>/qa/rhythm/report.json
param(
  [Parameter(Mandatory = $true)][string]$Project,
  [string]$Studio = 'C:\dev\the-other-self',
  [switch]$Final,
  [switch]$Montage,
  [double]$TargetLufs = -14
)
$ErrorActionPreference = 'Stop'
$slug = Split-Path $Project -Leaf
$video = if ($Final) { "$Project\render\$slug.mp4" } else { "$Project\render\$slug-draft.mp4" }
if (-not (Test-Path $video)) { throw "video yok: $video (önce pipeline.py $slug --only render)" }
$shots = (Get-Content "$Project\shots.json" -Raw -Encoding UTF8 | ConvertFrom-Json).shots
$timeline = Get-Content "$Project\timeline.json" -Raw -Encoding UTF8 | ConvertFrom-Json

# 1) ffprobe özeti
Write-Output '== ffprobe'
ffprobe -v error -show_entries format=duration:stream=codec_type,width,height,r_frame_rate -of default=nw=1 $video

# 2) Kareler: her shot'ın başlangıcı + 0.2 s (en fazla 40 kare, eşit aralıkla seyrelt)
$frames = "$Project\qa\frames"
New-Item -ItemType Directory -Force $frames | Out-Null
Remove-Item "$frames\*.jpg" -ErrorAction SilentlyContinue
$step = [math]::Max(1, [math]::Ceiling($shots.Count / 40))
$i = 0
foreach ($s in $shots) {
  if (($i % $step) -eq 0) {
    $t = [double]$s.t_start + 0.2
    $name = '{0}\{1:000}-{2}-{3:0.0}s.jpg' -f $frames, $i, $s.id, $t
    ffmpeg -hide_banner -loglevel error -y -ss $t -i $video -frames:v 1 -q:v 3 $name
  }
  $i++
}
Write-Output "== $((Get-ChildItem $frames -Filter *.jpg).Count) kare -> $frames  (Claude her kareye bakmalı: etiket/yüz çakışması, güvenli alan, boş kare, Türkçe karakter bozulması)"

# 3) Kontak sayfası (Pillow): 4 sütun
$contact = @"
from PIL import Image; import glob, sys
fs = sorted(glob.glob(r'$frames\*.jpg'))
if fs:
    cols = 4; w, h = 480, 270
    rows = (len(fs) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * w, rows * h), (20, 20, 20))
    for i, f in enumerate(fs): sheet.paste(Image.open(f).resize((w, h)), ((i % cols) * w, (i // cols) * h))
    sheet.save(r'$Project\qa\contact.jpg', quality=85); print('contact ->', r'$Project\qa\contact.jpg')
"@
$contact | python -

# 4) Transkript (timeline.json → rhythm_qa'nın beklediği [start,end] listesi) + ritim/ses QA
$rq = "$env:USERPROFILE\.claude\skills\lowbudgetstories-dna\scripts\rhythm_qa.py"
$iv = @()
foreach ($seg in $timeline.segments) { $iv += ,@([double]$seg.start, [double]$seg.start + [double]$seg.dur) }
$iv | ConvertTo-Json -Compress -Depth 3 | Out-File -Encoding ascii "$Project\qa\speech_intervals.json"
Write-Output '== rhythm_qa (norm: LBS 10 video; voiced mod — konuşmalı anlatım)'
$args = @($video, '--transcript', "$Project\qa\speech_intervals.json", '--mode', 'voiced', '--out', "$Project\qa\rhythm", '--target-lufs', "$TargetLufs")
if ($Montage) { $args += '--montage' }
python $rq @args
Write-Output "rhythm exit: $LASTEXITCODE  (0 = FAIL yok; WARN'lar raporda)"
Write-Output "Rapor: $Project\qa\rhythm\report.json"
