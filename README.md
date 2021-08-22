# sap_extraction

Bot para extracción de transacción FBL5N en SAP Fiori

Las librerías utilizadas son:
- Selenium
- Datatime
- Environs (para protección de credenciales)

El primer paso es ingresar a la transacción de SAP, mediante selenium se realizan todos los clicks correspondientes y se logra ingresar y descargar la data en formato excel. 