# sap_extraction

Bot para extracción de transacción FBL5N en SAP Fiori

Las librerías utilizadas son:
- Selenium
- Datatime
- Environs (para protección de credenciales)

En primer lugar, se definió la función descarga que ingresa a la transacción de SAP, mediante selenium se realizan todos los clicks correspondientes para poder realizar el flujo completo y extraer los datos.

Para poder realizar inspection en una scrollbar, se basó en lo siguiente:
https://twitter.com/sulco/status/1305841873945272321

Cabe destacar que SAP posee frames, es decir páginas dentro de otra página por lo que hay que utilizar switch para ingresar.
