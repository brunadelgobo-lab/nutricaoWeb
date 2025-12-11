from django.db import models
import hashlib

# define como ficará armazenado os dados no banco de dados
class Nutricionista(models.Model):
    nome_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    crn = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    senha = models.CharField(max_length=200)

    # função que pega a senha cadastrada e criptografa ela com SHA256
    def set_password(self, raw_password):
        hash_obj = hashlib.sha256(raw_password.encode('utf-8'))
        self.senha = hash_obj.hexdigest()

    # função que verifica se a senha informada é a mesma guardada no banco, se sim, libera o acesso
    def check_password(self, raw_password):
        hash_obj = hashlib.sha256(raw_password.encode('utf-8'))
        return self.senha == hash_obj.hexdigest()

    def __str__(self):
        return self.nome_completo
