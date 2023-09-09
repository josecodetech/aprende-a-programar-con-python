import fitz
import os
def añadir_imagen(pdf_original, pdf_final, imagen_png, x, y, ancho, alto):
    pdf_documento = fitz.open(pdf_original)
    imagen = fitz.open(imagen_png)
    pagina = pdf_documento[0]
    img_rect = fitz.Rect(x,y,x+ancho,y+alto)
    pagina.insert_image(img_rect,pixmap=imagen[0].get_pixmap(alpha=True))
    pdf_documento.save(pdf_final)
    pdf_documento.close()
    imagen.close()
if __name__ == '__main__':
    pdf_original = "pruebas.pdf"
    pdf_final = "documento_firmado.pdf"
    imagen_png = "firma.png"
    x = 85
    y = 600
    ancho = 80
    alto = 80
    añadir_imagen(pdf_original,pdf_final,imagen_png,x,y,ancho,alto)
    os.rename(pdf_final,"pdf_renombrado.pdf")