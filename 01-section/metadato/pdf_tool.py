from PyPDF2 import PdfReader, PdfWriter
from pypdf import PdfWriter as PypdfWriter
from PIL import Image
import os

class PDFHandler:
    @staticmethod
    def merge_pdfs(input_paths, output_path="merged.pdf"):
        """
        Une múltiples PDFs en un solo archivo.
        """
        try:
            writer = PdfWriter()
            for path in input_paths:
                reader = PdfReader(path)
                for page in reader.pages:
                    writer.add_page(page)
            with open(output_path, "wb") as f:
                writer.write(f)
            return {"success": f"PDFs unidos en {output_path}"}
        except Exception as e:
            return {"error": f"Error al unir PDFs: {str(e)}"}

    @staticmethod
    def split_pdf(input_path, output_dir="split_pages", page_range=None):
        """
        Separa un PDF en páginas individuales o un rango específico.
        page_range: Tupla (start, end) o None para todas las páginas.
        """
        try:
            reader = PdfReader(input_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            pages = reader.pages
            if page_range:
                start, end = page_range
                pages = pages[start-1:end]
            results = []
            for i, page in enumerate(pages, 1):
                writer = PdfWriter()
                writer.add_page(page)
                output_path = os.path.join(output_dir, f"page_{i}.pdf")
                with open(output_path, "wb") as f:
                    writer.write(f)
                results.append(output_path)
            return {"success": f"Páginas separadas en {output_dir}", "files": results}
        except Exception as e:
            return {"error": f"Error al separar PDF: {str(e)}"}

    @staticmethod
    def image_to_pdf(image_paths, output_path="image_to_pdf.pdf"):
        """
        Convierte imágenes (JPEG/PNG) a un PDF.
        """
        try:
            images = []
            for path in image_paths:
                img = Image.open(path)
                if img.mode != 'RGB':
                    img = img.convert('RGB')  # Convertir a RGB para compatibilidad
                images.append(img)
            if not images:
                return {"error": "No se proporcionaron imágenes válidas"}
            images[0].save(output_path, save_all=True, append_images=images[1:])
            return {"success": f"Imágenes convertidas a PDF en {output_path}"}
        except Exception as e:
            return {"error": f"Error al convertir imágenes a PDF: {str(e)}"}
