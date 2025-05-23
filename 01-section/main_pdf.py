from metadato.pdf_tool import PDFHandler

def main():
    test_pdf = "Documentos.pdf"
    test_images = ["IMG_20250523_093201.jpg", "space.jpg"]
    
    # Unir PDFs
    print(PDFHandler.merge_pdfs(["Documentos.pdf", "hoja_ejemplo.pdf"], "salida_unida.pdf"))
    
    # Separar PDF
    print(PDFHandler.split_pdf(test_pdf, "./", page_range=(3, 5)))
    
    # Convertir imágenes a PDF
    print(PDFHandler.image_to_pdf(test_images, "images_output.pdf"))
        
if __name__ == "__main__":
    main()