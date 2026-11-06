import os,json,base64,urllib.request,sys
OUT=sys.argv[1]; key=os.environ['ELEVENLABS_API_KEY']
text=("Şimdi sana bir şey anlatacağım ama inanmayacaksın! Yıl 1453. Bizanslılar limanın ağzına dev bir zincir germiş ve hiçbir gemi geçemiyor. "
"Osmanlı donanması geliyor, zincire çarpıyor ve öylece... duruyor. Surlardaki muhafızlar gülmekten el sallıyor! "
"Ama bir gece genç sultan tepeye kütüklerden bir yol döşetiyor, kütükleri yağlatıyor ve gemileri yokuş yukarı çektiriyor. "
"Sabah olduğunda yetmiş gemi tepenin öbür yanından kayarak limana iniyor. Zincirin arkasına. Muhafızlar artık gülmüyordu.")
prompts={
 'A':"Anadili Türkçe olan, İstanbul Türkçesiyle konuşan genç bir erkek, on dokuz yaşında, stüdyo kalitesinde kayıt. Esprili genç bir YouTube içerik üreticisi. Enerjik, oyuncu ve heyecanlı. Sesi açık, parlak, ince ve yüksek perdeli; hızlı ve akıcı bir tempoyla, gülümseyerek, arkadaşına inanılmaz bir hikâye anlatır gibi konuşuyor, sürpriz cümlelerde kısa bir duraklamayla yavaşlıyor.",
 'B':"Anadili Türkçe olan, İstanbul Türkçesiyle konuşan genç bir erkek, yirmi yaşlarında, stüdyo kalitesinde kayıt. Neşeli genç bir hikâyeci. Hevesli, esprili ve meraklı. Sesi hafif, parlak, belirgin şekilde ince ve yüksek perdeli, gençlik enerjisiyle dolu; hızlı, canlı ve doğal bir tempoyla, cümle sonlarında hafif alaycı bir gülümsemeyle konuşuyor.",
 'C':"Anadili Türkçe olan, İstanbul Türkçesiyle konuşan genç bir erkek, yirmili yaşlarının başında, stüdyo kalitesinde kayıt. Esprili bir sosyal medya hikâye anlatıcısı. Eğlenceli, alaycı ve enerjik. Sesi açık, parlak ve yüksek perdeli, hafif genizden; hızlı ve rahat bir tempoyla, şakaları ciddi bir yüzle söyler gibi, önemli anlarda vurguyu artırıp duraklamalarla merak uyandırarak konuşuyor.",
}
res={}
for name,p in prompts.items():
    body=json.dumps(dict(voice_description=p,model_id='eleven_ttv_v3',text=text,guidance_scale=float(sys.argv[2]),loudness=0.5)).encode()
    req=urllib.request.Request('https://api.elevenlabs.io/v1/text-to-voice/design?output_format=mp3_44100_128',data=body,headers={'xi-api-key':key,'Content-Type':'application/json'})
    try: r=json.load(urllib.request.urlopen(req,timeout=300))
    except urllib.error.HTTPError as e: print(name,'ERR',e.code,e.read()[:400]); continue
    for i,pv in enumerate(r['previews']):
        fn=f'{OUT}/{name}{i+1}.mp3'; open(fn,'wb').write(base64.b64decode(pv['audio_base_64']))
        res[f'{name}{i+1}']=dict(id=pv['generated_voice_id'],dur=pv['duration_secs'])
        print(name,i+1,pv['duration_secs'],pv.get('language'))
json.dump(res,open(f'{OUT}/ids.json','w'),indent=1)
