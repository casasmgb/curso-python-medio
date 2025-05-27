from metadato.metadata_extract import MetadataExtract

def main():
    extractor = MetadataExtract()
    test_image = "IMG_20250523_093201.jpg"  
    test_audio = "Color_Out_-_Host.mp3"     
    test_pdf = "Documentos.pdf"
        
    image_metadata = extractor.extract_image_metadata(test_image)
    audio_metadata = extractor.extract_audio_metadata(test_audio)
    pdf_metadata = extractor.extract_pdf_metadata(test_pdf)
    
    print ('[+] Metadatos de Imagen')
    for k,v in image_metadata.items():
        if type(v) == dict:
            for k1,v1 in v.items():
                print (f'\t\t{k1}:\t {v1}')    
        else:
            print (f'\t{k}:\t {v}')
        
    print ('[+] Metadatos de Audio')
    for k,v in audio_metadata.items():
        print (f'\t{k}:\t {v}')
        
    print ('[+] Metadatos de PDF')
    for k,v in pdf_metadata.items():
        print (f'\t{k}:\t {v}')
        
if __name__ == "__main__":
    main()