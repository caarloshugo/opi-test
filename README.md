# API para consumo de modelo predictivo del proyecto Dragon

## Descripción

Este proyecto genera una API a traves de una función Lambda y el API Gateway de AWS, esta API es para consumir el modelo predictivo del proyecto Dragon
También genera una función lambda para el autorizador que para motivos del demo solo responde con el token "allow"

## Requisitos

Para poder ejecutar el proyecto se necesita tener previamente instalado nodeJS 10 o superior

### NodeJs y npm

```bash
# Guia https://nodejs.org/en/download/package-manager/

# Usando Ubuntu
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# Usando Debian, como root
curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt-get install -y nodejs
```

### Reposotorio

```bash
# Clonar repositorio
git clone [repositorio]
cd dragon

```

### AWS CLI 2

```bash
# Usar la siguiente guia dependiendo del sistema operativo
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
```

Se necesita tener cuenta de aws con permisos `full access` de `lambda`
Nota: solo se necesita para poder subir el proyecto a una `lambda`

## Herramientas

Las siguientes herramientas son usadas a lo largo del proyecto, esta descrita su funcionabilidad y en algunas un link para ver su documentación general

### Serverless

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
Framework que permite crear funciones lambda y poderlas subir a AWS
<https://www.serverless.com/framework/docs/>

```bash
# Instalar dependencia
npm install -g serverless

#Hacer estte paso nuevamente desde la carpeta de authorizer "cd ../authorizer"
```

## Scripts

```bash
#Primero se tiene que hacer deploy del autorizador
cd authorizer
serverless deploy --aws-profile [nombre del perfil]

#Esto va generar una función lambda en AWS. Vamos a obtener el ARN de esta función y remplazarlo en el serverless.yml por [your-arn-lambda-authorizer] de la función lambda del modelo para ligar el autorizador

# Deploy del modelo a AWS
serverless deploy --aws-profile [nombre del perfil]
```

## Llamar a la API
```bash
#Para mandar a llamar a la API de prueba con curl via GET. api-key: LJN3omdPaQ6dkD024Ua2j5qPmnOuFcos7v9uDu6c, parametros: number1 y number2
curl --location --request GET 'https://gvs9dx2fai.execute-api.us-west-2.amazonaws.com/dev/model?number1=2&number2=3' \
--header 'x-api-key: LJN3omdPaQ6dkD024Ua2j5qPmnOuFcos7v9uDu6c' \
--header 'authorizationToken: allow'
```

## Comandos de referencia

```bash
#Crear api key
aws apigateway create-api-key --name 'Dev API Key' --description 'Used for development' --enabled --stage-keys restApiId='[restApiId]',stageName='dev' --profile [profile]

#Crear usage plan
aws apigateway create-usage-plan --name "Dragon plan dev - test" --description "Dragon plan dev -test" --api-stages apiId=[apiId],stage=dev --throttle burstLimit=1000,rateLimit=1000 --quota limit=86400000,offset=0,period=DAY --profile [profile]

#Ligar api key con usage plan
aws apigateway create-usage-plan-key --usage-plan-id [usage-plan-id] --key-type "API_KEY" --key-id [key-id]  --profile [profile]
```

## Autor

- **Carlos Hugo Gonzalez**

