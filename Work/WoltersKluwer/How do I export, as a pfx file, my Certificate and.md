How do I export, as a pfx file, my Certificate and Private Key from Apache?

How do I export, as a pfx file, my Certificate and Private Key from Apache?
In order to export the Certificate, Private Key and any intermediate certificate as a pfx file use the command below:

> openssl pkcs12 -export -in my.crt -inkey my.key -certfile my.bundle -out my.pfx

Note: Remember to change the names to match your file names!