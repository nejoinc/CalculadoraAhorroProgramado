CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY IDENTITY,
    nombre VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    fecha_registro DATETIME DEFAULT GETDATE()
);