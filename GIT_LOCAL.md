A continuación se muestran los pasos para crear un repositorio Git local, hacer cambios y subir estos cambios a un repositorio remoto:

### 1. Crear un Repositorio Local
- **Inicializar el Repositorio:**
  - Abre VSCode y navega a la carpeta donde quieres crear el repositorio.
  - Abre el terminal en VSCode (Terminal → Nuevo Terminal).
  - Inicializa el repositorio con `git init`.
- **Agregar Archivos:**
  - Crea o añade archivos existentes a la carpeta.
  - Prepara los archivos con `git add .` (para agregar todos los archivos) o `git add [nombre del archivo]` (para agregar archivos específicos).

### 2. Confirmar Cambios Localmente
- **Confirmar Cambios:**
  - Después de preparar los archivos, confírmalos en el repositorio con `git commit -m "Commit inicial"` (reemplaza el mensaje con uno relevante).
- **Ver Historial de Commits:**
  - Puedes ver el historial de commits usando `git log`.

### 3. Conectarse a un Repositorio Remoto
- **Crear un Repositorio Remoto:**
  - Usa un servicio como GitHub, GitLab o Bitbucket para crear un nuevo repositorio remoto.
- **Vincular el Repositorio Local al Remoto:**
  - En el terminal, vincula tu repositorio local al remoto con `git remote add origin [URL del repositorio remoto]`.
  - Verifica la conexión usando `git remote -v`.

### 4. Subir al Repositorio Remoto
- **Primera Subida:**
  - Para la primera subida, usa `git push -u origin master` (reemplaza 'master' con el nombre de tu rama si es diferente).
- **Subidas Subsecuentes:**
  - Para subidas posteriores, simplemente usa `git push`.

### 5. Clonar y Tirar del Repositorio Remoto
- **Clonar:**
  - Para clonar el repositorio en otro lugar, usa `git clone [URL del repositorio remoto]`.
- **Tirar Cambios:**
  - Para tirar cambios del repositorio remoto, usa `git pull`.

### Consejos Adicionales
- **Archivo .gitignore:**
  - Crea un archivo `.gitignore` para excluir archivos o carpetas de ser rastreados.
- **Ramas:**
  - Usa ramas para diferentes características o versiones con `git branch [nombre de la rama]` y cambia entre ellas con `git checkout [nombre de la rama]`.
- **Fusionar Cambios:**
  - Fusiona cambios de diferentes ramas en la rama principal con `git merge [nombre de la rama]`.
