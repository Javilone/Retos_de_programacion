# Crea un programa que se encargue de calcular el aspect ratio de una
# imagen a partir de una url.
# - Url de ejemplo:
#   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
# - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#   imagen de 1920*1080px.


from PIL import Image
import requests

url="https://cdn.wonderstatic.com/product-image/dekoracja-stojaca-gorilla-60x76-cm-ciemnoszara-1?width=350&height=312&quality=85&dpr=2&format=pjpg&auto=webp&fit=bounds&io=true"
im = Image.open(requests.get(url, stream=True).raw)

caja = im.getbbox()
aspect_ratio = caja[3]/caja[2]

print(f"La imagen mide: {caja[2]}x{caja[3]}px")
print(f"El ratio de la imagen es: {round(aspect_ratio,1)}:1")