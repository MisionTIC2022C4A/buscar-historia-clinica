# buscar-historia-clinica
Microservicio hecho en Django para buscar la historia clínica de un paciente.

```
heroku login
heroku container:login
heroku create historia-clinica-ms
heroku container:push web --app historia-clinica-ms
heroku container:release web --app historia-clinica-ms
```
