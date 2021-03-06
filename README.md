# Pre-preprocessing with python scripts
Eklemek istediğim çok özellik var (çoklu dosya, string check, biraz da hata ayıklama). Tamamlar mıyım bilmiyorum.

## Kurulum
`pip install ppps`

## Örnek bir script:

```python
import time
st = time.time()

import ppps

rv = ppps.process_file(
    input_path="src/main.c",
    output_path="build/ppps/out.c"
)

if rv: print(f"Finished in [{time.time()-st}s]")
else: print("Pre-pre process failed")
```


Bu scripti proje klasörüne yükleyin

## Parametreler

### input_path
İşlenecek dosyanın yolu

### output_path
Çıktı dosyasının yolu

### exec_tokens

Derleyici script tarafından `exec()` fonksiyonu içine alınacak stringleri belirlemek için kullanılan tokenlar

```python
import ppps
ppps.process_file("main.c", exec_tokens={
    "start_token" : "/**",
    "end_token"   : "**/"
})
```

(karışıklık çıkmaması açısından tokenların basit olmaması iyi olur)

### eval_tokens

Derleyici script tarafından `eval()` fonksiyonu içine alınacak stringleri belirlemek için kullanılan tokenlar.

```python
import ppps
ppps.process_file("main.c", exec_tokens={
    "start_token" : "/*(",
    "end_token"   : ")*/"
})
```

### replace_exec
`exec()` içine alınacak stringlerin output dosyasından temizlenip temizlenmeyeceğini belirler

```python
import ppps
ppps.process_file("main.c", replace_exec=True)
```
True temizler, False bırakır

### replace_eval
`eval()` içine alınacak stringlerin output dosyasından temizlenip temizlenmeyeceğini belirler

```python
import ppps
ppps.process_file("main.c", replace_eval=True)
```
True temizler, False bırakır
